import scrapy

class PopularAnime(scrapy.Spider):
    name = "popular"
    start_urls = ['http://www.crunchyroll.com/videos/anime/popular']

    def parse(self, response):
        for href in response.css('li.group-item a::attr(href)'):
            yield response.follow(href, self.parse_anime)

    def parse_anime(self, response):
        def css_extract(query):
            return response.css(query).extract_first().strip('()')

        yield {
            'anime-title': css_extract('h1.ellipsis span::text'),
            '5-stars': css_extract('ul.rating-histogram:nth-child(3) > li:nth-child(1) > div:nth-child(3)::text'),
            '4-stars': css_extract('ul.rating-histogram:nth-child(3) > li:nth-child(2) > div:nth-child(3)::text'),
            '3-stars': css_extract('ul.rating-histogram:nth-child(3) > li:nth-child(3) > div:nth-child(3)::text'),
            '2-stars': css_extract('ul.rating-histogram:nth-child(3) > li:nth-child(4) > div:nth-child(3)::text'),
            '1-stars': css_extract('ul.rating-histogram:nth-child(3) > li:nth-child(5) > div:nth-child(3)::text'),
        }