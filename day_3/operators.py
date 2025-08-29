import math

age = 35
height = 82.5
complex = 2j - 1

base = input("Enter base: ")
height = input("Enter height: ")

area = (int(base) * int(height)) / 2
print("The area of the triangle is ", int(area))

side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")

perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is ", perimeter)

length, width = input("Enter length: "), input("Enter width: ")
rect_area = int(length) * int(width)
rect_perim = 2 * (int(length) + int(width))

print("The area of the rectangle is ", rect_area, " and the perimeter is ", rect_perim)

radius = input("Enter radius: ")
circle_area = math.pi * (int(radius) ** int(radius))
circle_circum = math.pi * 2 * float(radius)
print("The area of the circle is ", area, " and the circumference is ", circle_circum)


# y = 2x - 2
slope = 2
x_intercept = 1
y_intercept = 2

len('python') != len('dragon')

clause1 = 'on' in 'python'
clause2 = 'on' in 'dragon'
print(clause1, clause2)

clause3 = "jargon" in "I hope this course is not full of jargon"
print(clause3)

clause4 = not(clause1 and clause2)

print(str(float(len('python'))))

print('2 is even?', 2%2 == 0)
print('3 is even?', 3%2 == 0)

print('floor division of 7 by 3 is 2.7? ', 7 // 3 == int(2.7))

print('type `10` equals 10 ', type('10') == type(10))

print('int(`9.8`) equals 10 ', int(9.8) == 10)

hours, rate = input('Enter hours: '), input('Enter rate per hour: ')
print('your weakly earning is ', int(hours) * int(rate))

years_lived = input('Enter number of years you have lived: ')
print('You have lived for ', int(years_lived) * 365 * 24 * 60 * 60 , ' seconds') 

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')

