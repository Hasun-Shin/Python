from ..reader import * # reader 패키지의 모든 모듈
def write():
    file1 = open('barcode.txt', 'w')
    file1.write('barcode data : %s' % barcode.data)
    file2 = open('qrcode.txt', 'w')
    file2.write('qrcode data : %s' % qrcode.data)
    file1.close()
    file2.close()
