import os
import glob
from posixpath import splitext
import time
import colorama
from colorama import Back, Fore
import filetype


colorama.init(autoreset=True)


class Main:
    def __init__(self) -> None:
        self.files = 0
        self.directories = 0
        self.result: dict = dict(
            audio=dict(count=0, files=[]),
            image=dict(count=0, files=[]),
            video=dict(count=0, files=[]),
        )
        self.__extension = {
            "audio": [".mp3", ".opus"],
            "video": [".mp4", ".mkv"],
            "image": [".png", ".jpg", ".jpeg"],
        }
        self.allowed_type = ["audio", "image", "video"]

    def wrap(self, text: str) -> str:
        width = os.get_terminal_size().columns // 2
        if width < len(text):
            text = text[: width - 4] + "..." + text[-width:]
        return text

    def info(self, text: str, color: str = Back.BLUE) -> str:
        return f"{color} {Fore.BLACK}INFO{Fore.RESET} {Back.RESET} {text}"

    def __set_value(self, type: str, value: dict):
        self.result[type]["count"] += value["count"]
        self.result[type]["files"].append(value["files"])

    def check(self, path: str, mime: str = None) -> bool:
        if os.path.isdir(path):
            listfile = glob.glob(path + "/*")
            if len(listfile) != 0:
                for item in listfile:
                    if os.path.isdir(item):
                        print(self.wrap("➜ " + item), end="\r")
                        self.directories += 1
                        time.sleep(0.005)
                        self.check(item, mime=mime)
                    if os.path.isfile(item):
                        if mime == "video" and filetype.is_video(item):
                            extension = os.path.splitext(item)[1].lower()
                            if extension in self.__extension["video"]:
                                self.__set_value(
                                    "video", value={"count": 1, "files": item}
                                )
                        if mime == "audio" and filetype.is_audio(item):
                            extension = os.path.splitext(item)[1].lower()
                            if extension in self.__extension["audio"]:
                                self.__set_value(
                                    "audio", value={"count": 1, "files": item}
                                )
                        if mime == "image" and filetype.is_image(item):
                            extension = os.path.splitext(item)[1].lower()
                            if extension in self.__extension["image"]:
                                self.__set_value(
                                    "image", value={"count": 1, "files": item}
                                )
                        print(end="")
                        print(self.wrap(item))
                        self.files += 1
            return True
        else:
            return False
