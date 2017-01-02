import scrapy
import json

class KomandiruotesSpider(scrapy.Spider):
	name = 'komandiruotes'

	def start_requests(self):
		file_data = open('URLs.json')
		json_data = json.load(file_data)
		for node in json_data:
			yield scrapy.Request(url=node['url'], callback=self.parse)

	def parse(self, response):
		yield {
				'sprendimo_numeris': response.css('tr.border-bottom td.mobile-new-line::text')[0].extract(),
				'sprendimo_data': response.css('tr.border-bottom td.mobile-new-line::text')[1].extract(),
				'komandiruotes_laikotarpis': response.css('tr.border-bottom td.mobile-new-line::text')[2].extract(),
				'vykusio_asmens_vardas_pavarde': response.css('tr.border-bottom td.mobile-new-line::text')[3].extract(),
				'istaiga': response.css('tr.border-bottom td.mobile-new-line::text')[4].extract(),
				'vykusio_asmens_pareigybes': response.css('tr.border-bottom td.mobile-new-line::text')[5].extract(),
				'tikslas': response.css('tr.border-bottom td.mobile-new-line::text')[6].extract(),
				'isvykimo_vietos': response.css('tr.border-bottom td.mobile-new-line::text')[7].extract(),
				'finansuojama_suma_eur': response.css('tr.border-bottom td.mobile-new-line::text')[8].extract(),
				'komandiruotes_rezultatas': response.css('tr.border-bottom td.mobile-new-line::text')[9].extract(),
			}