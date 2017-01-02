import scrapy
import json

class LinksSpider(scrapy.Spider):
	name = 'links'
	start_urls = [
	# pakeiskit savo adresu
		'file://127.0.0.1/Users/vhs/workspace/komandiruotes/data_20170102.json'
	]

	def parse(self, response):
		json_response = json.loads(response.body_as_unicode())
		nodes = json_response["data"]

		for node in nodes:
			yield {
				'name': node["3"],
				'url': "http://portalas.vtd.lt" + node["DT_RowAttr"]["for"],
			}