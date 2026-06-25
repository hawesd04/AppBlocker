import subprocess
import ctypes
import os
import sys
import time


def flushdns():
    try:
        result = subprocess.run(
            ["ipconfig","/flushdns"],
            capture_output=True,
            text=True,
            check=True
        )
        
        print("Success:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred (Exit Code {e.returncode}):")
        print(e.stderr)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

def block(filepath, block_string):
    print(f'blocking discord in filepath: {filepath}')
    with open(filepath, "a") as file:
        file.writelines(block_string);

def unblock(filepath):
    print(f'unblocking discord in filepath: {filepath}')
    lines = ''

    with open(filepath, "r") as file: 
        lines = file.readlines();

    with open(filepath, "w") as file:
        for line in lines:
            if "#discord-blocker" not in line:
                file.write(line)
        


'''
    Main method, checks for admin priviledge, grants it if not available, and blocks access
    starts timer, and ends block after sleep period.
'''
if __name__ == "__main__": 
    if (is_admin()):
        filepath = r"C:\Windows\System32\drivers\etc\hosts"
        block_string = [
            "\n127.0.0.1 discord.com #discord-blocker",
            "\n127.0.0.1 discord.gg #discord-blocker",
            "\n127.0.0.1 discordapp.com #discord-blocker",
            "\n127.0.0.1 discord.co #discord-blocker",
            "\n127.0.0.1 dis.gd #discord-blocker",
            "\n127.0.0.1 x.com #discord-blocker",
            "\n127.0.0.1 x.com #discord-blocker",
            "\n127.0.0.1 www.x.com #discord-blocker",
            "\n127.0.0.1 twitter.com #discord-blocker",
            "\n127.0.0.1 www.twitter.com #discord-blocker",
            "\n127.0.0.1 t.co #discord-blocker",
        ]

        factor = -1
        while (factor != 0 and factor != 1):
            factor = int(input('Minutes (0) or Hours (1): '))
            
        factorStr = ''
        if (factor == 0): factorStr = 'Minutes' 
        elif (factor == 1): factorStr = 'Hours'

        duration = int(input(f'Amount of time in {factorStr}: '))
        print(f'Blocked time set to {duration} {factorStr}' )

        block(filepath, block_string)

        flushdns()

        if (factor == 0):
            # factors of 1 minute
            total_seconds = 60 * duration
            for i in range(total_seconds):
                time.sleep(1)
                percent = (i + 1) / total_seconds * 100
                bar = '■' * int(percent // 2)
                print(f'\r[{bar:<50}] {percent:.1f}%', end='')

        elif (factor == 1):
            # factors of 60 minutes
            total_seconds = 60 * 60 * duration
            for i in range(total_seconds):
                time.sleep(1)
                percent = (i + 1) / total_seconds * 100
                bar = '■' * int(percent // 2)
                print(f'\r[{bar:<50}] {percent:.1f}%', end='')
        else: 
            print('Factor configured incorrectly')

        unblock(filepath)

        flushdns()
            
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None,                       # parent window handle
            "runas",                    # lpOperation ("runas" requests elevation)
            sys.executable,             # lpFile (app to run, python interp)
            " ".join([f'"{arg}"' for arg in sys.argv]), #arguments/params
            None,                       # lpDirectory (none is current)
            1                           # nshowcmd: 1 menas showNormal (window)
        )
    