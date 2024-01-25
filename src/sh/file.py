from datetime import datetime
import json


class File:
    def __init__(self, path: str, name: str, stats):
        self.path = path
        self.name = name
        self.size = stats.st_size
        self.uid = stats.st_uid
        self.gid = stats.st_gid
        self.ctime = datetime.fromtimestamp(stats.st_ctime)
        self.raw_mode: stats.st_mode

    @property
    def mode(self):
        return "{:o}".format(self.raw_mode)[-3:]

    @property
    def full_path(self) -> str:
        return f"{self.path}/{self.name}"

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def cat(self) -> str:
        with open(self.full_path, "r") as f:
            return f.read()

    def lines(self) -> list[str]:
        """Return lines in file, split on newline"""
        with open(self.full_path, "r") as f:
            return f.readlines()

    def json(self):
        """Load json from file"""
        return json.loads(self.cat())
