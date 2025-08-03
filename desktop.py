import ctypes
from screeninfo import get_monitors

# https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
# https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow

# 
SPI_SETDESKWALLPAPER = 0x0014
SPI_GETDESKWALLPAPER = 0x0073

def test1():
    path = ctypes.create_unicode_buffer(1024)
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, ctypes.sizeof(path), path, 0)
    print(result, path.value)

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\vsreeniv\Pictures\s.jpg", 0)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\vsreeniv\Pictures\1.jpg", 0)


def set_wallpaper(filelocation, check_and_set = False):
    path = ctypes.create_unicode_buffer(1024)
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, ctypes.sizeof(path), path, 0)
    if result != 1 :
        return
    if check_and_set:
        if path.value == filelocation:
            print("Already using the same file as desktop")
            return
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filelocation, 0)

def get_primary_monitor_resoution():
    for m in get_monitors():
        if m.is_primary:
            return (m.width,m.height)
    return None

if __name__ == "__main__":
    wp1 = r"C:\Users\vsreeniv\Pictures\1.jpg"
    wp2 = r"C:\Users\vsreeniv\Pictures\s.jpg"
    set_wallpaper(wp2)
    print(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
