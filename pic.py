from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from find_system_fonts_filename import get_system_fonts_filename, FindSystemFontsFilenameException
import os
import io
import logging as lg
import font

def get_font():
    f = bytes.fromhex(font.font)
    return io.BytesIO(f)

def t1():
    wp2 = r"C:\Users\vsreeniv\Pictures\s.jpg"
    img = Image.open(wp2)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    ##font = ImageFont.truetype("sans-serif.ttf", 16)
    font = ImageFont.truetype("rsw.ttf", 16)
    # draw.text((x, y),"Sample Text",(r,g,b))
    ##draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    img.save('sample-out.jpg')
    fonts_filename = get_system_fonts_filename()
    print(fonts_filename)


def get_modified_filename(oimgfn, prefix = None):
    pfx = prefix if prefix else "n_"
    d = os.path.dirname(oimgfn)
    f = os.path.basename(oimgfn)
    fl1 = f.split(".")
    ext = fl1[-1]
    b = fl1[0:-1]
    if ext != "jpg" and ext != "png":
        lg.error("invalid image extension for " + repr(oimgfn))
        raise Exception("invalid image extension for " + repr(oimgfn))
    nf = os.path.join(d, pfx + "".join(b) + "." + ext)
    lg.debug("new path = ", repr(nf))
    return nf

def update_file_with_text(oimgfn, i):
    oimg = Image.open(oimgfn)
    draw = ImageDraw.Draw(oimg)
    txtloc_height = oimg.height
    txtloc_width = oimg.width
    font_size = 18
    text_line_len = 150
    text_x_loc  = 300
    text_y_off_from_bottom = 150
    expl = [i["explanation"][j:j + text_line_len] for j in range(0,len(i["explanation"]), text_line_len)]

    f = get_font()
    font = ImageFont.truetype(f, font_size)
    pxlfrmbottom = text_y_off_from_bottom + len(expl) * (font_size + 2)
    diff = font_size + 5
    for e in expl:
        draw.text((text_x_loc, txtloc_height - pxlfrmbottom), e, (255,255,255), font=font)
        pxlfrmbottom -= diff

#    draw.text((0,0),i["explanation"],(255,255,255),font=font)
    mfn = get_modified_filename(oimgfn)
    oimg.save(mfn)
    return mfn

def update_resolution(imgfn, resolution):
    if not resolution:
        return
    img = Image.open(imgfn)
    rimg = img.resize(resolution)
    mfn = get_modified_filename(imgfn, "r_")
    rimg.save(mfn)
    return mfn

def t3():
    ofn = r"tmpdir\2.jpg"
    resolution = (3480,2160)
    update_resolution(ofn, resolution)

def t2():
    ofn = r"tmpdir\1.jpg"
    mfn = get_modified_filename(ofn)
    print(mfn)

if __name__ == "__main__":
#    t1()
#    t2()
    t3()

