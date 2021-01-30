# revise by JLZ
from threading import Thread
from time import time
import datetime
import os
from ftplib import FTP
global localpath,ifisd
ifisd="isd-lite/"
localpath="/shares/Public2/NOAA/"+ifisd


class MyFTP(FTP):
    def getSubdir(self, *args):
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
        if dirname != None:
            self.cwd(dirname)
        files = self.getSubdir()

        r_files = [file.split(" ")[-1] for file in files]

        return [file for file in r_files if file != "." and file !=".."]

    def getfiles(self, dirname=None):
        if dirname != None:
            self.cwd(dirname) 
        return self.nlst()  

   
def test():
    ftp = MyFTP() 
    ftp.connect("ftp.ncdc.noaa.gov", 21)  
    ftp.login("anonymous", "guest") 


    fnames=[]
    j=1901
 #   while j< 1962:
    while j< 2021:
        ftp.cwd("/pub/data/noaa/isd-lite/"+str(j))
        lst=ftp.getdirs()
        cmds="mkdir -p /shares/Public2/NOAA/isd-lite/"+str(j)
        os.system(cmds)
        for name in lst:
            localname="/shares/Public2/NOAA/isd-lite/"+str(j)+"/"+name
            if((os.path.isfile(localname)) or (os.path.isfile(localname[:-3]))):
                print(localname+" Exist!")
            else:
#            fnames.append(str(name)
                print(localname+" None")
                cmds=" wget -Nc --ftp-user=anonymous --ftp-password=guest ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/"+str(j)+"/"+name \
                +" -P "+localpath+str(j)+"/"
                print(cmds)
                os.system(cmds)
        j=j+1

    ftp.quit()
   
       
if __name__ == '__main__':
    test()
