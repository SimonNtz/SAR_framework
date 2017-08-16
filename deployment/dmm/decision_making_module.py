from __future__ import division
from elasticsearch import Elasticsearch
from pprint import pprint as pp
import requests
import sys
from slipstream.api import Api
import lib_access as la
import server_dmm as srv_dmm
import summarizer as summ
import math

api = Api()
index = 'sar'
type = 'eo-proc'

server_host = 'localhost'
res = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def query_db(cloud, time, offer):
    query = { "query":{
          "range" : {
               "%s.execution_time" % offer: {
                      "gte": 0,
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
        if rep['_source']:
            pp(rep['_source']['CannedOffer_1'])
            past_time = rep['_source'][offer]['time_records']
            ratio = math.ceil(float(time/past_time))
            print "RATIO:" + str(ratio)
            specs = srv_dmm._format_specs(rep['_source'][offer]['components'])
            specs['mapper'] = ratio * specs['mapper']
            serviceOffers = srv_dmm._components_service_offers(c, specs)
            mapper_so =  serviceOffers['mapper']
            reducer_so =  serviceOffers['reducer']
            cost = summ.get_price([mapper_so, reducer_so], time)
            ranking.append([c,
                            mapper_so,
                            ,reducer_so,
                             str(cost) + "EUR",
                             str(time) + "sec",
                             specs ])
    return sorted(ranking, key=lambda x:x[3])

if __name__ == '__main__':
    cloud=['ec2-eu-west']
    time = 1000
    offer = '1'
    dmm(cloud, time, offer, ss_username, ss_password)
