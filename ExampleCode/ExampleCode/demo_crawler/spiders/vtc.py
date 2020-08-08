import scrapy


class VtcnewsSpider(scrapy.Spider):
    name = 'vtc'
    allowed_domains = ['vtc.vn']
    start_urls = ['https://vtc.vn/']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('body[class="load-news-detail ads"]::attr("data-page")').get() =='detail':

            f = open('D:/ExampleCode/ExampleCode/output/vtc/vtc.txt', 'a', encoding='utf8')

            link = response.url
            f.write('[Link]'+link.strip()+'\n')
            f.write('\n')

            title = response.css('h1.font28.bold.lh-1-3::text').get().strip()
            f.write('[title]' + str(title)+'\n')
            f.write('\n')

            category = response.css('div.mb15.gray-91.font12 a::attr(title)').get().strip()
            f.write('[category]'+str(category)+'\n')
            f.write('\n')

            date = response.css('span.time-update.mr10::text').get()
            f.write('[date]'+date+'\n')
            f.write('\n')

            description = response.css('h4.font16.bold.mb15::text').get().strip().split(',')
            f.write('[description]' + str(description) + '\n')
            f.write('\n')

            f.write('[related news]'+'\n')
            for i in response.css('h3.borbot-e0-doted.pb5.mb5.font14.pl15.relative a'):
                relatedNews = ''.join(i.css('*::text').getall())
                f.write(relatedNews+'\n')
                f.write('\n')

            f.write('[content]'+'\n')
            for i in response.css('div.edittor-content.box-cont.clearfix p'):
                content = ''.join(i.css('*::text').getall())
                f.write(content + '\n')
                f.write('\n')

            f.write('[tags]'+'\n')
            for i in response.css('li.inline.mr5.mb5 > div > a'):
                tags = ''.join(i.css('*::text').getall())
                f.write(tags + '\n')
                f.write('\n')

            author = response.css('span.uppercase.bold ::text').get().strip()
            f.write('[author]' + str(author) + '\n')
            f.write('\n')

            f.write('\n')
            self.CRAWLED_COUNT += 1
            self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)

            f.write(str(self.CRAWLED_COUNT)+'\n')

        yield from response.follow_all(css='a[href^="https://vtc.vn/"]::attr(href),a[href^="/"]::attr(href)',callback=self.parse)
