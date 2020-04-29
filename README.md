To use:

Must have matplotlib installed. 

Pull up a Python terminal (I use iPython). 

```python
#Import Parser
from Parser import Parser

#Create instance of parser class
p = Parser()

#Plot by FIPS code
#If you do not know your counties FIPS code,
# look in data/fips.csv

p.plotCounty('37037')

#Default plotCounty plots deaths. 
#To plot cases, use a 'c' specifier. 
p.plotCounty('37037', 'd')

#Only valid specifiers are 'c' and 'd', all others will throw error.

```

