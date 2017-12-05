import scrapy


class IfashionSpider(scrapy.Spider):
    name = 'ifashion'
    start_urls = [
        'https://guang.taobao.com/ifashion/kantugouDetail.htm?spm=a21ct.88415.403469.13.69c8caeaWMsnLa&contentId=2738958&gender=0']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'w') as f:
            f.write(response.body)
