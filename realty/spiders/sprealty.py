from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import Request
from realty.items import RealtyItem
from urlparse import urlparse, urljoin


class RealtySpider(Spider):
    name = "realty"
    allowed_domains = ["irk.etagi.com"]
    start_urls = [
        "http://irk.etagi.com/realty/trehkomnatnye-kvartiry/",
        "http://irk.etagi.com/realty/elitnye-kvartiry/",
    ]

    def parse(self, response):
        """
        """
        sel = Selector(response)
        sites = sel.xpath("//div[@class='tabs-container']//*//article//div[@class='description']")
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(response.url))
        rub = u'\u0440\u0443\u0431.'
        items = []
        for site in sites:
            item = RealtyItem()
            price = site.xpath(".//section[@class='d-1']//p[@class='price']//span/text()").extract()[0]
            price = price.replace(rub, '').replace(u' ', '')
            item['price'] = price
            item['floor'] = site.xpath(".//section[@class='d-2 params']//p[@class='row floor']//span[@class='value corporate_red']/text()").extract()[0]
            item['space'] = site.xpath(".//section[@class='d-2 params']//p[@class='row space']//span[@class='value corporate_red']/text()").extract()[0]
            item['url'] = urljoin(domain, site.xpath(".//p[@class='title-obj']/a/@href").extract()[0])
            kitchen = site.xpath(".//section[@class='d-2 params']//p[@class='row kitchen']//span[@class='value corporate_red']/text()").extract()
            if kitchen:
                item['kitchen'] = kitchen[0]
                # item['district'] = request.meta['item']
            request = Request(item['url'], callback=self.parse_page)
            request.meta['item'] = item
            yield request

            items.append(item)

    @staticmethod
    def parse_page(response):
        item = response.meta['item']
        item['district'] = response.xpath(".//tr[1]/td[2]/text()").extract()[0]
        return item
