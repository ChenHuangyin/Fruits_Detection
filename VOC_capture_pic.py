import re
import requests
import os

def download(html,keyword,index):
    if(index == 0):
        os.makedirs('./'+keyword)
    pic_urls = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print ('开始下载'+keyword+'...')
    for url in pic_urls:
        print ('正在下载第'+str(i+1)+'张图片')
        try:
            pic= requests.get(url, timeout=10,allow_redirects=False)
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ChunkedEncodingError:
            continue
        string = './' + keyword +'/'+keyword+'_'+ str(index) + '_' + str(i) + '.jpg'

        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    keywords = ['香蕉','菠萝','西瓜','橙子','草莓','芒果','葡萄','苹果']
    
    for j in range(len(keywords)):
        for i in range(25):
            url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+keywords[j]+'&pn='+str(i*20)
            result = requests.get(url,allow_redirects=False)
            download(result.text,keywords[j],i)
