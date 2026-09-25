import subprocess, ctypes, os, sys, platform, time
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QFileDialog
from PySide6.QtCore import QDateTime, QTimer
from PySide6.QtGui import QCloseEvent, QIcon
from block_mainwindow_ui import Ui_MainWindow

"""
    Gets the default host file path depending on whether the user's
    operating system is Windows or MacOS / Linux
    
    Returns
    ---------------
    String
        a defualt path to the hosts file depending on the users os
"""
def default_hosts_path() -> str:
    system = platform.system()
    if (system == "Windows"):
        return r"C:\Windows\System32\drivers\etc"
    else: # mac / linux
        return "/etc"
"""
    Allows the user to select a file on their pc to choose as their targeted
    hosts file

    Paramaters
    ---------------
    parent : String
        the parent ui window being targeted in the selection
    None : None
        If no parent ui exists, return none.
    
    Returns
    ---------------
    String
        the string representing the file path of the selected hosts file
    None
        Null in the case that there is no file selected
"""
def pick_hosts_file(parent=None) -> str | None:
    path, _ = QFileDialog.getOpenFileName(parent,"Select hosts file",default_hosts_path(),"All Files (*)")
    return path or None

"""
    Finds the resource path of the current root directory

    Paramaters
    ---------------
    rel : String
        the relative path of the current asset to be accessed
    
    Returns
    ---------------
    String
        A string that represents the current full resource path of the
        root directory + relative path to form the full resource path
"""
def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)

"""
    Flushes the DNS of the current user's operating system, ensuring instant operating system changes
    and immediate feedback upon blocking or canceling within the software
"""
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

"""
    Checks if the user is an admin, and if not, prompts them to give the software elevated permissions
"""
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
"""
    Gets the amount of time

    Paramaters
    ---------------
    duration : int
        the duration of blocktime to convert to minutes and hours
    
    Returns
    ---------------
    list
        a list of strings 'hourstr' and 'minutestr' describing the relative 
        hour and minute of a duration
"""
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

"""
    Writes the lines to the provided hosts file, beginning to block selected programs

    Paramaters
    ---------------
    filepath : String
        The path of the hosts file to open and write to
    block_string : String
        The string to write into the hosts file
"""
def block(filepath, block_string):
    print(f'blocking discord in filepath: {filepath}')
    with open(filepath, "a") as file:
        file.writelines(block_string);

"""
    Uses block tags to identify lines that should be skipped, to rewrite the hosts
    file without added changes

    Paramaters
    ---------------
    filepath : String
        The path of the hosts file to open and write to
"""
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
    """
    A class used to represent the main window of the App Blocker PySide6 GUI.
 
    The window lets a user select a set of sites/apps to block (by
    writing entries to the system's hosts file), choose a blocking
    duration (either a fixed duration or an end time), and start/cancel
    a timed blocking session. While a session is active, a progress bar
    and countdown label are shown and updated with a timer that ticks
    once per second.
 
    ...
 
    Attributes
    ----------
    duration : int
        The length of the current blocking session in seconds. Set via
        duration_edit_changed or end_time_edit_change.
    end_time : float
        The time.monotonic() timestamp at which the current blocking
        session should end. Set when blocking begins.
    block_timer : PySide6.QtCore.QTimer
        A one-second-interval timer used to update the progress bar and
        countdown label, and to detect when a blocking session has
        finished.
    cancel : bool
        Unused flag reserved for signaling a user-initiated cancellation.
    block_string : str
        The most recently built block of hosts file entries (see
        build_string), corresponding to whichever services are
        currently checked.
    blockOpts : dict of str -> str
        Maps each supported service key (e.g. 'twitter', 'discord')
        to the hosts file block_string that block that service.
    blockStatus : dict of str -> bool
        Maps each supported service key to whether the user has checked
        it for blocking.
    filepath : str
        The filesystem path to the hosts file that will be modified.
        Defaults to the platform's standard hosts path and can be
        changed via folder_clicked.
 
    Methods
    -------
    folder_clicked()
        Opens a file picker so the user can select a custom hosts file
        and validates the selection.
    build_string()
        Builds the combined hosts file block string from all
        currently checked services.
    discord_toggled()
        Syncs blockStatus['discord'] with the Discord checkbox state.
    twitter_toggled()
        Syncs blockStatus['twitter'] with the Twitter/X checkbox state.
    instagram_toggled()
        Syncs blockStatus['instagram'] with the Instagram checkbox state.
    youtube_toggled()
        Syncs blockStatus['youtube'] with the YouTube checkbox state.
    tiktok_toggled()
        Syncs blockStatus['tiktok'] with the TikTok checkbox state.
    facebook_toggled()
        Syncs blockStatus['facebook'] with the Facebook checkbox state.
    bsky_toggled()
        Syncs blockStatus['bsky'] with the Bluesky checkbox state.
    cancel_blocking_clicked()
        Ends the current blocking session early.
    on_block_tick(sound=None)
        Updates the progress bar/label each second and ends the session
        once time has elapsed.
    begin_blocking_clicked()
        Builds the block string, writes it to the hosts file, and starts
        the countdown timer.
    end_blocking()
        Stops the timer, restores the hosts file, flushes DNS, and
        resets the UI to its idle state.
    duration_edit_changed()
        Recomputes duration from the "duration" time-edit widget.
    seconds_until(qtime)
        Computes the number of seconds from now until a given time of
        day.
    end_time_edit_changed()
        Recomputes duration from the "end time" time-edit widget.
    closeEvent(event)
        Ensures blocking is cleanly ended if the window is closed while
        a session is active.
    """
    def __init__(self):
        """
        Initialize the main window.
 
        Loads the compiled UI, initializes blocking state (timer,
        duration,  options/status, and hosts file path), wires up 
        all widget signals to their handler methods, and sets the
        initial visibility/enabled state of window controls.
        """
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



        


"""
    Main method, checks for admin priviledge, grants it if not available, and blocks access
    starts timer, and ends block after sleep period.
"""
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

    with open(resource_path("appblocker.qss"), encoding="utf-8") as f:
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