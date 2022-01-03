import random
import urllib.request
import urllib.parse

def method_gethtml(targetaddress):
    useragents = ['Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)', 
               'Mozilla/5.0 (compatible; U; ABrowse 0.6;  Syllable) AppleWebKit/420+ (KHTML, like Gecko)', 
               'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)', 
               'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR   3.5.30729)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0;   Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;   SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)', 
               'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1;   .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)', 
               'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)', 
               'Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)', 
               'Mozilla/4.0 (compatible; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727); Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.2)', 
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)']
    useragents_index = random.randint(0,len(useragents)-1)
    useragent = useragents[useragents_index]
    #print(useragent)
    cookie = 'acw_tc=2760823516338607076621711ee440d018c1dd64893f40e30ae5162624d351; \
             Hm_lvt_f3c5c9ab40800b1142160abc4bba3ecb=1633856586,1633860707; \
             Hm_lpvt_f3c5c9ab40800b1142160abc4bba3ecb=1633860707'
    headers = {'User-Agent': useragent,
               'Connection': 'keep-alive',
               'Cookie': cookie}  
    url = urllib.request.Request(targetaddress,headers)
    page_content = urllib.request.urlopen(url).read()
    # page_content = pageContent.decode('UTF-8')
    return page_content

target_address = 'https://js.51jobcdn.com/in/resource/js/2021/search/index.107a3edc.js'
source_code = method_gethtml(target_address)

print(source_code)