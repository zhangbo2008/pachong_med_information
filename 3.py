# 解析test.html



with open('test.html') as f:
   a=f.read()
a_old=a
   
from bs4 import BeautifulSoup


soup = BeautifulSoup(a, 'html.parser')

# 查找<h1>标签
h1_tag = soup.find('h1')


# 查找所有<p>标签
p_tags = soup.find_all('div')
p_tags = soup.find_all('div', class_="panel-heading")

# 提取第一个<p>标签的文本内容
p_text = p_tags[0].text

print("段落:", p_text)


# 分层解析:
#第一层是: #每一层都展开就行, 都是class写法.
#这一层逻辑是字典
# save={}
# for L1 in soup.find_all('div', class_="panel panel-default"):

#       k1 =L1.find('div', class_="panel-heading").text.strip()
#       v1 =L1.find('div', class_="panel-collapse collapse in")
#       v2 =L1.find('div', class_="panel-collapse collapse") #这个地方标签有2种写法.
#       if v1==None:
#          v1=v2
#       save1=[]
#       for  k2 in v1.find_all('table', class_="searchDetailTable"):
#           save2=[] #======这一层是一个数组来记录元素 .
#           for v2 in k2.find_all('tr', ):
            
#             #=======最后一层嵌套th, td
#             all_th=[]
#             all_td=[]
#             inner_dict={}
#             for k3 in v2.find_all('th'):
#                all_th.append(k3.text.strip())
#             for v3 in v2.find_all('td'):
#                 all_td.append(v3.text.strip())
#             all_td=all_td+[0]*(len(all_th)-len(all_td))
#             for i in range(len(all_th)):
#               inner_dict[all_th[i]]=all_td[i] #拼接好最内层数据的字典.再往外传到.
#             print(1)
#             save2.append(inner_dict)
#           save1.append(save2)
#       #=====我们逻辑是把内层拼好字典.
#       print(1)
#       save[k1]=save1
# print(1)


#=========最强的解析软件还是这个lxml!!!!!!!!!!!!!!但是还是soup稳定.可以多次查询.
#=======现在发现他所有key都是定死的,所以直接每次定死text爬取即可.更准


#1....................基本信息
#

from lxml import etree
save={}
jibenxinxi=[]

aa=etree.HTML(a)
tmp=aa.xpath('//div[@id="collapseOne"]//table')
th=aa.xpath('//div[@id="collapseOne"]//table//th//text()')
td=aa.xpath('//div[@id="collapseOne"]//table//td//text()')

td=[i.strip() for i in td]
d1={}
for i in range(len(th)):
  d1[th[i]]=td[i]
  
save['基本信息']=d1
print(1)
# 写入公式信息.  # xpath 多次查询不太对, 还是用回soup!!!还是soup稳定!!!!!!!!!!!!!!!!!!!!!!


a=soup.find_all('table', class_="searchDetailTable")[1]
all_th=[i.get_text().strip().replace('\n','') for i in a.find_all('th')]
all_td=[i.get_text().strip().replace('\n','') for i in a.find_all('td')]
d1={}
for i in range(len(all_th)):
  d1[all_th[i]]=all_td[i]
save['公示的试验信息']={}
save['公示的试验信息']['一、题目和背景信息']=d1
pass



#========二、申请人信息




a=soup.find_all('table', class_="searchDetailTable")[2]
all_th=[i.get_text().strip().replace('\n','') for i in a.find_all('th')]
all_td=[i.get_text().strip().replace('\n','') for i in a.find_all('td')]
d1={}
for i in range(len(all_th)):
  d1[all_th[i]]=all_td[i]

save['公示的试验信息']['二、申请人信息']=d1


pass


# 三、临床试验信息:实验目的.实验设计

import re#直接正则得了.
helper=a_old[a_old.find('<div class="sDPTit2">1、试验目的</div>'):]
helper=helper[len('<div class="sDPTit2">1、试验目的</div>')+1:helper.find('<div class="sDPTit2">2、试验设计</div>')].strip()
a=soup.find_all('table', class_="searchDetailTable")[3]

all_th=[i.get_text().strip().replace('\n','') for i in a.find_all('th')]
all_td=[i.get_text().strip().replace('\n','') for i in a.find_all('td')]
d1={}
for i in range(len(all_th)):
  d1[all_th[i]]=all_td[i]

save['公示的试验信息']['三、临床试验信息']={}
save['公示的试验信息']['三、临床试验信息']={'1、试验目的':helper,'2、试验设计':d1}



# 3、受试者信息


a=soup.find_all('table', class_="searchDetailTable")[4]

all_th=[i.get_text().strip().replace('\n','') for i in a.find_all('th')]
all_td=[i.get_text().strip().replace('\n','') for i in a.find_all('td')]
d1={}
for i in range(len(all_th)):
  d1[all_th[i]]=all_td[i]
save['公示的试验信息']['三、临床试验信息']['3、受试者信息']=d1



#==============入选标准
ruxuanbiaozhun=a.find_all('tr',)[3].find('td')
ruxuanbiaozhun=ruxuanbiaozhun.find_all('td')

all_th=[i.get_text().strip().replace('\n','') for i in ruxuanbiaozhun[::2]]
all_td=[i.get_text().strip().replace('\n','') for i in ruxuanbiaozhun[1::2]]
d2={}
for i in range(len(all_th)):
  d2[all_th[i]]=all_td[i]
save['公示的试验信息']['三、临床试验信息']['3、受试者信息']['入选标准']=d2


pass


#=======注意find_all函数recursive默认是打开的, 但是我们层级结构经常需要关闭他!!!!!!!!!!!!

# 排除标准
ruxuanbiaozhun=a.find_all('tr',recursive=False)[4].find('td')
ruxuanbiaozhun=ruxuanbiaozhun.find_all('td')

all_th=[i.get_text().strip().replace('\n','') for i in ruxuanbiaozhun[::2]]
all_td=[i.get_text().strip().replace('\n','') for i in ruxuanbiaozhun[1::2]]
d2={}
for i in range(len(all_th)):
  d2[all_th[i]]=all_td[i]
save['公示的试验信息']['三、临床试验信息']['3、受试者信息']['排除标准']=d2

pass


# 4、试验分组



#''试验药''
a=soup.find_all('table', class_="searchDetailTable")[5]
a=a.find('tr')
a=a.find_all('tr')[1:]
a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),'名称':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),'用法':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t','')} for i in a]
pass

helper2={'试验药':a}
#对照药

a=soup.find_all('table', class_="searchDetailTable")[5]
a=a.find_all('tr',recursive=False)[1]
a=a.find_all('tr')[1:]
a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),'名称':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),'用法':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t','')} for i in a]

print(1)
helper2['对照药']=a

save['公示的试验信息']['三、临床试验信息']['4、试验分组']=helper2
pass









#5. 重点指标:
a=soup.find_all('table', class_="searchDetailTable")[6]
a=a.find('tr',recursive=False)
a=a.find_all('tr')[1:]
a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),'指标':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),'评价时间':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t',''),'终点指标选择':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t','')} for i in a]

pass
helper4={'主要终点指标及评价时间':a}



a=soup.find_all('table', class_="searchDetailTable")[6]
a=a.find_all('tr',recursive=False)[1]
a=a.find_all('tr')[1:]
a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),'指标':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),'评价时间':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t',''),'终点指标选择':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t','')} for i in a]




helper4['次要终点指标及评价时间']=a

pass

save['公示的试验信息']['三、临床试验信息']['5、终点指标']=helper4
# helper3={'5、终点指标':}








pass


a=soup.find_all('table', class_="searchDetailTable")[7]


th=a.find_all('th')[1:]
td=a.find_all('td')
all_th=[i.get_text().strip().replace('\n','') for i in th]
all_td=[i.get_text().strip().replace('\n','') for i in td]

d1={}
for i in range(len(all_th)):
  d1[all_th[i]]=all_td[i]
pass






save['公示的试验信息']['四、研究者信息']={}
save['公示的试验信息']['四、研究者信息']['1、主要研究者信息']=d1

pass





# 2、各参加机构信息
a=soup.find_all('table', class_="searchDetailTable")[8]


aaa=a.find_all('tr')[1:]
bbbbb=[i.find_all('td') for i in aaa]


a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),
    '机构名称':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),
    '主要研究者':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t',''),
    '国家或地区':i.find_all('td')[3].get_text().strip().replace('\n','').replace('\t',''),
     '省（州）':i.find_all('td')[4].get_text().strip().replace('\n','').replace('\t',''),
         '城市':i.find_all('td')[5].get_text().strip().replace('\n','').replace('\t',''),
        
    } for i in aaa]















save['公示的试验信息']['四、研究者信息']['2、各参加机构信息']=a

print(1)


# 
# 五、伦理委员会信息
a=soup.find_all('table', class_="searchDetailTable")[9]


aaa=a.find_all('tr')[1:]
bbbbb=[i.find_all('td') for i in aaa]




a=[{'序号':i.find_all('td')[0].get_text().strip().replace('\n','').replace('\t',''),
    '名称':i.find_all('td')[1].get_text().strip().replace('\n','').replace('\t',''),
    '审查结论':i.find_all('td')[2].get_text().strip().replace('\n','').replace('\t',''),
    '批准日期/备案日期':i.find_all('td')[3].get_text().strip().replace('\n','').replace('\t',''),
        
    } for i in aaa]
pass



save['公示的试验信息']['五、伦理委员会信息']=a