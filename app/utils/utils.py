def str2bool(s, default=False):
    try:
        return bool(s)
    except Exception:
        return default


def str2int(s, default=0):
    try:
        return int(s)
    except Exception:
        return default


def str2float(s, default=0):
    try:
        return float(s)
    except Exception:
        return default