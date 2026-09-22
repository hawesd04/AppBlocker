import subprocess, ctypes, os, sys, platform, time
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFrame, QTimeEdit, QProgressBar, QFileDialog
from PySide6.QtCore import QDateTime, QTimer
from PySide6.QtGui import QCloseEvent, QIcon
from block_mainwindow_ui import Ui_MainWindow

def default_hosts_path() -> str:
    system = platform.system()
    if (system == "Windows"):
        return r"C:\Windows\System32\drivers\etc"
    else: # mac / linux
        return "/etc"

def pick_hosts_file(parent=None) -> str | None:
    path, _ = QFileDialog.getOpenFileName(parent,"Select hosts file",default_hosts_path(),"All Files (*)")
    return path or None

def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)

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
    

def getTime(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60

    minuteStr = ""
    if (minutes < 10):
        minuteStr=f"0{minutes}"
    else: minuteStr =f"{minutes}"

    hourStr = ""
    if (hours < 10):
        hourStr=f"0{hours}"
    else: hourStr =f"{hours}"

    return [f'{hourStr}',f'{minuteStr}']


def block(filepath, block_string):
    print(f'blocking discord in filepath: {filepath}')
    with open(filepath, "a") as file:
        file.writelines(block_string);

def unblock(filepath):
    BLOCK_TAGS = ("#discord-blocker", "#instagram-blocker", "#twitter-blocker", "#youtube-blocker", "facebook-blocker", "tiktok-blocker", "bsky-blocker")
    with open(filepath, "r") as file:
        lines = file.readlines()

    # keep a list of all lines in lines where any of the above blocked tags are not included.
    kept = [line for line in lines if not any(tag in line for tag in BLOCK_TAGS)]

    # drop the blank lines left behind by additions to block_string
    while kept and kept[-1].strip() == "":
        kept.pop()

    with open(filepath, "w") as file:
        file.writelines(kept)
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # use compiled ui
        self.setupUi(self)

        self.duration = 0
        self.end_time = 0
        self.progressBar.setValue(0)

        self.block_timer = QTimer(self)
        self.block_timer.setInterval(1000)
        self.block_timer.timeout.connect(self.on_block_tick)

        self.cancel = False
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
            'instagram': 
                "\n127.0.0.1 www.instagram.com #instagram-blocker" + 
                "\n127.0.0.1 instagram.com #instagram-blocker",
            'tiktok':
                "\n127.0.0.1 tiktok.com #tiktok-blocker" +
                "\n127.0.0.1 www.tiktok.com #tiktok-blocker",
            'bsky':
                "\n127.0.0.1 bsky.app #bsky-blocker",
            'facebook':
                "\n127.0.0.1 facebook.com #facebook-blocker" +
                "\n127.0.0.1 www.facebook.com #facebook-blocker",
            'youtube':
                "\n127.0.0.1 youtube.com #youtube-blocker" +
                "\n127.0.0.1 www.youtube.com #youtube-blocker",}
        
        self.blockStatus = {
            'twitter': False,
            'discord': False,
            'instagram': False,
            'youtube': False,
            'facebook': False,
            'bsky': False,
            'tiktok': False
        }
        self.filepath = default_hosts_path() + r"\hosts"
        self.hostFileDirectoryLabel.setText(self.filepath)

        self.setWindowTitle("App Blocker")
        self.setFixedHeight(490)

        self.startButton.setDisabled(True)
        self.startButton.clicked.connect(self.begin_blocking_clicked)

        self.cancelButton.setDisabled(True)
        self.cancelButton.clicked.connect(self.cancel_blocking_clicked)

        self.folderButton.clicked.connect(self.folder_clicked)
        
        self.durationEdit.timeChanged.connect(self.duration_edit_changed)
        self.endTimeEdit.timeChanged.connect(self.end_time_edit_changed)

        self.discordCheck.checkStateChanged.connect(self.discord_toggled)
        self.twitterCheck.checkStateChanged.connect(self.twitter_toggled)
        self.instagramCheck.checkStateChanged.connect(self.instagram_toggled)
        self.youtubeCheck.checkStateChanged.connect(self.youtube_toggled)
        self.tiktokCheck.checkStateChanged.connect(self.tiktok_toggled)
        self.facebookCheck.checkStateChanged.connect(self.facebook_toggled)
        self.bskyCheck.checkStateChanged.connect(self.bsky_toggled)

        self.midLine.setFrameShape(QFrame.NoFrame)
        self.midLine.setFixedHeight(2)
        self.midLine.setStyleSheet("background-color: #16ffffff; border: none; margin: 0; padding: 0;")
        
        self.progressGroup.setHidden(True)

        self.validPathIcon.setHidden(True)
        self.folderButton.setIcon(QIcon(resource_path("assets/folder_white.svg")))
        if (self.filepath):
            if (os.path.isfile(self.filepath) and self.filepath[-5:] == "hosts"):
                self.hostFileDirectoryLabel.setStyleSheet("color: lime;")
                self.validPathIcon.setHidden(False)

    def folder_clicked(self):
        path = pick_hosts_file(self)
        self.validPathIcon.setHidden(True)
        self.hostFileDirectoryLabel.setStyleSheet("color: gray;")
        if path:
            if(os.path.isfile(path)):
                self.filepath = path
                self.hostFileDirectoryLabel.setText(path)

                if (self.filepath[-5:] == "hosts"):
                    self.hostFileDirectoryLabel.setStyleSheet("color: lime;")
                    self.validPathIcon.setHidden(False)
                    if (self.duration > 0):
                        self.startButton.setDisabled(False)

        if (self.validPathIcon.isHidden()):
            self.startButton.setDisabled(True)

                    

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

    def instagram_toggled(self):
        print("instagram toggled")
        self.blockStatus["instagram"] = self.instagramCheck.isChecked()

    def youtube_toggled(self):
        print("youtube toggled")
        self.blockStatus["youtube"] = self.youtubeCheck.isChecked()

    def tiktok_toggled(self):
        print("tiktok toggled")
        self.blockStatus["tiktok"] = self.tiktokCheck.isChecked()

    def facebook_toggled(self):
        print("facebook toggled")
        self.blockStatus["facebook"] = self.facebookCheck.isChecked()

    def bsky_toggled(self):
        print("bluesky toggled")
        self.blockStatus["bsky"] = self.bskyCheck.isChecked()

    

    # ---------------------------------------------------------------------------------

    def cancel_blocking_clicked(self):
        self.end_blocking()

    def on_block_tick(self):
        remaining = self.end_time - time.monotonic()
        percent = min(100, (1 - remaining / self.duration) * 100)
        self.progressBar.setValue(int(percent))

        timeArr = getTime(remaining)

        self.progressLabel.setText(f"Blocking Progress: {timeArr[0][:-2]}:{timeArr[1][:-2]} remaining")



        if (remaining <= 0):
            self.end_blocking()

    def begin_blocking_clicked(self):
        self.block_string = self.build_string()
        self.startButton.setDisabled(True)
        #print(self.block_string)

        print(f"Begin Blocking...")

        self.progressGroup.setHidden(False)
        self.setMaximumHeight(590)
        self.setFixedHeight(590)
        self.cancelButton.setDisabled(False)

        print(f'Blocked time set to {self.duration} seconds' )

        block(self.filepath, self.block_string)
        self.end_time = time.monotonic() + self.duration
        self.block_timer.start()

    def end_blocking(self):
        self.block_timer.stop()
        unblock(self.filepath)
        flushdns()
        self.cancelButton.setDisabled(True)
        self.startButton.setDisabled(False)
        self.setFixedHeight(490)
        self.setMaximumHeight(490)
        self.progressGroup.setHidden(True) 

    def duration_edit_changed(self):
        durEditObj = self.durationEdit.time()

        durationStr = durEditObj.toString()
        hours = durEditObj.hour()
        minutes = durEditObj.minute()

        self.duration = (hours * 3600) + (minutes * 60)
        self.selectedDurationLabel.setText(f"Blocking for a duration of: {durationStr[:-3]}")

        if (self.duration > 0 and not (self.validPathIcon.isHidden())):
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

        if (self.duration > 0 and not (self.validPathIcon.isHidden())):
            self.startButton.setDisabled(False)

        print(f"the duration is: {self.duration} seconds")

        timeArr = getTime(self.duration)

        self.selectedDurationLabel.setText(f"Blocking for a duration of: {timeArr[0]}:{timeArr[1]}")

    def closeEvent(self, event: QCloseEvent):
        print("closing program")
        if self.block_timer.isActive():
            self.end_blocking()
        super().closeEvent(event)



        


'''
    Main method, checks for admin priviledge, grants it if not available, and blocks access
    starts timer, and ends block after sleep period.
'''
if __name__ == "__main__": 
    # You need one QApplication instance per application.
    # Passing sys.argv allows command line args for the application.
    # If no command line, use QApplication([])

    # resolve qss path to allow access to items in ./assets that are not accessible from build directory
    os.chdir(resource_path("."))

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("assets/db.ico")))

    # Create a Qt widget (window)
    window = MainWindow()
    window.show() # enables window visibility

    with open(resource_path("discordblocker.qss"), encoding="utf-8") as f:
        style = f.read()
        app.setStyleSheet(style)



    # Starts the QApplication event loop!
    if (is_admin()):
        sys.exit(app.exec())
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None,                       # parent window handle
            "runas",                    # lpOperation ("runas" requests elevation)
            sys.executable,             # lpFile (app to run, python interp)
            " ".join([f'"{arg}"' for arg in sys.argv]), #arguments/params
            None,                       # lpDirectory (none is current)
            1                           # nshowcmd: 1 menas showNormal (window)
        )
    

    # this code beyond exec does not get executed until when the application end event is called.
    # run_block(300, block_string, filepath)