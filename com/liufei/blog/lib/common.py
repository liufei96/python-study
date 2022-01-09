
from core import src

def auth(func):
    def inner(*args, **kwargs):
        if src.status_dic['status']:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('\033[1;31;0m 请先进行登录 \033[0m')
            if src.login():
                ret = func(*args, **kwargs)
                return ret

    return inner