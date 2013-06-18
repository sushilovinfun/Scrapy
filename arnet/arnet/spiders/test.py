from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from arnet.items import ArnetItem

class MySpider(CrawlSpider):
    name = "arnet"
    allowed_domains = ["arnetminer.org"]
    
    start_urls = [
    	"http://arnetminer.org/person/usama-m-fayyad-157717.html",
        "http://arnetminer.org/person/g-piatetsky-shapiro-498336.html",
        "http://arnetminer.org/person/nicholas-weir-86638.html",
        "http://arnetminer.org/person/s-djorgovski-821874.html",
        "http://arnetminer.org/person/padhraic-smyth-218377.html",
        "http://arnetminer.org/person/-/148983",
        "http://arnetminer.org/person/john-a-major-1180829.html",
        "http://arnetminer.org/person/t-anand-174071.html",
        "http://arnetminer.org/person/gary-s-kahn-326979.html",
        "http://arnetminer.org/person/-/255251",
        "http://arnetminer.org/person/-/799907",
        "http://arnetminer.org/person/-/199147",
        "http://arnetminer.org/person/-/501751",
        "http://arnetminer.org/person/-/528417",
        "http://arnetminer.org/person/sharad-saxena-1405144.html",
        "http://arnetminer.org/person/-/953937",
        "http://arnetminer.org/person/-/871397",
        "http://arnetminer.org/person/-/637625",
        "http://arnetminer.org/person/-/5066",
        "http://arnetminer.org/person/-/236237",
        "http://arnetminer.org/person/-/484628",
        "http://arnetminer.org/person/-/239881",
        "http://arnetminer.org/person/-/922122",
        "http://arnetminer.org/person/lisa-ballesteros-495880.html",
        "http://arnetminer.org/person/adam-carlson-160770.html",
        "http://arnetminer.org/person/adam-st-amant-1402150.html", #note this appears to be a typo while Robert below it appears to be the real guy he doesn't get the credit
        "http://arnetminer.org/person/-/970611",
        "http://arnetminer.org/person/-/390868",
        "http://arnetminer.org/person/-/579925",
        "http://arnetminer.org/person/-/275533",
        "http://arnetminer.org/person/-/1488977",
        "http://arnetminer.org/person/-/313640",
        "http://arnetminer.org/person/-/298351",
        "http://arnetminer.org/person/-/207926",
        "http://arnetminer.org/person/-/1284140",
        "http://arnetminer.org/person/fern-halper-88453.html",
        "http://arnetminer.org/person/thomas-kirk-549613.html",
        "http://arnetminer.org/person/alan-lazar-858824.html",
        "http://arnetminer.org/person/deborah-l-mcguinness-855791.html",
        "http://arnetminer.org/person/lori-alperin-resnick-1498658.html",
        "http://arnetminer.org/person/-/1048625",
        "http://arnetminer.org/person/-/887121",
        "http://arnetminer.org/person/-/298504",
        "http://arnetminer.org/person/philip-k-chan-219909.html",
        "http://arnetminer.org/person/-/1193943", #may not be the right person
        #Patricia Lynch Carbone (MITRE) and Larry Kershberg (George Mason U.) are missing from arnetminer.org
        "http://arnetminer.org/person/-/699455",
        "http://arnetminer.org/person/-/155634",
        "http://arnetminer.org/person/-/1100976",
        #W. James Bishop could not be found
        "http://arnetminer.org/person/chun-nan-hsu-106824.html",
        "http://arnetminer.org/person/c-a-knoblock-477259.html",
        "http://arnetminer.org/person/-/1496816",
        "http://arnetminer.org/person/wesley-w-chu-340364.html",
        "http://arnetminer.org/person/-/359652",
        "http://arnetminer.org/person/-/68026",
        "http://arnetminer.org/person/-/745329",
        "http://arnetminer.org/person/-/1344877",
        "http://arnetminer.org/person/-/637822",
        "http://arnetminer.org/person/-/1187409",
        "http://arnetminer.org/person/-/695243",
        "http://arnetminer.org/person/sholom-m-weiss-507972.html",
        "http://arnetminer.org/person/fred-damerau-241291.html",
        "http://arnetminer.org/person/-/1286436",
        "http://arnetminer.org/person/brian-gaines-752481.html",
        "http://arnetminer.org/person/-/545590",
        "http://arnetminer.org/person/-/424271",
        "http://arnetminer.org/person/randy-kerber-59785.html",
        "http://arnetminer.org/person/-/96334",
        "http://arnetminer.org/person/-/345316",
        "http://arnetminer.org/person/-/114083",
        "http://arnetminer.org/person/dan-geiger-330355.html",
        "http://arnetminer.org/person/david-maxwell-chickering-1215050.html",
        "http://arnetminer.org/person/-/134804",
        "http://arnetminer.org/person/-/153907",
        "http://arnetminer.org/person/-/178578",
        "http://arnetminer.org/person/-/1514123",
        "http://arnetminer.org/person/hiroshi-tanaka-214797.html",
        "http://arnetminer.org/person/-/51422",
        "http://arnetminer.org/person/-/224202",
        "http://arnetminer.org/person/nada-matic-107206.html"
        "http://arnetminer.org/person/vladimir-vapnik-125753.html",
        "http://arnetminer.org/person/yongjian-fu-389775.html",
        "http://arnetminer.org/person/-/67688",
        "http://arnetminer.org/person/surnjani-djoko-995485.html",
        "http://arnetminer.org/person/diane-j-cook-823144.html",
        "http://arnetminer.org/person/-/302453",
        #missing A. Inkeri  Verkarno
        "http://arnetminer.org/person/-/411731"
        "http://arnetminer.org/person/kim-swarm-311854.html"
        "http://arnetminer.org/person/robert-zembowicz-609825.html",
        "http://arnetminer.org/person/jan-m-zytkow-124235.html",
        "http://arnetminer.org/person/-/1440447",
        "http://arnetminer.org/person/-/484391",
        "http://arnetminer.org/person/martin-l-kersten-759951.html",
        "http://arnetminer.org/person/-/1532438",
        "http://arnetminer.org/person/ryszard-s-michalski-372666.html",
        "http://arnetminer.org/person/-/1231010",
        "http://arnetminer.org/person/-/1326659",
        "http://arnetminer.org/person/luc-dehaspe-566186.html",
        "http://arnetminer.org/person/luc-de-raedt-487936.html",
        "http://arnetminer.org/person/jean-daniel-zucker-365228.html",
        "http://arnetminer.org/person/j-thomas-964440.html",
        "http://arnetminer.org/person/geber-ramalho-987367.html",
        "http://arnetminer.org/person/-/15985",
        "http://arnetminer.org/person/david-a-bell-327563.html",
        "http://arnetminer.org/person/john-g-hughes-8020.html",
        "http://arnetminer.org/person/-/1327350",
        "http://arnetminer.org/person/terence-m-barron-839645.html",
        "http://arnetminer.org/person/veda-c-storey-1388919.html",
        "http://arnetminer.org/person/-/128231",
        "http://arnetminer.org/person/nick-cercone-10306.html",
        "http://arnetminer.org/person/jinshi-xie-1378457.html",
        "http://arnetminer.org/person/-/476448",
        "http://arnetminer.org/person/wei-min-shen-184764.html",
        "http://arnetminer.org/person/bharat-g-mitbander-435637.html",
        "http://arnetminer.org/person/kayliang-ong-1432951.html",
        "http://arnetminer.org/person/-/402337",
        "http://arnetminer.org/person/foster-j-provost-976323.html",
        "http://arnetminer.org/person/-/129885",
        "http://arnetminer.org/person/james-clifford-226237.html",
        "http://arnetminer.org/person/-/1437233",
        "http://arnetminer.org/person/-/98703",
        "http://arnetminer.org/person/robin-d-burke-844235.html",
        "http://arnetminer.org/person/kathryn-schmitt-206378.html",
        "http://arnetminer.org/person/-/239907",
        "http://arnetminer.org/person/r-s-mitchell-801745.html",
        "http://arnetminer.org/person/l-a-smith-399427.html",
        "http://arnetminer.org/person/g-holmes-470232.html",
        "http://arnetminer.org/person/se-june-hong-511033.html", #Se June Hong not Hon
        "http://arnetminer.org/person/-/736242",
        "http://arnetminer.org/person/marek-j-druzdze-439653.html" #Another potential typo situation
        "http://arnetminer.org/person/-/12998",
        "http://arnetminer.org/person/-/167687",
        "http://arnetminer.org/person/-/696677",
        "http://arnetminer.org/person/raguram-sasisekharan-748003.html",
        "http://arnetminer.org/person/-/165976",
    ]

    def parse(self, response):
    	x= HtmlXPathSelector(response)
        
        titles = x.select("/html/body")
        items = []
        for titles in titles:
            item = ArnetItem()
            item ["Name"] = titles.select("//*[@id='contentZone']/div[1]/div[1]/h1/text()").extract()
            item ["Current_Title"] = titles.select("//*[@id='contentZone']/div[3]/dl/dd[1]/text()").extract()
            item ["Affiliation"] = titles.select("//*[@id='contentZone']/div[3]/dl/dd[2]/text()").extract()
            item ["Bio"] = titles.select("//*[@id='contentZone_0']/div[2]/p/text()").extract()
            item ["Education"] = titles.select("//*[@id='contentZone_1']/table/tr").extract()
            item ["Conferences"] = titles.select("//div[5]/div/div[2]/dl/dd/a[@class='label label-infox label-link']/text()").extract()
            items.append(item)
        return items