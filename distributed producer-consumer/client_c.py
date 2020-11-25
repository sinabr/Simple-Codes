# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:21:06 2020

@author: Sina
"""

from multiprocessing.managers import BaseManager, SyncManager
import random        
import time
from threading import Thread

BaseManager.register('queue')

manager = BaseManager(address=('localhost',50020),authkey=b'mymanager')
manager.connect()

def consumer(i):

    t = random.randint(1,3)

    while True :
        q = manager.queue()
        element = q.get()
        if element == -1 or  element == '-1':
            print('C - {} Terminated'.format(i))
            break
        else:
            print('C - {} Used {}'.format(i,element))
        time.sleep(t)

a = Thread(target=consumer,args=[1])
b = Thread(target=consumer,args=[2])
c = Thread(target=consumer,args=[3])

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()

print("consumers done")