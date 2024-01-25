from .sh import ls, pwd, cd, touch, cat


def register_global(glob):
    glob["ls"] = ls
    glob["pwd"] = pwd
    glob["cd"] = cd
    glob["touch"] = touch
    glob["cat"] = cat
