## ================ 1) Truthy and Falsy values ================
# What prints
if 100:
    print('this prints')

if 'apple':
    print('this prints')

if [1, 2, 3]:
    print('this prints')

if {'apple':1, 'orange':2}:
    print('this prints')

# What does not prints
if 0:
  print('this will not print')

if '':
  print('this will not print')

if []:
  print('this will not print')

if {}:
  print('this will not print')

if None:
  print('this will not print')



## ================ 2) Using bool() to check for truthy/falsy values ================
print(bool(10))          # True
print(bool('apple'))     # True
print(bool([1, 2, 3]))   # True
print(bool({1:2, 3:4}))  # True
print(bool(object()))    # True

print(bool(0))           # False
print(bool(''))          # False
print(bool([]))          # False
print(bool({}))          # False
print(bool(None))        # False



## ================ 3) any() and all() ================
print(all([True, True, True]))    # True
print(all([True, True, False]))   # False

print(any([True, True, False]))   # True
print(any([False, False, False])) # False


## ================ 4) The meaning of ‘x or 100’ ================
a = x or 100
# What x or 100 means:
#   if x is None, x or 100 takes the default value 100
#   if x is not None, x or 100 takes the original value of x

def get_fruit() -> str | None:
    # might return a fruit or None

fruit = get_fruit()  # this might be some fruit, or None

fruit = fruit or 'apple'
# if fruit is not None, no changes
# if fruit is None, fruit = 'apple'

print(fruit)

# The line fruit = fruit or 'apple' ensures that fruit will be a string.
#   if get_fruit() returns a string, nothing changes
#   if get_fruit() returns None, fruit is auto reassigned to 'apple'



