# Create a function called convert() that:

# Takes two parameters: value and unit

# If unit is "cm", convert to meters

# If unit is "kg", convert to grams

# If unit is "inch", convert to feet

def convert(value,unit):
    if unit == 'cm':
        result = value/100
        print(f'{result} m')
    elif unit == 'kg':
        result = value*1000
        print(f'{result} g')
    elif unit == 'inch':
        result = value/12
        print(f'{result} feet')

convert(100, "cm")
convert(5, "kg")
convert(24, "inch")