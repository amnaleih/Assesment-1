rivers = {
    'nile river': 'Egypt',
    'mississippi river': 'United States of America',
    'mekong river': 'Myanmmar',
    'yukon river ': 'Alaska',
    'yangtze river': 'China',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows throughout the {country.title()}.")

print("\nThe following rivers are included in this type of data sets:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries of this rivers are included in this type of data sets:")
for country in rivers.values():
    print(f"- {country.title()}")