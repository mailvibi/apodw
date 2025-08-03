import nasa
import sys
import os
import logging as lg
import pic
import desktop

def get_download_dir():
    DIR_LOC="tmpdir"
    if not os.path.exists(DIR_LOC):
        os.mkdir(DIR_LOC)
    return DIR_LOC

def get_file_save_name(imgname):
    fn = imgname
    d = get_download_dir()
    fn = os.path.join(d, fn)
    fn = os.path.abspath(fn)
    return fn

def save_file(apod_img_info):
    fn = get_file_save_name(i["imgname"])
    with open(fn, "wb") as f:
        f.write(apod_img_info["image"])
    return fn

if __name__ == "__main__":
    i = nasa.get_apod()
    monitor_resolution = desktop.get_primary_monitor_resoution()
    ofn = save_file(i)
    print(ofn)
    mfn = pic.update_resolution(ofn, monitor_resolution)
    mfn = pic.update_file_with_text(mfn, i)
    print(mfn)
    print(i["explanation"])
    desktop.set_wallpaper(mfn)
#    mfn = update_file_with_text(ofn, i)
