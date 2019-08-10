import threading
import wget
import time
import os

from urllib.error import HTTPError, ContentTooShortError
from requests_html import HTMLSession

session = HTMLSession()

#图片存放根目录
dir = '/Users/daipeng/workspace_py/spider_learning/HibobiSpider/images'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'If-None-Match':'2956f-vhiJpxuswrT6Vh8uEDrdbuJ7d2s',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

params = {'lang':'en','country':'SA'}
cookies = {'_ga':'GA1.2.773192687.1565097423', '_gid':'GA1.2.1019465888.1565097423', '_fbp':'fb.1.1565097424674.1988162091', 'country':'SA', 'cookieCoutry':'SA0AE0', 'isDefaultCountry':'ok', 'threshold':'370.00', 'currencyCode':'SAR', 'fare':'75.00', 'lang':'en', 'currencySymbol':'SAR', 'HasCates':'en'}

#商品分类和页数mapping
category_map_pagesize = {'Baby Boy':38, 'Baby Girl':57, 'Toddler Boy':33, 'Toddler Girl':61, 'Boy':5, 'Girl':14, 'Shoes':11, 'Accessories':12}

#商品分类和链接mapping
category_map_link = {
    'Baby Boy':'https://www.hibobi.com/categories/Baby-Boy-65-front.html?cate=65-front&spm=1000.1100.0.0&lang=en&country=SA',
    'Baby Girl':'https://www.hibobi.com/categories/Baby-Girl-64-front.html?cate=64-front&spm=1001.2001.64-front.1&lang=en&country=SA',
    'Toddler Boy':'https://www.hibobi.com/categories/Toddler-Boy-84-front.html?cate=84-front&spm=1001.2001.64-front.2&lang=en&country=SA',
    'Toddler Girl':'https://www.hibobi.com/categories/Toddler-Girl-83-front.html?cate=83-front&spm=1001.2001.84-front.3&lang=en&country=SA',
    'Boy':'https://www.hibobi.com/categories/Boy-86-front.html?cate=86-front&spm=1001.2001.83-front.4&lang=en&country=SA',
    'Girl':'https://www.hibobi.com/categories/Girl-85-front.html?cate=85-front&spm=1001.2001.86-front.5&lang=en&country=SA',
    'Shoes':'https://www.hibobi.com/categories/Shoes-128-front.html?cate=128-front&spm=1001.2001.85-front.6&lang=en&country=SA',
    'Accessories':'https://www.hibobi.com/categories/Accessories-141-front.html?cate=141-front&spm=1001.2001.128-front.7&lang=en&country=SA'
}

# 多线程配置信息
#threadLock = threading.Lock()
threads = []

# 下载图片操作
def downloadImage(img_name_map_full_url, dir):
    for img_name, full_img_url in img_name_map_full_url.items():
        #threadLock.acquire()
        download(full_img_url, dir + img_name)
        #threadLock.release()

def download(url, out):
    time.sleep(0.2)
    try:
        wget.download(url, out)
    except (HTTPError, ContentTooShortError) as e:
        print("download image error, reason: " + e.reason + "\n" + "download params url: " + url + " out: " + out)
        download(url, out)

for category, category_link in category_map_link.items():
    # 判断图片存储目录
    path = dir + "/" + category
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)

    page_size = category_map_pagesize[category]
    for page in range(1, page_size):
        r = session.get(category_link + "&page=" + str(page), headers=headers, cookies=cookies)

        # 图片名称和图片地址mapping
        img_name_map_full_url = {}

        # 图片名称和单品页地址mapping
        img_name_map_good_link= {}

        # goods list <li> elements
        goods_list = r.html.find('.goods-list li')
        for good in goods_list:
            full_img_url = good.find('a span img')[0].attrs['src']
            img_url = full_img_url[0:full_img_url.rindex('?')]
            img_name = img_url[img_url.rindex('/'):]
            img_name_map_full_url[img_name] = full_img_url

            good_link = "https://www.hibobi.com" + good.find('a')[0].attrs['href']
            img_name_map_good_link[img_name] = good_link

        t = threading.Thread(target=downloadImage, name='download-image-%s' % category + str(page), args=(img_name_map_full_url, path))
        threads.append(t)
        t.start()

        print("-恭喜你" + category + "分类下商品图片第：" + str(page) + "页下载完成")
    print("--恭喜你" + category + "分类下所有商品图片下载完成，页数：" + str(page_size))


# 等待所有线程完成
for t in threads:
    t.join()
print ("---恭喜你所有图片下载完成, 退出主线程...")


