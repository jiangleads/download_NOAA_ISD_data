# revise by JLZ
from queue import Queue
from threading import Thread
from time import time
import datetime
import os
from ftplib import FTP
import subprocess

class MyFTP(FTP):
    encoding = "gbk"  # 默认编码
    def getSubdir(self, *args):
        '''拷贝了 nlst() 和 dir() 代码修改，返回详细信息而不打印'''
        cmd = 'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            cmd = cmd + (' ' + arg)
        files = []
        self.retrlines(cmd, files.append)
        return files

    def getdirs(self, dirname=None):
        """返回目录列表，包括文件简要信息"""
        if dirname != None:
            self.cwd(dirname)
        files = self.getSubdir()

        # 处理返回结果，只需要目录名称
        r_files = [file.split(" ")[-1] for file in files]

        # 去除. .. 
        return [file for file in r_files if file != "." and file !=".."]

    def getfiles(self, dirname=None):
        """返回文件列表，简要信息"""
        if dirname != None:
            self.cwd(dirname)  # 设置FTP当前操作的路径
        return self.nlst()  # 获取目录下的文件 

class DownloadWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue
 
   def run(self):
       while True:
           # 从队列中获取任务并扩展tuple
           cmds = self.queue.get()
#           print(cmds)
           output=os.popen(cmds)
           print(str(output.read())+"  "+cmds)
           self.queue.task_done()


   
def test():
    file = open('download.sh','r')
    fnames = file.readlines()
    file.close()
#    print(fnames)  
       
        #创建一个主进程与工作进程通信
    queue = Queue()
   
   
    #创建4个工作线程
    for x in range(30):
        worker = DownloadWorker(queue)
        #将daemon设置为True将会使主线程退出，即使所有worker都阻塞了
        worker.daemon = True
        worker.start()
       
    #将任务以tuple的形式放入队列中
    for link in fnames:
        queue.put((link))
   
    #让主线程等待队列完成所有的任务
    queue.join()
       
        
       
if __name__ == '__main__':
    test()
