import os
import fnmatch

from .file import File


def _resolve_path(path: str) -> str:
    if path[0] == "/":
        return path
    return os.path.expanduser(os.getcwd() + "/" + path)


def ls(*args, **kwargs) -> list[File]:
    """List files and directories in the current working directory."""
    pwd = os.getcwd()
    items = os.listdir()
    results = []
    filter_ = args[0] if len(args) > 0 else None
    for item in items:
        if filter_ and not fnmatch.fnmatch(item, filter_):
            continue
        stats = os.stat(item)
        results.append(File(pwd, item, os.stat(item)))
    return sorted(results, key=lambda x: x.name)


def pwd() -> str:
    """Get the current working directory."""
    return os.getcwd()


def cd(new_dir: str) -> str:
    """Change the current working directory."""
    new_path = _resolve_path(new_dir)
    os.chdir(new_path)
    return new_path


def mv(file: File | str, destination: str):
    """Move a file or directory."""
    # destination is a directory that we're moving the file to
    if os.path.isdir(destination):
        pass
    # destination is NOT a dir, so this is a rename
    pass


def touch(path: str) -> bool:
    """Touch a file or dir, returns True if a file is created."""
    full_path = _resolve_path(path)
    file_created = not os.path.exists(full_path)
    with open(full_path, "a"):
        os.utime(full_path)
    return file_created


def cat(filename: str) -> str:
    """Cat a file."""
    with open(filename, "r") as f:
        return f.read()
