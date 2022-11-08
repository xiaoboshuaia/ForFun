'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-11-08 13:39:03
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-11-08 15:46:20
FilePath: \Project\OTTM\html\translate_webp_to_JPG.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
将webp的图片格式转化为JPG格式


'''

from PIL import Image
with open(r'xiaogong.webp', 'rb') as f:
    img = Image.open(f)
    img.load()
    img.save(r'xiaogong.jpg', 'JPEG')
    
# 本质就是通过从jpg文件中读取的坐标信息保存为svg所需要的格式
def toSVG(infile, outfile):
    image = Image.open(infile).convert('RGBA')
    data = image.load()
    width, height = image.size
    out = open(outfile, "w")
    out.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    out.write('<svg id="svg2" xmlns="http://www.w3.org/2000/svg" version="1.1" \
                width="%(x)i" height="%(y)i" viewBox="0 0 %(x)i %(y)i">\n' % \
                {'x': width, 'y': height})
    
    for y in range(height):
        for x in range(width):
            rgba = data[x, y]
            rgb = '#%02x%02x%02x' % rgba[:3]
            if rgba[3] > 0:
                out.write('<rect width="1" height="1" x="%i" y="%i" fill="%s" \
                    fill-opacity="%.2f" />\n' % (x, y, rgb, rgba[3]/255.0))
    out.write('</svg>\n')
    out.close()
    
toSVG('xiaogong.jpg', 'xiaogong.svg')











