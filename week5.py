def describe_city(name, country='egypt'):
    print(f"{name} is in {country}")
describe_city(country='helwan',name= "cairo")
def prod_num(*numbers):
    s=0 
    for x in numbers:
        s+=x
    return s 
s= prod_num(8,9,2,3,4,5,6,7,8,9,8,6,5,4,44,4,4,4,4,4,4)
print(s)

def describe_country(country, *cities):
    if len(cities) == 1:
        print(f"{cities[0]} is in {country}.")
    else:
        cities_str = ", ".join(cities)
        print(f"{cities_str} are in {country}.")

# Example usage
describe_country("England", "Liverpool", "Manchester", "London")
# Output: Liverpool, Manchester, London are in England.

describe_country("England", "Liverpool")
# Output: Liverpool is in England.

import json
fav_num= input ("what is you fav number?")
with open ('new_file.text', 'w') as f:
    json.dump(fav_num,f )
import json
with open ('new_file.text','r') as f:
    fav_num = json.load(f)
print(fav_num)

