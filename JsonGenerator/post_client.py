import csv
import json
import os
import random
import sys
import time
from time import gmtime, strftime

import jinja2
import requests
from azure.eventhub import EventData, EventHubProducerClient
from azure.eventhub.aio import EventHubProducerClient

'''
header = dict()
header['referringId'] = randomdata.referringId
header['partnerOrderId'] = "s1284"

order = dict()
order['header'] = header

body = dict()
body['order'] = order



jstr = json.dumps(body, sort_keys=True, indent=2))

requests.post(body)
'''
#import ggps

VERSION = 'v20170323a'

# Get environment variables


# Set envrioment variables
ehcstr="<connection_string>"
eventhub_name="<eventhub name>"

def print_options(msg):
    print(msg)
    # arguments = docopt(__doc__, version=VERSION)
    # print(arguments)

def read_csv_file(infile):
    csv_rows = list()
    with open(infile, 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            csv_rows.append(row)
    return csv_rows


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname (__file__)), 
    autoescape=True)
template = jinja_env.get_template("templates/hon_tmpl.json")

if __name__ == "__main__":

    start_time = time.time()
    if len(sys.argv) > 2:
        func  = sys.argv[1].lower()
        count = int(sys.argv[2])

        if func == 'test':
            infile = 'data/order_data.csv'
            rows = read_csv_file(infile)
            print("{} rows read from file {}".format(len(rows), infile))
            # Eventhub producer
            producer = EventHubProducerClient.from_connection_string(conn_str=ehcstr, eventhub_name=eventhub_name)

            for idx, row in enumerate(rows):
                if idx < count:
                    time.sleep(0.5)
                    values = dict()             # Jinga will merge these values into the template
                    values['orderTime'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    values['mRID'] = row['mRID']  # 
                    values['createDatetime'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    values['start'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    time.sleep(3)
                    values['end'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    values['businessType'] = row['businessType']
                    values['curveType'] = row['curveType']
                    values['measurement_Unit_name'] = row['measurement_Unit_name']
                    values ['codingScheme'] = row ['codingScheme']   
                    values ['out_Quantity_quantity'] = row ['out_Quantity_quantity']
                    values ['out_Quantity_quality'] = row ['out_Quantity_quality']   
                    values['name'] = row ['name']
                    values['resolution'] = row['resolution']

                  					
                    jstr = template.render(values)
                    jstr.encode('utf-8')
                    
                    print(jstr)

                    # Add events to the batch.
                    event_data_batch = producer.create_batch()
                    event_data_batch.add(EventData(jstr))
                    producer.send_batch(event_data_batch)
                         

                   # headers = {'Content-type':'application/json','Ocp-Apim-Subscription-Key':'53436f0d75fd496c81e092e5d2a0c68a','Ocp-Apim-Trace':'true'}
                    #commented this out on 4-6-2021
                    
                    # r=requests.post(url,jstr,headers=headers)
                    #print (r.status_code)
                    #
                    #print (str(r.text))

# Close the producer.    
producer.close()
