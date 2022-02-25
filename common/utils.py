"""File holding general purpose functions."""
import time


def normalize_time(seconds: int):
    """Turns seconds into H:M:S"""
    if seconds < 3600:
        return time.strftime("%M:%S", time.gmtime(seconds))
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
