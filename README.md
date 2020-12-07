# screenshot
基于selenium的批量网页截图小工具，适用于批量网站核验研判，暂时只支持Chrome

### 准备驱动
下载链接：[chromedriver](http://chromedriver.storage.googleapis.com/index.html) 
选择与Chrome版本一致的驱动软件，并放在当前目录(样例文件为谷歌V87.0.4280)

###  需要截图的url
将要截图的网址复制到 ./url.txt  里，里面有样例网址

###  运行
运行  python .\screenshot.py

### 结果
结果存储到 './result/'
其中 ./result/res.txt 为截图+url信息
