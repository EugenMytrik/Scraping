import scrapy


class WorkuaSpider(scrapy.Spider):
    name = "workua"
    allowed_domains = ["work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response):
        for job in response.css("div.card-hover"):
            title = job.css("h2 a::text").get()
            link = job.css("h2.cut-top a::attr(href)").get()
            company = job.css("span.add-right-xs span.strong-600::text").get()

            yield {
                "title": title,
                "link": link,
                "company": company,
            }
