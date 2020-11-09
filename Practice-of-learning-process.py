# Practice-of-learning-process 关于学习上的一些练习内容，注释和容易犯错的点
# 第一阶段结果 从0到认识python 用时5天学习（马士兵教育免费教学课程）
import requests
import json
import openpylx
headers = {}  
# headers作用：让Pycharm伪装成浏览器，获取:打开浏览器
rest = requests.get('url',headers = headers)  
# "url"获取：单机 空白处检查网页network
