# 生成词云的图片

import jieba
from matplotlib import pyplot as plt    # 绘图，数据可视化
from wordcloud import WordCloud
import numpy as np                      # 矩阵运算
import sqlite3
from PIL import Image                   # 图片处理
# 准备词云需要的词
conn = sqlite3.connect("movie.db")
cur = conn.cursor()
sql = '''select instroduction from movie250'''
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
conn.close()
# 分词
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img)   # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="simhei.ttf"        
)
wc.generate_from_text(string)
# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 不显示坐标轴
# plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)   #保存图片
plt.show()          # 显示生成的词云
