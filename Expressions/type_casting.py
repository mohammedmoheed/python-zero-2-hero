# type casting is changing the data type of any variable

a = '123'  # it is an string
b = '12a'  # it is an string

print(type(a))


a = int(a)
x = float(a)
print(type(a)) # here string converted to integer
print(type(x))

b = int(b) # it cant be converted into string


