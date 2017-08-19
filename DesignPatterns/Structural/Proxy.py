"""
Proxy!

Problem
	* Postpone object creation unless absolutely necessary
	* Find a placeholder
"""
import time


class Worker(object):
    """docstring for Producer"""

    def working(self):
        print('Worker is not available')

    def newWork(self):
        print('Worker is waiting for new job')


class Proxy(object):
    """docstring for Proxy"""

    def __init__(self):
        self.ocupied = 'No'
        self.worker = None

    def work(self):
        """CHECK IF WORKER IS AVAILABLE"""
        print('Checking if worker is available')
        if self.ocupied == 'No':
            self.worker = Worker()
            time.sleep(2)
            self.ocupied = 'Yes'
            self.worker.newWork()

        else:
            time.sleep(2)
            print("Worker is Busy")

p = Proxy()
p.work()
p.work()
