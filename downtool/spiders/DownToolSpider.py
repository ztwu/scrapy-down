import scrapy as scrapy

from downtool.DownToolItem import DownToolItem

class DownToolSpider(scrapy.Spider) :
    # 爬虫名字，唯一，用于区分以后新建的爬虫
    name = "downtool"

    # 可选，定义爬取区域，超出区域的链接不爬取
    allowed_domains = ["so.redocn.com"]  # 如果对于页面没有特殊要求，也可以不写

    # 定义开始爬取的页面
    start_urls = ["http://so.redocn.com/shuiguo/cbaeb9fb.htm"]

    def parse(self, response):
        urls = response.xpath('//div[@class="wrap g-bd"]/div/dl/dd/a/img[not(contains(@class, "lazy"))]/@src').extract()
        for url in urls :
            imgItem = DownToolItem()
            imgItem['img'] = [url]
            #imgItem['gif'] = []  # 上面如果定义了gif关键字，就得给初始化

            # 将结果交给Pipeline处理
            yield imgItem

        nexturl = response.xpath(u'//a[contains(text(),"下一页")]/@href').extract()
        domains = ['http://so.redocn.com']
        nexturl_all = domains[0] + nexturl[0]

        if nexturl_all :
            yield scrapy.Request(nexturl_all, callback=self.parse)