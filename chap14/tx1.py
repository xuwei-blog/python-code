'''import sys
print(sys.getsizeof(28))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
'''

import schedule
import time
def job():
    print('哈哈哈哈哈哈哈')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)