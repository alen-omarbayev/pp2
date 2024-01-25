#Add an element to the fruits list:

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")


#Remove all elements from the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()


#Copy the fruits list:

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()


#Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")


#Add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)


#What is the position of the value "cherry":

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")


#Insert the value "orange" as the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")


#Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)



#Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")


#Reverse the order of the fruit list:

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()


#cars = ['Ford', 'BMW', 'Volvo']

cars.sort()


#Sort the list descending:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)


#Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)


#Sort a list of dictionaries based on the "year" value of the dictionaries:

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)


#Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

