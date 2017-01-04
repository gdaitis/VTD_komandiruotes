import scrapy
import json
import urllib2

class KomandiruotesSpider(scrapy.Spider):
	name = 'komandiruotes'

	def start_requests(self):
		file_data = urllib2.urlopen('https://raw.githubusercontent.com/gdaitis/VTD_komandiruotes/master/scrapper/URLs.json')
		json_data = json.load(file_data)
		for node in json_data:
			yield scrapy.Request(url=node['url'], callback=self.parse)

	def parse(self, response):
		array = response.css('tr.border-bottom td.mobile-new-line')
		yield {
				'sprendimo_numeris': array[0].css("::text").extract_first(),
				'sprendimo_data': array[1].css("::text").extract_first(),
				'komandiruotes_laikotarpis': array[2].css("::text").extract_first(),
				'vykusio_asmens_vardas_pavarde': array[3].css("::text").extract_first(),
				'istaiga': array[4].css("::text").extract_first(),
				'vykusio_asmens_pareigybes': array[5].css("::text").extract_first(),
				'tikslas': array[6].css("::text").extract_first(),
				'isvykimo_vietos': array[7].css("::text").extract_first(),
				'finansuojama_suma_eur': array[8].css("::text").extract_first(),
				'komandiruotes_rezultatas': array[9].css("::text").extract_first(),
			}