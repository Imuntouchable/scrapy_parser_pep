import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        rows = response.xpath('//section[@id="numerical-index"]//tbody/tr')
        for row in rows:
            pep_link = row.xpath('.//a/@href').get()
            if pep_link:
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        if title:
            number, name = title.split(' – ', 1)
            data = {
                'number': int(number.replace('PEP ', '')),
                'name': name.strip(),
                'status': response.xpath('//dd//abbr/text()').get()
            }
            yield PepParseItem(data)
