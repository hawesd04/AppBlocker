import subprocess
import ctypes
import os
import sys
import time
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QTimeEdit, QProgressBar
from PySide6.QtCore import QSize, Qt, QDateTime, QTime
from block_mainwindow_ui import Ui_MainWindow

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
        

def run_block(duration_temp, block_string, filepath):
    if (is_admin()):
        # print(block_string)
        # print(filepath)
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # use compiled ui
        self.setupUi(self)

        self.duration = 0
        self.block_string = "[]"
        self.blockOpts = {
            'twitter': 
                "\n127.0.0.1 x.com #twitter-blocker" +
                "\n127.0.0.1 www.x.com #twitter-blocker" +
                "\n127.0.0.1 twitter.com #twitter-blocker" +
                "\n127.0.0.1 www.twitter.com #twitter-blocker" +
                "\n127.0.0.1 t.co #twitter-blocker",
            'discord':         
                "\n127.0.0.1 discord.com #discord-blocker" +
                "\n127.0.0.1 discord.gg #discord-blocker" +
                "\n127.0.0.1 discordapp.com #discord-blocker" +
                "\n127.0.0.1 discord.co #discord-blocker" +
                "\n127.0.0.1 dis.gd #discord-blocker",
            'telegram': 
                "\n127.0.0.1 web.telegram.org #telegram-blocker",
            'youtube': 
                "\n127.0.0.1 youtube.com #youtube-blocker" +
                "\n127.0.0.1 www.youtube.com #youtube-blocker",}
        
        self.blockStatus = {
            'twitter': False,
            'discord': False,
            'telegram': False,
            'youtube': False,
        }

        self.setWindowTitle("Application Blocker")
        self.setMinimumSize(465,410)
        self.setMaximumSize(465,410)

        self.startButton.setDisabled(True)
        self.startButton.clicked.connect(self.begin_blocking_clicked)
        
        self.durationEdit.timeChanged.connect(self.duration_edit_changed)
        self.endTimeEdit.timeChanged.connect(self.end_time_edit_changed)


        self.discordCheck.checkStateChanged.connect(self.discord_toggled)
        self.twitterCheck.checkStateChanged.connect(self.twitter_toggled)
        self.telegramCheck.checkStateChanged.connect(self.telegram_toggled)
        self.youtubeCheck.checkStateChanged.connect(self.youtube_toggled)

        self.progressFrame.setHidden(True)

    def build_string(self):
        block_string = ""
        for key, value in self.blockStatus.items():
            if (value):
                block_string += self.blockOpts[key]

        print(f"The constructed block string is now:\n---------------------------------------\n{block_string}\n---------------------------------------")
        return block_string

    # ---------------------------------------------------------------------------------

    def discord_toggled(self):
        print("discord toggled")
        self.blockStatus["discord"] = self.discordCheck.isChecked()

    def twitter_toggled(self):
        print("twitter toggled")
        self.blockStatus["twitter"] = self.twitterCheck.isChecked()

    def telegram_toggled(self):
        print("telegram toggled")
        self.blockStatus["telegram"] = self.telegramCheck.isChecked()

    def youtube_toggled(self):
        print("youtube toggled")
        self.blockStatus["youtube"] = self.youtubeCheck.isChecked()

    # ---------------------------------------------------------------------------------

    def begin_blocking_clicked(self):
        self.block_string = self.build_string()
        #print(self.block_string)

        print(f"Begin Blocking...")

        self.progressFrame.setHidden(False)

    def duration_edit_changed(self):
        durEditObj = self.durationEdit.time()

        durationStr = durEditObj.toString()
        hours = durEditObj.hour()
        minutes = durEditObj.minute()

        self.duration = (hours * 3600) + (minutes * 60)
        self.selectedDurationLabel.setText(f"Blocking for a duration of: {durationStr[:-3]}")

        if (self.duration > 0):
            self.startButton.setDisabled(False)

    def seconds_until(self, qtime):
        now = QDateTime.currentDateTime()
        target = QDateTime(now.date(), qtime)
        print(f"the time is currently {now}, and the target is {target}")
        if target <= now:
            target = target.addDays(1)

        return now.secsTo(target)
    
    def end_time_edit_changed(self):
        now = datetime.now()

        print("heyyyy")
        print(datetime.now().time())
        self.duration = self.seconds_until(self.endTimeEdit.time())

        if (self.duration > 0):
            self.startButton.setDisabled(False)

        print(f"the duration is: {self.duration} seconds")

        hours = self.duration // 3600
        minutes = (self.duration % 3600) // 60

        minuteStr = ""
        if (minutes < 10):
            minuteStr=f"0{minutes}"
        else: minuteStr =f"{minutes}"

        hourStr = ""
        if (hours < 10):
            hourStr=f"0{hours}"
        else: hourStr =f"{hours}"

        self.selectedDurationLabel.setText(f"Blocking for a duration of: {hours}:{minutes}")



        


'''
    Main method, checks for admin priviledge, grants it if not available, and blocks access
    starts timer, and ends block after sleep period.
'''
if __name__ == "__main__": 

    filepath = r"C:\Windows\System32\drivers\etc\hosts"
    block_string = [
        # "\n127.0.0.1 discord.com #discord-blocker",
        # "\n127.0.0.1 discord.gg #discord-blocker",
        # "\n127.0.0.1 discordapp.com #discord-blocker",
        # "\n127.0.0.1 discord.co #discord-blocker",
        # "\n127.0.0.1 dis.gd #discord-blocker",
        "\n127.0.0.1 x.com #twitter-blocker",
        "\n127.0.0.1 www.x.com #twitter-blocker",
        "\n127.0.0.1 twitter.com #twitter-blocker",
        "\n127.0.0.1 www.twitter.com #twitter-blocker",
        "\n127.0.0.1 t.co #twitter-blocker",
    ]

    # You need one QApplication instance per application.
    # Passing sys.argv allows command line args for the application.
    # If no command line, use QApplication([])
    app = QApplication(sys.argv)

    # Create a Qt widget (window)
    window = MainWindow()
    window.show() # enables window visibility

    # Starts the QApplication event loop!
    app.exec()

    # this code beyond exec does not get executed until when the application end event is called.
    # run_block(300, block_string, filepath)