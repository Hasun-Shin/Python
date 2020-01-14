# print.py
from ..reader import * # reader 패키지의 모든 모듈
def write():
    print('barcode print:', barcode.data)
    print('qrcode print:', qrcode.data)