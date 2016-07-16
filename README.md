# Web Crawler Scrapy

## Description
I create a Scrapy project to crawl the information of applications in the Xiaomi Appstore (http://app.xiaomi.com). There are 30 categories in the homepage. And about 67 pages of application in every categories. The id, title, url, company, describe, introdction and application ID of every application was crawled. Then the data will be saved into Mongodb in json format. To implement the FindNextPage function Splash & ScrapyJS is used. Totally get 27284 applications. 
### Time
06/04/2016 to 07/02/2017.

### [Demo](https://www.youtube.com/watch?v=HVAR5syRljc&feature=youtu.be)
Created by [Ankai Liang](https://github.com/AnkaiLiang/-12WebCralwer)

### Usage
1. Install packages.
  - [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)
  - [MongoDB](https://docs.mongodb.com/master/installation/)
  - [Splash](https://splash.readthedocs.io/en/stable/install.html)
  - [ScrapyJS](https://pypi.python.org/pypi/scrapyjs)
2. Start your Splash and MongoDB server.
    + Start your MongoDB:
    
        ```bash
        ./mongod
        ```
        
    + Start Splash:

        ```bash
        docker run -p 8050:8050 scrapinghub/splash
        ```


3. Modify the the code in xiaomi/settings.py.
Set your Splash server address and the information of MongoDB. 
In my case, it's :

    ```python
    SPLASH_URL = 'http://192.168.99.100:8050'
    MONGODB_SERVER = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "Xiaomi"
    MONGODB_COLLECTION = "AppInfo"
    ```

5. Go to the catalog /xiaomi, Run the crawler:

    ```bash
    scrapy crawl xiaomi
    ```

### Team
We have 4 people in our team. And we independently complete the entire project coding.
  - [AnkaiLiang](https://github.com/AnkaiLiang)
  - [Taran](https://github.com/songtailun)
  - [Kristy Luo](https://github.com/Kristy-Luo)
  - [jenny91515](https://github.com/jenny91515)

### Acknowledgement
  - BitTiger
  - Jing Li
  - [jamesyx](https://github.com/jamesyxw/crawler)

## Resource
  - [BitTiger Project: Web Crawler Scrapy](https://www.bittiger.io/microproject/oYDSG6MSFihpiNJ66)
  - [Scrapy](http://scrapy.org)
  - [MongoDB](https://www.mongodb.org)
  - [Splash & ScrapyJS](https://github.com/scrapinghub/scrapy-splash)
  - [ScrapyJS & ScrapyJS](https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/)

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

## Project Information
- category: full stack
- team: 12WebCralwer
- description: a Scrapy project to crawl the content in the Xiaomi Appstore homepage
- stack: mongodb, python
