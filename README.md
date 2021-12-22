# douban_flask
#### 所需要的库

```
flask
sqlite3
bs4
re  
xlwt 
jieba
matplotlib
wordcloud
numpy
PIL
```



####  一个爬取豆瓣电影并可视化的项目

项目学习自B站https://www.bilibili.com/video/BV12E411A7ZQ

#### 项目截图

![](https://raw.githubusercontent.com/sanxiadaba/myPic/master/img/799e96ec-4f40-4ec8-9e18-97c36ba3f3c4.png)

![](https://raw.githubusercontent.com/sanxiadaba/myPic/master/img/0471a947-c237-4445-abac-3bb8133affb7.png)

![](https://raw.githubusercontent.com/sanxiadaba/myPic/master/img/7af51bc9-9b08-45fe-95d0-85cf25564500.png)

![](https://raw.githubusercontent.com/sanxiadaba/myPic/master/img/a86a007d-dad8-4fc1-b789-694632f4c340.png)







### 项目运行

spider为进行爬虫的主程序，to_spider为其的调用

运行to_spider可生成top250的excel与db文件（原始项目已经配备的有）

再运行app.py打开本地的1234端口即可打开本项目



### 注意

有时爬虫程序会被拒绝访问

解决方法：设置cookies

先在电脑端访问网址https://movie.douban.com/top250 再右键点击检查，找到network或网络选项卡再选择all标签，然后再次刷新页面

找到对应页面

![](https://raw.githubusercontent.com/sanxiadaba/myPic/master/img/TLUPA_XB_EV3EK%7B2%7DS%7BC5%5BN.png)

将cookies复制下来，更换constant下对应的cookies值即可（注意cookies本身不是一个字符串，别忘最后开始和末尾加上单引号）


