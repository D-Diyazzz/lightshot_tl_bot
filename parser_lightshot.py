
from bs4 import BeautifulSoup
import requests as req
import random
from urllib import request as ulreq
from PIL import ImageFile

def getsizes(uri):
    # get file size *and* image size (None if not known)
    print("form getsize")
    file = ulreq.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    print("from getsize2")
    return size, None


# Send picture
def pic_dow(hashcode):
    hashcode = ''.join(hashcode)

    src = "https://prnt.sc/"+hashcode

    resp = req.get(src, headers={'User-Agent': 'Chrome'})

    soup = BeautifulSoup(resp.text, 'lxml')
    imgs = soup.find_all("img", class_="no-click screenshot-image")

    for img in imgs:
        link = img.get("src")
        print(link)
        if link[0:2] == '//':
            return rand_hashcode()
        print(link)
        try:
            size_image = getsizes(link)
            if size_image == (503, (161, 81)):
                return rand_hashcode()
            return link
        except:
            return link
  

# Create hashcode
def rand_hashcode():
    hashcode = []
    for i in range(6):
        n_or_l = random.randrange(0, 2)
        print(n_or_l)
        if n_or_l == 0:
            n = random.randrange(0, 10)
            hashcode.append(str(n))
        else:         
            n = random.randrange(97, 123)
            hashcode.append(chr(n))
    print(hashcode)
    return pic_dow(hashcode)




if __name__ == '__main__':
    rand_hashcode()
