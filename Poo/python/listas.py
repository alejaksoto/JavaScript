"""listas """
dic_dogs_ages = {
    'toti' : 3,
    'doby' : 1,
    'capi' : 2,
}

print(f'age\tname')

for age, name in dic_dogs_ages.items():
    print(age, name)
