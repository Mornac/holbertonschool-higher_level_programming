# Python - Everything is object #  
## 📂 Introduction  
This post is designed to help learn Python and understand the vocabulary commonly used. In this blog, I present codes examples and their outputs to illustrate key concepts covered in my project : 
- id() and type()
- mutable objects
- immutable objects
- why does it matter and how differently does Python treat mutable and immutable objects
- how arguments are passed to functions and what does that imply for mutable and immutable objects
- Python: Everything is object - Global example

## 📂 Id() and type()  
Id() returns the unique identifier of an object, which is its memory address in the CPython implementation.
It's used to uniquely identify object in memory.
Type() is used to determinate the type of the object : integer, float, string, boolean, tuple, list, dict, set, bytes, frozenset and bytearray.

```python
Example with id()
a = 5
print(id(a))

Output (memory address)
134132579320520
```

```python
Example with type()
a = int(1)
b = float(3.14)
c = str("Hello")
d = bool(a)
e = (a, b)

Output
1
3.14
Hello
True
(1, 3.14)
```

## 📂 Mutable objects
A mutable object is an object that can be modified after it's created: list, dict, set and bytearray.

```python
Example of mutable object
a = [1, 2, 3]
a.append(4)
print(a)

Output
[1, 2, 3, 4]
```

## 📂 Immutable objects
An immutable object is an object that can't be modified: integer, float, string, boolean, tuple, frozenset and bytes.

```python
Example of immutable object
a = "Holberton"
a = a + "School"
print(a)
 
Output
(a new string is created, the original is not modified)
HolbertonSchool
 ```

 ## 📂 Why does it matter and how differently does Python treat mutable and immutable objects
Arguments can be passed to Python functions either by reference or by value.
It influences performance and memory usage.
Immutable objects are safe from side effects in functions: this is good for data integrity.
Mutable objects can be modified through references, which can be risky if not handled whith care.

 ## 📂 how arguments are passed to functions and what does that imply for mutable and immutable objects
Arguments in Python are passed to functions by object reference, called pass-by-assignment or pass-by-object-sharing.
This means that functions receive a reference to the original object, not a copy.
However, whether the object can be modified inside the function depends on whether it is mutable or immutable :  
. mutable object can be changed inside the function  
. immutable object can't be changed inside the function, creates a new object instead

## 📂 Python: Everything is object - Global example
```python
# Menu
pizzaName = "Margarita"                          # string object
price = 10.50                                    # float object
ingredients = ["tomato", "mozarella", "oregano"] # list object
isVegetarian = True                              # boolean object

print("🍕 Pizza name:", pizzaName)
print("Type:", type(pizzaName))                  # type()
print("ID:", id(pizzaName))                      # id()

print("💰 Price:", price)
print("Type:", type(price))
print("ID:", id(price))  

print("IsVegetarian:", isVegetarian)
print("Type:", type(isVegetarian))
print("ID:", id(isVegetarian)) 

print("Ingredients:", ingredients)
print("Type:", type(ingredients))
print("ID:", id(ingredients))   

print("Adding 'olives' to ingredients")
ingredients.append("olives")                    # mutable object
print("Ingredients:", ingredients)
print("Type:", type(ingredients))
print("ID:", id(ingredients))   

print("Changing pizza name:", pizzaName)
pizzaName += " (Small)"                         # immutable object
print("New pizza name:", pizzaName)
print("ID after modification:", id(pizzaName))

menu = {                                        # dict object
    "Margarita": 10.5,
    "Veggie": 11,
    "Special": 11.5
}
print("📋 Menu:", menu)
print("Type:", type(menu))
print("ID:", id(menu))   

Output
🍕 Pizza name: Margarita
Type: <class 'str'>
ID: 135514128636528  

💰 Price: 10.5
Type: <class 'float'>
ID: 135514130008208  

IsVegetarian: True
Type: <class 'bool'>
ID: 135514141648320  

Ingredients: ['tomato', 'mozarella', 'oregano']
Type: <class 'list'>
ID: 135514131843520  

Adding 'olives' to ingredients
Ingredients: ['tomato', 'mozarella', 'oregano', 'olives']
Type: <class 'list'>
ID: 135514131843520  

Changing pizza name: Margarita
New pizza name: Margarita (Small)
ID after modification: 135514128638576  

📋 Menu: {'Margarita': 10.5, 'Veggie': 11, 'Special': 11.5}
Type: <class 'dict'>
ID: 135514128646080  
```
