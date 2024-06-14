from ctypes import c_int64

import click
import time


def get_progress_bar(action, file, length):
    bar = click.progressbar(label='{} "{}"'.format(action, file), length=length)
    last_current = c_int64(0)

    def progress(current, total):
        if current < last_current.value:
            return
        bar.pos = 0
        bar.update(current)
        last_current.value = current
        if length < 525292800:
            time.sleep(.21)
        elif length < 1025292800:
            time.sleep(.23)
        elif length < 1525292800:
            time.sleep(.25)
        else:
            time.sleep(.3)
    return progress, bar
