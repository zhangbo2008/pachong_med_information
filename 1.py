from selenium.webdriver import Chrome  # http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml  我们实战爬取这个网页所有内容!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import time
# https://blog.csdn.net/zhoukeguai/article/details/113247342   
# driver = Chrome("./chromedriver.exe")
# 把当前目录下的chromdriver.exe复制到你的python安装目录. 我用的124版本, 根据自己需要下载即可.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 导入无头浏览器的包

opt = Options()
opt.add_argument('--headless')  # 设置为无头
# opt.add_argument('--disable-gpu')  # 设置没有使用gpu
opt.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
opt.add_argument(f'user-agent={user_agent}')

opt.add_experimental_option("excludeSwitches",["enable-automation"])
opt.add_experimental_option("useAutomationExtension",'False')






opt.add_argument('--disable-javascript')
opt.add_argument('disable-infobars')
opt.add_experimental_option('detach', True)
opt.add_argument('-disable-blink-features=AutomationControlled')





# =====这个可以解决网页空白的问题.
web = Chrome(options= opt)  # 然后配置放到浏览器上
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            })

# http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml
web.get('http://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml')
# web.get('http://www.baidu.com')
time.sleep(1) #=======第一次要等1秒,等网页加载过来, 如果你网更慢, 就设置更慢一嗲.
# el = web.find_element('xpath','//*[@type="submit"]') #这是新版的，旧版是：find_element_by_xpath
# el.click() # 点击事件
# print('打印title')
# print(web.title)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


a=[]
a.append(web.page_source) # 保存第一页.
cnt=0
for i in range(24689-1): #下面循环总页数-1次.
    web.find_element(by=By.XPATH,value="//span[@class='fa fa-angle-right']").click()
    login_btn=WebDriverWait(web,10,0.1).until(EC.presence_of_element_located((By.ID, "block5")))  #写入一个等待的id即可.
    a.append(web.page_source)
    cnt+=1
    print(cnt)

for  dex,i in enumerate(a):
    with open(f'd:/savehtml/{dex}.html','w') as f:
      f.write(i)