import reddit
import downloader
import time
client_id="9a89a3ff03efeb8"
redlist=["EarthPorn","CityPorn","SpacePorn"]

while 1:
    #access_token=au.refresh_to_token()
    for redname in redlist: 
        red=reddit.Reddit(client_id,redname)
        linklist=red.get_gallery()
        down=downloader.Downloader("Pics/"+redname,linklist)
        down.get_pics()
        time.sleep(10)
    time.sleep(600)
