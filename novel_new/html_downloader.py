#coding:UTF8
'''
@author: linsen
'''

import urllib2,file_handle


class HtmlDownloader(object):
    def __init__(self):
        self.filelogs = file_handle.FileHandle()
    
    def download(self, url):
        if url is None:
            return None
        
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0','Referer' : url}
        request = urllib2.Request(url,None,headers)
        self.filelogs.writeLogs(str(url))
        try:
            response = urllib2.urlopen(request,timeout=30)   #2.7
#             response = urllib.urlopen(url)   #3
        except urllib2.HTTPError,e:    #HTTPError必须排在URLError的前面
            self.filelogs.writeLogs(e.code)
            if e.code == 404 or e.code == 403:
                return None
            else:
                exit()
        except urllib2.URLError, e:
            self.filelogs.writeLogs('reason：'+e.reason)
            exit()
            return None
        
        if response:
            if response.getcode() != 200:
                self.filelogs.writeLogs(url+' 状态：'+response.getcode())
                return None
            try:
                readcont = response.read()
                return readcont
            except:
                self.filelogs.writeLogs('read失败')
                return None
        else:
            return None
    
    



