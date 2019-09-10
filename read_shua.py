import re
import requests
import time
import telnetlib
import os
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
def get_id(name,url):
    name = name+'.txt'
    text = open(name,'a')
    for j in range(1,50):
        try:
            html = requests.get(url+'/article/list/'+str(j)+'?',headers = headers).text
            id_list = re.findall(r'data-articleid="(.*?)">',html)
            if id_list==[]:
                print("空")
                break
            else:
                for i in range(0,len(id_list)):
                    text.write(url+'/article/details/'+id_list[i]+'\n')
            print(id_list)
        except Exception as errors:
            print(errors)
    text.close()
def enter_web(urls):
    try:
        html = requests.get(urls,headers = headers)
        #print("+1")
    except:
        print("-1")
if __name__=="__main__":
    url = input("请输入csdn博客主页url （例：https://blog.csdn.net/qq_37174835）:")
    #url = 'https://blog.csdn.net/qq_37174835'
    name = input("请输入你的名字(代号 例：cctv)：")
    a = 0
    ss = name+'.txt'
    print("程序正在运行----阅读量增加中")
    print("每2分钟所有博客阅读+1")
    while 1:
        a+=1
        if os.path.exists(ss)==False:
            print("文件不存在")
            get_id(name,url)
        f_txt = open(ss, 'r')
        all_url = f_txt.readlines()
        length = len(all_url)
        for line in range(0, length):
            try:
                line_url = all_url[line]
                line_url = line_url.rstrip('\n')
                enter_web(line_url)
                #print(line_url)
            except Exception as errors:
                print(errors)
        f_txt.close()
        print("已经运行了%d次"%a)
        time.sleep(120)
        pass