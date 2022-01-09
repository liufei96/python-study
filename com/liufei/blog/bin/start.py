import sys
import os

# D:/git_project/python-study/com/liufei/blog/bin
print(os.path.dirname(__file__))
# D:/git_project/python-study/com/liufei/blog
print(os.path.dirname(os.path.dirname(__file__)))

BATH_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BATH_DIR)

from core.src import run

if __name__ == '__main__':
    run()
