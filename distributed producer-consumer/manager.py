# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:21:06 2020

@author: Sina
"""

from multiprocessing.managers import BaseManager, SyncManager
from queue import Queue
import time

class QueueManager(BaseManager):
    def __init__(self,port,length):
        super().__init__(address=('localhost',port),authkey=b'mymanager')
        self.queue = Queue(maxsize=length)
        self.register('queue',callable=lambda:self.queue)

    
manager = QueueManager(50020,10)
server = manager.get_server()
server.serve_forever()


