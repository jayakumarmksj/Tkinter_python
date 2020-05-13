
from covid import Covid
covid=Covid(source='worldometers')
#data=covid.get_data()
data=covid.get_status_by_country_name('India')
print("Covid 19 Cases:")
for k in data:
    print(k,data[k])
 
""" 
for states wide data  use this

from covid_india import states
print(states.getdata())

for specific state wide data  use this
print(states.getdata('state_name'))


"""
