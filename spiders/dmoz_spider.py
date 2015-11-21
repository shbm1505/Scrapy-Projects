from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from tutorial.items import MytestItem

class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.amazon.com/gp/product/B00VIPM9JQ?keywords=lenovo%20laptop&qid=1446730839&ref_=sr_1_1&sr=8-1"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//html')
     #   items = []
        f = open('y.xls','wb')
    #    with open('z.txt', 'wb') as f:
        items=[]

        for site in sites:
        #    item = Website()
            item=MytestItem()
            item['title'] = site.xpath('//div[@class="a-section"]/text()').extract()
            item['rating'] = site.xpath('//div[@class="a-icon-row a-spacing-none"]/a/@title').extract()
            item['help'] = site.xpath('//div[@class="a-row a-spacing-micro"]/span[contains(@class,"a-size-small a-color-secondary")]/text()').extract()
            items.append(item)
        #    rating = site.xpath('//div[@class="a-section celwidget"]/div[@class="a-row a-spacing-micro"]/spam[@class="a-row a-spacing-micro"]/text()').extract()
        #    item['url'] = site.xpath('a/@href').extract()
        #    item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
        #    items.append(item)
        #    print title
            #print rating
        for i in range(0,len(items)):
            f.write(str(items[i]['title'])+"   "+str(items[i]['rating'])+" "+str(items[i]['help'])+"\n")
        print items
     #   return items


        