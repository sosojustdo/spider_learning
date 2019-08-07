from requests_html import HTMLSession

session = HTMLSession()
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'If-None-Match':'29632-HdsOkod2dfzIA9ATU2MHcyPI7yY',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

params = {'lang':'en','country':'SA'}

cookies = {'_ga':'GA1.2.773192687.1565097423', '_gid':'GA1.2.1019465888.1565097423', '_fbp':'fb.1.1565097424674.1988162091', 'country':'SA', 'cookieCoutry':'SA0AE0', 'isDefaultCountry':'ok', 'threshold':'370.00', 'currencyCode':'SAR', 'fare':'75.00', 'lang':'en', 'currencySymbol':'SAR', 'HasCates':'en'}

#proxies = {'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'}#代理ip字典，随机调用

r = session.get('http://www.hibobi.com/categories/Baby-Boy-65-front.html', headers=headers, cookies=cookies)

print(r.text)