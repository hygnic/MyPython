# User: hygnic
# Date: 2018/9/12
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src import service

if __name__ == '__main__':
    service.main()
