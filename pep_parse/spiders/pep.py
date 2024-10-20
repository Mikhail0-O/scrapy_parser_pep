import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        all_link = response.css('a.pep.reference.internal')
        for author_link in all_link:
            yield response.follow(author_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').get().split(' ')[1],
            'name': ' '.join(response.css(
                'h1.page-title::text').get().split(' ')[3:]),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get()
        }

        yield PepParseItem(data)
