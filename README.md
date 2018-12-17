# dfvfs_extractor
Repository fo  Daily Blog Challenge#569 2018-12-16 | https://www.hecfblog.com/2018/12/daily-blog-569-sunday-funday-121618.html


Example
--------

Extract file + sha256 hash of `/windows/system32/cmd.exe` from image :
```
 $>python2 sunday_funday_569.py -i HRServer_Disk0.e01 --target /windows/system32/cmd.exe --hash --extract ./output_folder

[2018-12-17 07:31:04][sunday_funday_569] Extractor:
[2018-12-17 07:31:04][sunday_funday_569]   - Extracting Files: False
[2018-12-17 07:31:04][sunday_funday_569]   - Processing hash: True (sha256)
The following Volume Shadow Snapshots (VSS) were found:

Identifier      Creation Time
vss1            2018-08-07 23:07:58.0441283
Please specify the identifier(s) of the VSS that should be processed:
Note that a range of stores can be defined as: 3..5. Multiple stores
can be defined as: 1,3,5 (a list of comma separated values). Ranges
and lists can also be combined as: 1,3..5. The first store is 1. All
stores can be defined as "all". If no stores are specified none will
be processed. You can abort with Ctrl^C.

VSS identifier(s):all
[2018-12-17 07:31:08][sunday_funday_569] Start processing /vss1
[2018-12-17 07:31:09][sunday_funday_569]    - vss1_windows_system32_cmd.exe: 935c1861df1f4018d698e8b65abfa02d7e9037d8f68ca3c2065b6ca165d44ad2
[2018-12-17 07:31:09][sunday_funday_569] Start processing /p1
[2018-12-17 07:31:10][sunday_funday_569]    - p1_windows_system32_cmd.exe: 935c1861df1f4018d698e8b65abfa02d7e9037d8f68ca3c2065b6ca165d44ad2
```

Compute the hash (sha256) of files inside a directory
```
$>python2 sunday_funday_569.py -i HRServer_Disk0.e01 --target /windows/system32/winevt/logs --hash 
[2018-12-17 07:34:10][sunday_funday_569] Extractor:
[2018-12-17 07:34:10][sunday_funday_569]   - Extracting Files: False
[2018-12-17 07:34:10][sunday_funday_569]   - Processing hash: True (sha256)
The following Volume Shadow Snapshots (VSS) were found:

Identifier      Creation Time
vss1            2018-08-07 23:07:58.0441283
Please specify the identifier(s) of the VSS that should be processed:
Note that a range of stores can be defined as: 3..5. Multiple stores
can be defined as: 1,3,5 (a list of comma separated values). Ranges
and lists can also be combined as: 1,3..5. The first store is 1. All
stores can be defined as "all". If no stores are specified none will
be processed. You can abort with Ctrl^C.

VSS identifier(s):
[2018-12-17 07:34:13][sunday_funday_569] Start processing /p1
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-EapMethods-Ttls%4Operational.evtx: 1562c0bb2db76fbf63096b934826f7b0917e2f82411e311efe9a6319158cc631
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Application.evtx: b7f6b95d010553b2ad49123bcd700c081d7ee58aedc04a7605e5c8e2a4ad5cb2
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_HardwareEvents.evtx: fe55cd1fa7d3489ab4110a9884ad5757e8d5e4107b2350497725758fbe0fc1e6
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Internet Explorer.evtx: b790c872a389511da32f190adf66f301283c86a7acbbbfcfe154c70858fae70d
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Key Management Service.evtx: b790c872a389511da32f190adf66f301283c86a7acbbbfcfe154c70858fae70d
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NdisImPlatform%4Operational.evtx: 5e59f7e070a456470d0f2c494cd0816a7bd3d05b426bf39e76ccaefa59cc5bbf
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkLocationWizard%4Operational.evtx: 0c39e53ea57b7fb5e1e2d98075de895568f47e1845c60bf4219a76fcc782a108
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkProfile%4Operational.evtx: ae71cabd2cbd318a20bbae4a3e40e10064ce0e4418c23cbe0dad5e1cd58fba00
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkProvider%4Operational.evtx: 2eb9c88272d9b5518c16c10ac44e97249716b0420e508513a8b837a8677b61bd
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NlaSvc%4Operational.evtx: 2cf9762ca9e533722a572dad4432c29b07ff75d5f5d3b4d5dc62e5fd25517550
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-Ntfs%4Operational.evtx: 80f230355ce4d868b68a6f02e28deefd3ca1d9d285a0fd3d0369f86d2df5db33
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-Ntfs%4WHC.evtx: 892d4b6a74bcc14c1413495203881860157f8034bdbd827645e2101f35a2fef8
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NTLM%4Operational.evtx: 52e970f13c8080bc03d6927f2a03c0908d0f252c35b76d897ddc6e9b0cd81512
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-OfflineFiles%4Operational.evtx: 1562c0bb2db76fbf63096b934826f7b0917e2f82411e311efe9a6319158cc631
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-OneBackup%4Debug.evtx: e7f3357a7cc30bbd43f9174b4b5ae84daea8543a91aab56c298d7ec33e0ef024
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-OOBE-Machine-DUI%4Operational.evtx: 8040f74274a52115a8d5d72802bddb20111b4dd414cf3b30eabb0573eedfdca4
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-Partition%4Diagnostic.evtx: 41059d3d031ed3b0206ad278736c34d7a5b045a49054d2672b7e3654d7905c25
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-PerceptionRuntime%4Operational.evtx: 17dfa8e4ca74c842f9c5a52a4ac55821f0ac01a012bb4e8eabe7dc5700f92777
[2018-12-17 07:34:14][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-PowerShell%4Admin.evtx: 9f120c38445a157d836ae7e9248177fd0e726c132338676aab7d47aae273bb9b
[...] // End snip
```

Compute the hash (md5) + extract of files inside a directory, recursive with shadow copies
```
$> python2 sunday_funday_569.py -i HRServer_Disk0.e01 --target /windows/system32/winevt/logs --hash --extract out_folder/win_logs --recurse --algo md5

[2018-12-17 07:36:51][sunday_funday_569] Extractor:
[2018-12-17 07:36:51][sunday_funday_569]   - Extracting Files: True
[2018-12-17 07:36:51][sunday_funday_569]   - Processing hash: True (md5)
The following Volume Shadow Snapshots (VSS) were found:

Identifier      Creation Time
vss1            2018-08-07 23:07:58.0441283
Please specify the identifier(s) of the VSS that should be processed:
Note that a range of stores can be defined as: 3..5. Multiple stores
can be defined as: 1,3,5 (a list of comma separated values). Ranges
and lists can also be combined as: 1,3..5. The first store is 1. All
stores can be defined as "all". If no stores are specified none will
be processed. You can abort with Ctrl^C.

VSS identifier(s):all
[2018-12-17 07:36:56][sunday_funday_569] Start processing /vss1
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_Application.evtx: f2599f943d8db08015eed5c5ed6b8517
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_HardwareEvents.evtx: 13cea5122548b7c434ae6c81db201a82
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_Internet Explorer.evtx: a55fe49683c29388694af6ac8d49b480
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_Key Management Service.evtx: a55fe49683c29388694af6ac8d49b480
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_Microsoft-Windows-NetworkProfile%4Operational.evtx: 02c71d0409952ffdaa0e074cc9ab2bbc
[2018-12-17 07:36:58][sunday_funday_569]    - vss1_windows_system32_winevt_logs_Microsoft-Windows-Ntfs%4Operational.evtx: 3f136642b351fbb507a06261359fdb15
[...]
[2018-12-17 07:36:58][sunday_funday_569] Start processing /p1
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-EapMethods-Ttls%4Operational.evtx: 88e19d126dab89378bf0485e6ff6bdd7
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Application.evtx: 9622372e9c4b50d3f872fa39218d3662
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_HardwareEvents.evtx: 13cea5122548b7c434ae6c81db201a82
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Internet Explorer.evtx: a55fe49683c29388694af6ac8d49b480
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Key Management Service.evtx: a55fe49683c29388694af6ac8d49b480
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NdisImPlatform%4Operational.evtx: f63b397d2f79478620bc3dff8475b9a3
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkLocationWizard%4Operational.evtx: d77831833fe34cf0354d049e368a8802
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkProfile%4Operational.evtx: 02c71d0409952ffdaa0e074cc9ab2bbc
[2018-12-17 07:36:59][sunday_funday_569]    - p1_windows_system32_winevt_logs_Microsoft-Windows-NetworkProvider%4Operational.evtx: 361961c886c34509ca14d5e021fc0698
[...]

$> find out_folder/ | head -n10

out_folder/
out_folder/win_logs
out_folder/win_logs/p1_windows_system32_winevt_logs_Application.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_HardwareEvents.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Internet Explorer.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Key Management Service.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Microsoft-AppV-Client%4Admin.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Microsoft-AppV-Client%4Operational.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Microsoft-AppV-Client%4Virtual Applications.evtx
out_folder/win_logs/p1_windows_system32_winevt_logs_Microsoft-Client-Licensing-Platform%4Admin.evtx

```
