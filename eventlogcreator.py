#!/usr/bin/python3
import time
import subprocess

fichier = "rscd.log"
"""
What this tool is used for :

It creates a Windows 'Application' log if it finds the specified line in the RSCD log file.
Currently in 'debug' mode, that's why I'm using the while(x>=1)

Upgrade possibilities : 
- convert to while(True), and add an except KeyboardInterrupt
"""
x=1
while(x>=1):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
        if len(lignes) > 9:
            last_lines = []
            for i in range(1,11,1):
                last_lines.append(lignes[-i])
        else:
            last_lines = lignes
    # formatting, just because :)
    for i in range(len(last_lines)):
        last_lines[i] = last_lines[i].strip()
    for i in range(len(last_lines)):
        if "Failed to map user to local user" in last_lines[i]:
            subprocess.Popen(["powershell", "Write-EventLog -LogName 'Application' -Source 'rscdsvc' -EventID 6789 -EntryType Warning -Message 'A remote Host managed to enumerate users on this machine'"], stdout=subprocess.PIPE)
            print(last_lines)
    time.sleep(30)
    x-=1