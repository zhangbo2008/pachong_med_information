# 用第一个chromdriver开不开, 用这个undetected就秒开了.

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Configure Chrome options.
opts = Options()
opts.add_argument('--disable-gpu')  # 设置没有使用gpu
# Configure ChromeDriver service.
# service = Service(ChromeDriverManager().install())

# Start the Chrome driver with the configured options and service.
driver = uc.Chrome( options=opts)
# opt = Options()
# opt.add_argument('--headless')  # 设置为无头, 屋头就失败, 后续再看吧.

# opt.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')

# driver = uc.Chrome(options= opt)
driver.minimize_window() #窗口最小化
driver.get('http://www.baidu.com', )
import time
time.sleep(3)
print(driver.page_source)















driver.close()
