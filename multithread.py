
import threading
import time

def _func(id):
	print(threading.currentThread().getName())
	print('ID:',id)

t1 = threading.Thread(name = 'func1', target = _func, args = (1,))
t2 = threading.Thread(name = 'func2', target = _func, args = (2,))
t3 = threading.Thread(name = 'func3', target = _func, args = (3,))

t1.start()
t2.start()
t3.start()