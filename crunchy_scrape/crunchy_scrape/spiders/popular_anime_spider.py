import scrapy

class PopularAnime(scrapy.Spider):
    name = "popular"
    start_urls = ['http://www.crunchyroll.com/videos/anime/popular']

    def parse(self, response):
        for href in response.css('li.group-item a::attr(href)'):
            yield response.follow(href, self.parse_anime)

    def parse_anime(self, response):
        for title in response.css('h1.ellipsis'):
            yield {
                'anime-title': title.css('span::text').extract_first(),
            }