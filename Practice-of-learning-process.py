# Practice-of-learning-process 关于学习上的一些练习内容，注释和容易犯错的点
# 第一阶段结果 从0到认识python 用时5天学习（马士兵教育免费教学课程）
import requests
import json
import openpyxl
wk = openpyxl.Workbook()
sheep = wk.create_sheet() 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'}
# headers作用：让Pycharm伪装成浏览器，获取:打开浏览器，右键空白处检查网页network-随便点击一个——Headers——找到user-agent全段复制
# 例如复制到还需要进行一定的格式更改 User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400
rest = requests.get('url',headers = headers)  
# "url"获取：单机 空白处检查网页network，刷新，搜索相关内容，复制URL进来
resp = rest.text
# print(resp) 去掉中括号前后内容，已适应JSON解析库
content = resp.replace('','').replace('','')
json_loads = json.loads(content)
comments = json_loads['comments']
for item in comments:
  xxx = item['子项xxx']
  yyy = item['子项yyy']
  sheep.append([xxx,yyy]) # xxx放在excel表格第一栏，yyy放在excel表格第二栏,容易忽略sheep
wk.save('C:\\Users\\kx\\Date/文件名.xlsx') #记住将\改为\\
