import os
import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

# delete file if it already excists to avoid duplicates
if os.path.exists('br24crawl.json'):
    os.remove('br24crawl.json')


class crawl(scrapy.Spider):
    name = 'BR24'
    # assign url
    start_urls = [
        'https://www.br.de/nachrichten/wissen/faq-coronavirus-die-wichtigsten-fragen-und-antworten,Rorgu8D']

    def parse(self, response):
     #   print (response.css('h3::text').extract())
        # assign sections of faqs
        faqs = response.css('section.css-1jftgse')
        # assign date of publish
        time_publish = response.css('time.aipd-gtm::text').extract()
        # create list for all faqs
        all_faqs = list()
        # loop to iterate over website
        for i in range(2, len(faqs)):
            faq = faqs[i]
            titlefaqs = faq.css('h4::text').extract()
            #    print (titlefaqs)
            #    print (i-1)
            textfaqs = faq.css('p::text').extract()
            #    print (textfaqs)
            # define json format
            if len(textfaqs) > 0 and len(titlefaqs) > 0:
                BR24faqs = dict()
                BR24faqs['title'] = str(titlefaqs[0])
                BR24faqs['text'] = str(textfaqs[0])
                BR24faqs['publisher'] = (self.name)
                BR24faqs['publish_date'] = str(time_publish[0])
                BR24faqs['url'] = (self.start_urls[0])
                all_faqs.append(BR24faqs)
        return all_faqs
