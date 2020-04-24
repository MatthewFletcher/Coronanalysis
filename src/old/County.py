class County:
    def __init__(self,fips):
        self.Name = ""
        self.State = ""
        self.fips = 0
        self.Cases = []
        with open ("../data/fips.csv", 'r') as f:
            counties = f.readlines()
            for line in counties:
                if line.startswith(str(fips)):
                   line = line.split(',')
                   self.fips = int(line[0])
                   self.Name = line[1]
                   self.State = line[2]

    def __repr__(self):
        return f"{self.fips} -- {self.Name} County, {self.State}"

