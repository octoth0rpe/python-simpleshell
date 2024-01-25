from datetime import datetime


class File:
    def __init__(self, path: str, name: str, stats):
        self.path = path
        self.name = name
        self.size = stats.st_size
        self.uid = stats.st_uid
        self.gid = stats.st_gid
        self.ctime = datetime.fromtimestamp(stats.st_ctime)
        self.raw_mode: stats.st_mode
        self.mode = "{:o}".format(stats.st_mode)[-3:]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def cat(self) -> str:
        with open(f"{self.path}/{self.name}", "r") as f:
            return f.read()
