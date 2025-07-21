# ✅ Tasks:
# Create a list fav_bikes with at least 5 bike names.

# Add a new bike, remove one, and replace one with another.

# Print all bikes using a loop.

# fav_bikes = ['KTM','HIMALAYAN','SPLENDOR','RX100','PULSAR']
# fav_bikes.pop()
# fav_bikes.append('BULLET')
# fav_bikes[1]='XPULSE'

# for i in fav_bikes:
#     print(i)

############################################

# ✅ Tasks:
# Create a dictionary bike_specs with keys: brand, model, cc, mileage.

# Print each key and value using a loop.

# Add a new key year and update mileage.

##################################

# bike_specs  = {'brand' : 'yamaha', 'model':1996,'cc':97.2,'mileage':65 }

# for i in bike_specs.values():
#     print(i)

# bike_specs['year'] = 2003
# bike_specs['mileage']=26

# for i in bike_specs.values():
#     print(i)

#######################

#     ✅ Tasks:
# Create a set of bike accessories (helmet, gloves, jacket, gloves)

# Show the set (should not have duplicates).

# Add a new item and remove an existing one.

# bike_accessories = {'helmet','gloves','jacket','gloves'}
# bike_accessories.add('Mirror')
# bike_accessories.remove('helmet')

# for i in bike_accessories:
#     print(i)

###########################################

# ✅ Tasks:
# Create a tuple garage_location with (your city, pin code).

# Print the city and pincode from the tuple.

# Try changing one value — observe what error appears.

# garage_location = ('Kannur',670678)
# print(garage_location)

################################################

# 🛠️ Bike Garage Manager
# Create a dictionary where:

# Keys are bike names

# Values are another dictionary with keys: model, cc, year

# Add 2–3 bikes

# Print each bike’s full details in a nice format

bikes = {
    'splendor': {'model':1986,'cc':97.2,'year':2003},
    'xpulse' : {'model':2021,'cc':210,'year':2024},
    'himalayan' : {'model':2024,'cc':450,'year':2025},
    }

print(bikes['splendor'])

for i in bikes['xpulse'].values():
    print(i)