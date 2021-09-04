import ctypes
import threading
from enum import Enum


class AlertIcon(Enum):
    NONE = 0x0
    ERROR = 0x10
    QUESTION = 0x20
    WARN = 0x30
    INFO = 0x40


class AlertButtons(Enum):
    OK = 0x0
    OKCANCEL = 0x1
    ABORTRETRYIGNORE = 0x2
    YESNOCANCEL = 0x3
    YESNO = 0x4
    RETRYCANCEL = 0x5
    CANCELTRYAGAINCONTINUE = 0x6


class Button(Enum):
    UNKNOWN = 0
    OK = 1
    CANCEL = 2
    ABORT = 3
    RETRY = 4
    IGNORE = 5
    YES = 6
    NO = 7
    TRYAGAIN = 10
    CONTINUE = 11


def alert(text: str, title: str = 'WinAlert', icon=AlertIcon.NONE, buttons=AlertButtons.OK, keep_on_top: bool = True,
          nonblocking: bool = False):
    flags = 0
    if not isinstance(icon, AlertIcon):
        raise Exception('icon должен представлять класс AlertIcon')
    flags |= icon.value
    if not isinstance(buttons, AlertButtons):
        raise Exception('buttons должен представлять класс AlertButtons')
    flags |= buttons.value
    if keep_on_top:
        flags |= 0x1000
    if nonblocking:
        threading.Thread(target=ctypes.windll.user32.MessageBoxExW, args=(None, text, title, flags)).start()
    else:
        ret = ctypes.windll.user32.MessageBoxExW(None, text, title, flags)
        btns = {
            1: Button.OK,
            2: Button.CANCEL,
            3: Button.ABORT,
            4: Button.RETRY,
            5: Button.IGNORE,
            6: Button.YES,
            7: Button.NO,
            10: Button.TRYAGAIN,
            11: Button.CONTINUE
        }
        return btns.get(ret, Button.UNKNOWN)


if __name__ == '__main__':
    alert('Удалить шындовс?', title='Вайрус!', icon=AlertIcon.QUESTION, buttons=AlertButtons.CANCELTRYAGAINCONTINUE,
          keep_on_top=True)
    print('aboba')
