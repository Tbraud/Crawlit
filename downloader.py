import os
import urllib

class Downloader:

    def __init__(self,folder,linklist):
        self.folder_path=os.path.abspath(folder)
        self.linklist=linklist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def get_pics(self):
        for link in self.linklist:
            basename=os.path.basename(link)
            fullpath=os.path.join(self.folder_path,basename)
            if not os.path.exists(fullpath):
                try:
                    urllib.urlretrieve(link,fullpath)
                    print "Downloading "+link
                except:
                    pass
