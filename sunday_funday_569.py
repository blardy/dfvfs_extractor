#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I did not succeed to get it working using python3... // Switching to python2 ;(
#   todo: check with another mediator
#
#   File "/home/XXXXXXXX/.local/lib/python3.6/site-packages/dfvfs/helpers/command_line.py", line 584, in _ReadSelectedVolumes
#     volume_identifiers_string = self._input_reader.Read()
#   File "/home/XXXXXXXX/.local/lib/python3.6/site-packages/dfvfs/helpers/command_line.py", line 76, in Read
#     string = codecs.decode(encoded_string, self._encoding, self._errors)
#   TypeError: decoding with 'UTF-8' codec failed (TypeError: a bytes-like object is required, not 'str')
from __future__ import print_function
from __future__ import unicode_literals


__progname__ = "sunday_funday_569"
__author__ = "Bastien Lardy"

import logging
import argparse
import hashlib
import os
import re

from dfvfs.lib import definitions
from dfvfs.helpers import command_line
from dfvfs.helpers import volume_scanner
from dfvfs.resolver import resolver
from dfvfs.path import factory as path_spec_factory

LOG_FORMAT = '[%(asctime)s]' + '[{}]'.format(__progname__) + ' %(message)s'
LOG_VERBOSITY = {
    'DEBUG' : logging.DEBUG,
    'INFO' : logging.INFO,
    'WARNING' : logging.WARNING,
    'ERROR' : logging.ERROR,
    'CRITICAL' : logging.CRITICAL,
}


class Extractor(object):
    _READ_BUFFER_SIZE = 32768

    def __init__(self, extract_folder = '.', process_hash = False, process_list = False, hash_algo='sha256'):
        self.extract_folder = extract_folder
        self.process_hash = process_hash
        self.hash_algo = hash_algo

        logging.info('Extractor:')
        logging.info('  - Listing Files: {}'.format('True' if process_list else 'False'))
        logging.info('  - Extracting Files: {}'.format('True' if extract_folder else 'False'))
        logging.info('  - Processing hash: {} ({})'.format(process_hash, self.hash_algo if process_hash else '-'))

        # Q&D
        hashlib.new(self.hash_algo)


    def _process_data_stream(self, file_entry, data_stream, prefix = ''):
        # performing all tasks when reading the file as it improve perf.
        """ Process a data stream from the given file_entry.
            if self.process_hash is True then Hash will be compute.
            if self.extract_folder is not None then the data_stream will be extracted
            Args:
                file_entry  (dfvfs.FileEntry): file entry.
                data_stream (str): name of the data stream to extract.
                prefix (str): prefix to use for output.
            return:
                tuples (str(filename), str(hash))
        """
        hash_context = hashlib.new(self.hash_algo)

        output_file = None
        resulted_hash = None

        # Compute output filename
        filename = prefix + file_entry.name
        if data_stream:
            filename += '_' + data_stream

        try:
            logging.debug('    ==> Extracting {}'.format(filename))
            file_object = file_entry.GetFileObject(data_stream_name=data_stream)
            if not file_object:
                return (None, None)

            if self.extract_folder:
                output_file = open('{}/{}'.format(self.extract_folder, filename), 'wb')

            data = file_object.read(self._READ_BUFFER_SIZE)
            while data:
                if self.process_hash:
                    hash_context.update(data)
                if self.extract_folder:
                    output_file.write(data)

                data = file_object.read(self._READ_BUFFER_SIZE)

        except Exception as e:
            logging.error(e)

        finally:
            file_object.close()
            if output_file:
                output_file.close()
                logging.debug('  - extracted: {}/{}'.format(self.extract_folder, filename))
            if self.process_hash:
                resulted_hash = hash_context.hexdigest()
                logging.debug('  - sha256: {}'.format(resulted_hash))

        return (filename, resulted_hash)


    def process(self, file_entry, prefix = '', recurse = False, ads = True, filter = None):
        """Process the given file entry.
            Args:
                file_entry  (dfvfs.FileEntry): file entry.
                prefix (str): prefix for the extracted filename.
                recurse (boolean): boolean for recursive iteration.
                ads (boolean): process Alternate Datastream.
            return:
                Iterator of tuples (filename, hash)
        """
        logging.debug('Extract {} using prefix {}, recurse={}'.format(file_entry.name, prefix, recurse))

        # Only process File and Directories
        if not file_entry.IsFile() and not file_entry.IsDirectory():
            return

        # Create the output directory if it does not exist
        if self.extract_folder and not os.path.exists(self.extract_folder):
            os.makedirs(self.extract_folder)

        # process an individual file
        if file_entry.IsFile():
            if not filter or filter.search(file_entry.name):
                for data_stream in file_entry.data_streams:
                    if data_stream.name and not ads:
                        continue
                    filename, filehash = self._process_data_stream(file_entry, data_stream.name, prefix)
                    logging.debug('{}|{}'.format(filename, filehash))
                    yield (filename, filehash)

        # If the given entry is a Directory, we iterate over the sub entries
        for sub_file_entry in file_entry.sub_file_entries:
            sub_prefix = prefix + '_'

            # Skip this directory if we do not recurse
            if sub_file_entry.IsDirectory() and not recurse:
                continue
            # Update prefix if we are processing this directory
            elif sub_file_entry.IsDirectory():
                sub_prefix = '{}{}'.format(sub_prefix, sub_file_entry.name)

            # Process the sub entries
            for x in self.process(sub_file_entry, prefix=sub_prefix , recurse=recurse, ads=ads):
                yield x



def sunday_funday_569():
    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", choices = LOG_VERBOSITY)
    parser.add_argument("-i", "--image", required=True, help="filename of a storage media image")
    parser.add_argument("--target", required=True, help="file to extract / compute hash")

    parser.add_argument("--extract", help="Output folder")
    parser.add_argument("--hash", action='store_true', help="compute hash of the specified file")
    parser.add_argument("--list", action='store_true', help="print the specified target file if it exists")

    parser.add_argument("--filter", type=re.compile, help="Output folder")

    parser.add_argument("--algo", default='sha256', help="Output folder")
    parser.add_argument("--recurse", action='store_true', help="Enable recursivity if target is a folder")
    parser.add_argument("--noads", action='store_false', help="Disable ADS (Alternate Data Stream) processing")

    args = parser.parse_args()

    # configure logging
    logging.basicConfig(format=LOG_FORMAT, level=LOG_VERBOSITY.get(args.verbosity, 'INFO'), datefmt='%Y-%m-%d %I:%M:%S')

    if not args.extract and not args.hash and not args.list:
        logging.error('Please specify at least an action --hash or --extract <folder>')
        return

    try:
        # Instanciate the processing class
        extractor = Extractor(extract_folder = args.extract, process_hash = args.hash, process_list = args.list, hash_algo=args.algo)

        # dfvfs mediator for handling shadow // using interactive command line
        mediator = command_line.CLIVolumeScannerMediator()
        # Scan the given image
        vscanner = volume_scanner.VolumeScanner(mediator = mediator)
        base_path_specs = vscanner.GetBasePathSpecs(args.image)
        # Iterate over each partition/fs found
        for base_path_spec in base_path_specs:
            logging.info('Start processing {}'.format(base_path_spec.parent.location))
            
            # Converting "args.target" to a dfvfs "path_spec" object
            tsk_path_spec = path_spec_factory.Factory.NewPathSpec(definitions.TYPE_INDICATOR_TSK, location=args.target, parent=base_path_spec.parent)
            file_entry = resolver.Resolver.OpenFileEntry(tsk_path_spec)
            
            if not file_entry:
                logging.debug('   - {} was not found on {}'.format(args.target, base_path_spec.parent.location))
                continue

            # Building prefix, this will be the prefixw of the extracted file(s)
            #   <partition_name>_<path>_<filename>
            #   or 
            #   <partition_name>_<path>
            if file_entry.IsDirectory():
                basepath = args.target.replace('/', '_').strip('_')
            else:
                basepath = '_'.join(args.target.split('/')[:-1]).strip('_') + '_'          
            prefix = '{}_{}'.format(base_path_spec.parent.location.strip('/'), basepath)

            # Process
            for filename, filehash in extractor.process(file_entry, prefix=prefix, recurse=args.recurse, ads=args.noads, filter=args.filter):
                logging.info('   - {}: {}'.format(filename, filehash))
    except Exception as e:
        logging.error(e)
        raise e


if __name__ == '__main__':
    sunday_funday_569()