if 5 > 2:
  print("Five is greater than two!")

#This is single line comment
#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
multiline coments
This is a comment
written in
more than just one line 
"""
print("Hello, World!")

kapil=["kapil","ram","hari"]
print(kapil)



thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = thislist.copy()
print(mylist)

x=10
print(type(x))


a=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(a[5])
if "kapil" in a:
  print("yes")
else:
  print("no")




def check_odd_even(number):
    """
    This function checks if a number is odd or even.
    
    Parameters:
    number (int): The number to be checked.
    
    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage
num = 7
result = check_odd_even(num)
print(f"The number {num} is {result}.")


""""
a=input("enter number:")
a=int(a)
if a%2==0:
   print("even :",a)
else:
   print("odd :",a)
   
   """

"""
a=4
b=8
print(a & b)
"""
"""names={"ram","hari","gita"}
for name in names:
   print(name)"""

students={"ram":20,"hari":100,"gita":400,"santosh":900}
for student in students:
   print(students)

app=["x","y","Z"]
if "ram" in app:
   print ("yes")
else:
   print("no")


   a=range(1, 5)
   a=list(a)
   print(a)
   print(a[1])



   collection=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   for i in collection:
      print(i)


#lamda function in python
#Syntax: lambda arguments : expression
"""convert string  lower case into upper case"""
str1 = 'kapil'
upper = lambda string: string.upper()
print(upper(str1))


number=[12,34,56]
mul=[x*3 for x in number]
print(mul)

is_even_list = [lambda arg=x: arg * 10 for x in range(1,4)]
#print(is_even_list)
for item in is_even_list:
	print(item())

people = [13, 90, 17, 59, 21, 60, 5]
adult = list(filter(lambda age: age > 18, people))
print(adult)
#adults = list(map(lambda age: age > 18, people))
#print(adults)


numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(list(even_numbers))
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
#print(list(squares))
print(squares)

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "Boston"
}

# Accessing values
print(person["name"])  # Output: John

# Adding a new key-value pair
person["email"] = "john@example.com"

# Updating an existing value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Checking if a key exists
if "email" in person:
    print("Email is present")

# Iterating through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")



#map and filter

