import wbdata
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

x = wbdata.get_data("FP.CPI.TOTL")
pp.pprint(x[0])
# sources = wbdata.get_source(display=False)
# indicators = wbdata.get_indicator(source=sources[0]['id'], display=False)
# pp.pprint(indicators[0])
# print 
# sources[0]['id']