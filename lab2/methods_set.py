#Add an element to the fruits set:

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#Remove all elements from the fruits set:

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#Copy the fruits set:

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#Remove the items that exist in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

#Remove "banana" from the set:

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

#Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Remove the items that is not present in both x and y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#Return True if all items in set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

#Remove a random item from the set:

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#Remove "banana" from the set:

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)

#Return a set that contains all items from both sets, except items that are present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Remove the items that are present in both sets, AND insert the items that is not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

#Insert the items from set y into set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
