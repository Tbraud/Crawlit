import os
class ConfigFile:

    def __init__(self,filename):
        self.filedesc=open(filename,"r")
        self.parseconfig()

    def parseconfig(self):
        counter=0
        for line in self.filedesc:
            counter+=1
            line2=line.split()
            if line2[0]=="path:" and len(line2)==2:
                self.path=os.path.expanduser(line2[1])
                print self.path
            elif line2[0]=="subreddits:":
                self.redlist=line2[1:]
            elif line2[0]=="client_id:" and len(line2)==2:
                self.client_id=line2[1]
