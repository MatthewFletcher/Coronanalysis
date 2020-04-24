import requests
import json
import datetime as dt

import matplotlib.pyplot as plt

class Parser:

    def __init__(self):
        self.url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
        self.filename = '../data/us-counties.csv'
        self.jsonfile = '../data/us-counties.json'
        self.data = {}
        
        #Get data from json file
        self.loadData() 
    
    def loadData(self):
        with open(self.jsonfile, 'r') as f:
            self.data = json.load(f)
            for key in self.data.keys():
            

    def downloadData(self):
        r = requests.get(self.url)
        with open(self.filename, 'wb') as f:
            f.write(r.content)
        with open(self.filename, 'r') as f:
            f.readline()
            for line in f:
                line = line.replace('\n','').split(',')
                if line[3] not in self.data.keys():
                    self.data[line[3]] = {'county': line[1], 'state': line[2], 'data': []}
                self.data[line[3]]['data'].append({'date':
                    line[0], 'cases': line[4], 'deaths': line[5]})

    def json_serial(self, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, (dt.datetime, dt.date)):
            return dt.date.strftime(obj, '%Y-%m-%d')
        raise TypeError ("Type %s not serializable" % type(obj))

    def parsetojson(self):
            with open(self.jsonfile, 'w') as fp:
                json.dump(self.data, fp, default=self.json_serial)

    def updateData(self):
        self.downloadData()
        self.parsetojson()

    def plotCounty(self, fips):
        countydata = [d for d in self.data[fips]['data']]
        dates,cases, deaths = zip(*[(d['date'], d['cases'], d['deaths']) for d in countydata])
        plt.plot(dates, cases)
 
