import threading
import wget

from requests_html import HTMLSession

session = HTMLSession()

dir = '/Users/daipeng/workspace_py/spider_learning/HibobiSpider/images'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'If-None-Match':'2956f-vhiJpxuswrT6Vh8uEDrdbuJ7d2s',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

params = {'lang':'en','country':'SA'}

cookies = {'_ga':'GA1.2.773192687.1565097423', '_gid':'GA1.2.1019465888.1565097423', '_fbp':'fb.1.1565097424674.1988162091', 'country':'SA', 'cookieCoutry':'SA0AE0', 'isDefaultCountry':'ok', 'threshold':'370.00', 'currencyCode':'SAR', 'fare':'75.00', 'lang':'en', 'currencySymbol':'SAR', 'HasCates':'en'}

r = session.get('https://www.hibobi.com/categories/Baby-Boy-65-front.html?cate=65-front&spm=1001.2001.65-front.0&lang=en&country=SA', headers=headers, cookies=cookies)

img_size = len(r.html.find('.goods-list li a span img'))
img_name_list = []
for img in r.html.find('.goods-list li a span img'):
    full_img_url = img.attrs['src']
    img_url = full_img_url[0:full_img_url.rindex('?')]
    img_name = img_url[img_url.rindex('/'):]
    img_name_list.append(img_name)
    wget.download(dir + img_name, img_name)

'''
def downloadImage(img_name_list):
    for img_name in img_name_list:
        threading.Lock().acquire()
        wget.download(dir + img_name, img_name)
        threading.Lock().release()

for i in range(1, 5):
    t = threading.Thread(target=downloadImage, name='Download-Thread %s' % i, args=(img_name_list,))
    t.start()
'''
