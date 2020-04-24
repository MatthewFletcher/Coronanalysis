import csv
import datetime as dt
from County import County

import matplotlib.pyplot as plt


class Parser:
    def __init__(self, fn='../data/us-counties.csv'):
        self.counties = {}
        with open (fn, 'r') as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                f = row['fips']
                if f not in self.counties:
                    self.counties[f] = {'County': County(f['fips']), 'data':[]}
                self.counties[f]['data'].append({'date':
                    self.parseDate(row['date']),'casect':row['cases'], 'death': row['deaths']})



    def parseDate(self, s):
        '''
        Returns the datetime object corresponding to the given date
        '''
        return dt.datetime.strptime(s, '%Y-%m-%d')

    def printData(self):
        for row in self.data:
            print(row)
    
    def plotData(self, fips):
        fips  = str(fips)
        countyInfo = self.counties[fips]
        print(data)
        plt.title(f"{data[name]} County")
        plt.show()
