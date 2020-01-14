# screen.py
from ..reader import * # reader 패키지의 모든 모듈
def write():
    print('barcode screen:', barcode.data)
    print('qrcode screen:', qrcode.data)