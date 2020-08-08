import scrapy


class VtcnewsSpider(scrapy.Spider):
    name = 'vnexpress'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('meta[name="tt_page_type"]::attr("content")').get() =='article':

            f = open('D:/ExampleCode/ExampleCode/output/vnexpress/vnexpress.txt', 'a', encoding='utf8')

            link = response.url
            f.write('[Link]'+link.strip()+'\n')
            f.write('\n')

            title = response.css('h1.title-detail::text').get().strip()
            f.write('[title]' + str(title)+'\n')
            f.write('\n')

            category = response.css('ul.breadcrumb > li > a  ::text').get().strip()
            f.write('[category]'+str(category)+'\n')
            f.write('\n')

            date = response.css('span.date ::text').get()
            f.write('[date]'+date+'\n')
            f.write('\n')

            description = response.css('p.description::text').get().strip().split(',')
            f.write('[description]' + str(description) + '\n')
            f.write('\n')

            f.write('[content]'+'\n')
            for i in response.css('article.fck_detail p.Normal'):
                content = ''.join(i.css('*::text').getall())
                f.write(content + '\n')
                f.write('\n')

            f.write('[tags]'+'\n')
            for i in response.css('h4.item-tag > a'):
                tags = ''.join(i.css('*::text').getall())
                f.write(tags + '\n')
                f.write('\n')

            author = response.css('p.Normal strong ::text').get().strip()
            f.write('[author]' + str(author) + '\n')
            f.write('\n')

            f.write('\n')
            self.CRAWLED_COUNT += 1
            self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)

            f.write(str(self.CRAWLED_COUNT)+'\n')

        yield from response.follow_all(css='a[href^="https://vnexpress.net"]::attr(href),a[href^="/"]::attr(href)',callback=self.parse)
