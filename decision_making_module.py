from __future__ import division
from elasticsearch import Elasticsearch
from pprint import pprint as pp
import requests
import sys
from slipstream.api import Api
import lib_access as la
import server3 as srv3
import math

api = Api()
index = 'sar'
type = 'offer-cloud'

server_host = 'localhost'
res = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def get_price(ids, time):
    mapper_unit_price = float(api.cimi_get(ids[0]).json['price:unitCost'])
    reducer_unit_price = float(api.cimi_get(ids[1]).json['price:unitCost'])
    if api.cimi_get(ids[0]).json['price:billingPeriodCode'] == 'HUR' :
      time = math.ceil(time / 3600)
    else:
      time = time/ 3600
    cost = time * (mapper_unit_price + reducer_unit_price)

    return(cost)
def query_db(cloud, time, offer):
    query = { "query":{
          "range" : {
               "%s.execution_time" % offer: {
                      "lte": time,
                      "gt": 900
                       }
                     }
             }
          }
    return(res.get(index=index,doc_type=type,id=cloud))

''' decision making moduke

  : inputs    cloud, offer, time

  : query the document of according clouds for records with execution time equal
    or less than the input time
  : from th

'''

def dmm(cloud, time, offer, ss_username, ss_password):
    api.login(ss_username, ss_password)
    ranking = []
    for c in cloud:
        rep = query_db(c, time, offer)
        pp(rep['_source']['CannedOffer_1'])
        if rep['found']:
            specs = srv3._format_specs(rep['_source'][offer]['components'])
            time  = rep['_source'][offer]['execution_time']
            serviceOffers = srv3._components_service_offers(c, specs)
            mapper_so =  serviceOffers['mapper']
            reducer_so =  serviceOffers['reducer']
            cost = get_price([mapper_so, reducer_so], time)
            print c
        ranking.append([c, mapper_so, reducer_so, cost, time ])
    return sorted(ranking, key=lambda x:x[3])

if __name__ == '__main__':
    cloud=['ec2-eu-west']
    time = 1000
    offer = '1'
    dmm(cloud, time, offer, ss_username, ss_password)
