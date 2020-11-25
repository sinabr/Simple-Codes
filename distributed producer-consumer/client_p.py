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

def producer(i):

    a = random.randint(1,4)

    data = [1,3,5,7,8,3,5,7]


    i = 0
    while i < len(data) :
        q = manager.queue()
        print('P - {} Produced {}'.format(i,data[i]))
        q.put(data[i])
        time.sleep(a)
        i += 1


a = Thread(target=producer,args=[1])
b = Thread(target=producer,args=[2])
c = Thread(target=producer,args=[3])

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()

q = manager.queue()

q.put(-1)
q.put(-1)
q.put(-1)

manager.shutdown()

print('producers done')