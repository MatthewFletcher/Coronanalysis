def parsetojson():
    fn = '../data/us-counties.csv'
    d = {}
    with open(fn, 'r') as f:
        for line in f:
            line = line.replace('\n','').split(',')
            if line[3] not in d.keys():
                d[line[3]] = {'county': line[1], 'state': line[2], 'data': []}
            d[line[3]]['data'].append({'date': line[0], 'cases': line[4], 'deaths': line[5]})
        with open('us-counties.json', 'w') as fp:
            json.dump(d, fp)


