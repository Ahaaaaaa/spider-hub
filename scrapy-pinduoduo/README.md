### 拼多多商品信息爬虫

基于scrapy的拼多多的爬虫，默认抓取拼多多的热门栏目所有商品，每个商品只获取二十条评论，爬取到的数据存储到MongoDB数据库

### 环境
python 3.6.7    
mongodb

### 启动过程
##### 1. 安装依赖
```
$ pip3 install pymongo
$ pip3 install scrapy
```

##### 2. 命令行启动
```
$ scrapy crawl pinduoduo
$ 
```
