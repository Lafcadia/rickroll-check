import requests

def check(url):
    a = requests.get(url).text
    # print(a)
    ls = ['never gonna','give you up','so do i','never gonna give you up','never gonna let you down','rick','rickroll','你被骗了','诈骗']
    for i in ls:
        if i in a.lower():
            return True
    return False
                                                    
while True:
    t = input('请输入需要鉴定的网址：')
    state = "发现诈骗" if check(t) else "没有诈骗"
    print(state)
