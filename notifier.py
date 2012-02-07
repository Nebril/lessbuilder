#!/usr/bin/python
import pyinotify
import commands
import os

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        result = commands.getstatusoutput('/home/nebril/node_modules/less/bin/lessc ' + event.pathname + ' ../' + event.path[:-4] + 'css');
        if(result[0] == 0) :
            print 'compile successful'
        else :
            print result[1]

def main():
    fileList = os.listdir(os.getcwd())


    wm = pyinotify.WatchManager()
    for fname in fileList :
        if(fname[-4:] == 'less'):
            wm.add_watch(fname, pyinotify.IN_MODIFY, rec=True)


    eh = MyEventHandler()

    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()