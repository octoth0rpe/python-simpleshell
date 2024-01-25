import os
from datetime import datetime

def ls():
    items = os.listdir()
    results = []
    for item in items:
        stats = os.stat(item)
        results.append({
            "name": item,
            "size": stats.st_size,
            "uid": stats.st_uid,
            "gid": stats.st_gid,
            "created": datetime.fromtimestamp(stats.st_ctime),
            "raw_mode": stats.st_mode,
            "mode": '{:o}'.format(stats.st_mode)[-3:],
        })
    return results

def pwd():
    return os.getcwd()

def cd(new_dir: str):
    os.chdir(os.path.expanduser(new_dir))

def cat(filename: str):
    with open(filename, "r") as f:
        return f.read()
