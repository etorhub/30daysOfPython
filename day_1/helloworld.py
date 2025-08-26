# 1. check python version
import sys
print("Python version: " + sys.version)

# 2. Operations
print("Addition: " + str(3 + 4))
print("Subtraction: " + str(3 - 4))
print("Multiplication: " + str(3 * 4))
print("Modulus: " + str(3 % 4))
print("Division: " + str(3 / 4))
print("Exponentiation: " + str(3 ** 4))
print("Floor division: " + str(3 // 4))

# 3. Strings

print("My name is Etor")
print("My family name is Diaz Acha")
print("My country is Catalonia")
print("I am enjoying 30 days of python")

# Check data types

print("Type of 10: " + str(type(10)))
print("Type of 9.8: " + str(type(9.8)))
print("Type of 3.14: " + str(type(3.14)))
print("Type of 4 - 4j: " + str(type(4 - 4j)))
print("Type of ['Asabeneh', 'Python', 'Finland']: " + str(type(['Asabeneh', 'Python', 'Finland'])))
print("Type of 'Etor': " + str(type("Etor")))

# More data types

print("Type of boolean: " + str(type(True)))
print("Type of list: " + str(type([])))
print("Type of tuple: " + str(type(())))
print("Type of set: " + str(type(set())))
print("Type of dict: " + str(type({})))

# Euclidian distances

print("Euclidian distance between (2, 3) and (4, 5): " + 
  str(((4 - 2) ** 2 + (5 - 3) ** 2) ** 0.5)
)