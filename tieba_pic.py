import urllib.request
import re
import os
import random

def url_open(url):
    # 访问，获取html
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_img(html):
    pic = r'<img class="BDE_Image" src="([^"]+\.jpg)'
    imglist = re.findall(pic, html)
    for each in imglist:
        print(each)
    return imglist

def save_img(folder, imglist):


    for each in imglist:
        filename = each.split("/")[-1]
        #urllib.request.urlretrieve(each, filename, None)
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def get_pic(url):
    # get page
    html = url_open(url).decode('utf-8')
    #print(html)

    pageID = r'<a rel="noreferrer" href="/p/([^"]+)" '
    pagelist = re.findall(pageID, html)
    #print(pagelist)

    # 创建文件夹
    folder = input("输入文件夹名：")
    #print(folder)
    os.mkdir(folder)
    os.chdir(folder)

    for each in pagelist:
        # print(each)
        page = 'http://tieba.baidu.com/p/' + each
        print(page)
        pagehtml = url_open(page).decode('utf-8')
        #print(pagehtml)

        imglist = get_img(pagehtml)
        save_img(folder, imglist)

    html = url_open(url)
    get_img(html)
    imglist = get_img(html)
    save_img(imglist)

if __name__ == '__main__':
    # 代理
    #iplist = ['125.123.142.150:9999', '121.61.1.47:9999', '61.150.113.27:8908', '111.177.183.181:9999']
    #proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
    #opener = urllib.request.build_opener(proxy_support)
   # urllib.request.install_opener(opener)
    url = "https://tieba.baidu.com/f?kw=p%D5%BE&fr=ala0&tpl=5"
    get_pic(url)
