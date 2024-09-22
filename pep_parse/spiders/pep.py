import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        pep_links = response.css(
            'section#numerical-index tbody tr a::attr(href)'
        ).getall()
        for pep_link in pep_links:
            if pep_link:
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        if title:
            number, name = title.split(' – ', 1)
            data = {
                'number': int(number.replace('PEP ', '').strip()),
                'name': name.strip(),
                'status': response.xpath('//dd//abbr/text()').get()
            }
            yield PepParseItem(data)
