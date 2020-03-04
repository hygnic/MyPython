# User: hygnic
# Date: 2018/9/12
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIND_HOST = '127.0.0.1'
PORT = 8080

USER_HOME = os.path.join(BASE_DIR, 'home')

USER_ACCOUNT = {
    'alex': {
        'password': 'alex123',
        'quotation': 1000000,
        'expire': '2016-01-22',
    }
}