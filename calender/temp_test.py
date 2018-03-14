import time
i=1
print('准备进入while')
try:
    time.sleep(2)
    print('现在进入了while')
    time.sleep(2)
    m = 10
    time.sleep(2)
    print('准备进入for')
    time.sleep(2)

    for x in range(m):
        time.sleep(2)
        print('进入for')
        time.sleep(2)
        print('m = ',x)
        time.sleep(2)
        print('准备进入if')
        time.sleep(2)
        if x == 5:
            print('now in for')
            time.sleep(2)
            print('i将被设为0')
            raise Exception
            print('i被设为0')

        else:
            print('wait to goto for')
except Exception:
            print('已经发送，停止主程序')