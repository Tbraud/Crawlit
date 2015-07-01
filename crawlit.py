import conf
import reddit
import downloader
import time
import os

conf=conf.ConfigFile("config")

client_id=conf.client_id
redlist=conf.redlist
path=conf.path

while 1:
    for redname in redlist: 
        red=reddit.Reddit(client_id,redname)
        linklist=red.get_gallery()
        down=downloader.Downloader(os.path.join(path,redname),linklist)
        down.get_pics()
        time.sleep(10)
    time.sleep(600)
