#! /usr/bin/python3
#yum.iqianyue.com/proxy
import urllib.request

def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data

proxy_addr = "125.72.106.240:808"
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))