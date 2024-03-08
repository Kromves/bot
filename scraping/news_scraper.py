# import requests
# from parsel import Selector
#
#
# class NewsScraper:
#     PLUS_URL = 'https://rezka.ag/animation/'
#     URL = 'https://rezka.ag/animation/adventures/'
#     HEADERS = {
#         "Accept-Language":
#             "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
#     }
#
#     LINK_XPATH = '//div[@class="b-content__inline_item-cover"]/a/@href'
#     IMG_XPATH = '//div[@class="b-content__inline_item-cover"]/a/img/@src'
#     TITLE_XPATH = '//div[@class="b-content__inline_item-link"]/a/text()'
#     DESCRIPTION_XPATH = '//div[@class="b-content__inline_item-link"]/div/text()'
#
#
#     def scrape_data(self):
#         response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
#         tree = Selector(text=response.text)
#         links = tree.xpath(self.LINK_XPATH).getall()[:5]
#         images = tree.xpath(self.IMG_XPATH).getall()[:5]
#         titles = tree.xpath(self.TITLE_XPATH).getall()[:5]
#         descs = tree.xpath(self.DESCRIPTION_XPATH).getall()[:5]
#
#         for desc in descs:
#             print(desc)
#
#         return links
#
#
# if __name__ == "__main__":
#     scraper = NewsScraper()
#     scraper.scrape_data()
#
# num = 123
# print(num)
