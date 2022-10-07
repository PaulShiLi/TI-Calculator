import sys


class platform:
    platforms = {
        "linux": "Linux",
        "linux2": "Linux",
        "win32": "Windows",
        "cygwin": "Cygwin",
        "msys": "MSYS2",
        "darwin": "MacOS",
        "os2": "OS 2",
        "os2emx": "OS 2 EMX"
    }

    def __init__(self):
        self.platform = str(sys.platform)
        self.platformCheck()

    def platformCheck(self):
        try:
            self.os = self.platforms[self.platform]
        except KeyError:
            print("Platform not supported!")
            exit()
