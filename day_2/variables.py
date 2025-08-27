import math
# Day 2: 30 Days of python programming

# 1

first_name = 'Etor'
last_name = 'Diaz'
full_name = 'Etor Diaz'
country = 'Catalonia'
city = 'Barcelona'
age = 35
year = 2025
is_married = True
is_true = False
is_light_on = False
is_bananas, is_oranges = True, False

# 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))

print('First name len', len(first_name))

print(len(first_name) > len(last_name))

num_one,num_two = 5,4

total = num_one + num_two

diff = num_two - num_one

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

radius = 30
area_of_circle = math.pi * radius ** 2

cirum_of_circle = 2 * math.pi * radius 

user_radius = int((input('Input radius: ')))
print('Area of circle: ', math.pi * user_radius ** 2)

user_first_name, user_last_name, user_country, user_age = input('First name: '), input('Last name: '), input('Country: '), input('Age: ')
print(user_first_name, user_last_name, user_country, user_age)

print(help('keywords'))
