import scrapy

# from tutorial.tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.pythonscraping.com/pages/page1.html"
        "http://www.pythonscraping.com/pages/page3.html"
        # ,"http://en.wikipedia.org/wiki/Kevin_Bacon"
    ]

    def parse(self, response):
        title = response.xpath('//html/body/h1/text()').extract()
        print("title: ", title)

        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for sel in response.xpath('//ul/li'):
            # item = DmozItem()
            # link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print("title: " + title)
        #     # print(title, link, desc)
        #     # print(title, link, desc)

