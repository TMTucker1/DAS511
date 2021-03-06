# -*- coding: utf-8 -*-
"""OneHourPython (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i2ICUN74cV3ThXFHG36vcSGOAZ2POqLS

# One Hour Python

This is not a class in Python, but I do offer a lot of examples and code within Python through Jupyter Notebooks.  Being able to open and run the notebooks will prove very useful.  None of the material in this module will be on any test or homework, but I highly encourage you to spend 1-2 hours playing with this code, editing it, running it.  Google it if you need to.  Knowing how to run Python code and having a very basic idea how to edit the code I provide will be helpful all quarter.

Now lets learn some Python!!

### Running cells

Jupyter notebook has 2 kinds of cells Markdown Cells, which are text based and do **not** run code, and code cells.  In either case if you click "shift+enter" while in a cell you will run the contents of that cell.

### Importing Python Libraries

Before you can use packages in Python you need to import them.  See the Powerpoint slides to learn how to install these in Anaconda Navigator
"""

import statistics as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

"""
### Importing .csv files

A lot of the work you will be doing in data analytics revolves around .... data.  I am going to show you an easy way to import a .csv file.

First and this is **super*** important.  <font color = red> You need to ensure the .csv file is in the same folder as the folder your python code is saved in. </font>  Then run the following code:

**Replace 'CommuteTimes.csv' with the filename you are trying to open.**"""

from google.colab import files
files.upload()

accessData = pd.read_csv('CommuteTimes.csv', delimiter=',', header = 0)

"""You may be interested to see what a few rows of this table looks like.  To do that you can use the following: """

accessData.head()

"""#### You can select columns to refine your view of the data"""

accessData_filtered = pd.read_csv('CommuteTimes.csv', usecols = {"City", "Time_minutes"})
accessData_filtered.head()

"""#### You can generate descriptive statistics on numeric columns in the DataFrame"""

accessData.describe()

"""### Strings
A string is a collection of characters. Strings can be created with either single quotes (???) or double quotes (???). There is no differences. If the text is more than one line, you need to use triple quotes (????????? or ?????????)

You can assign string values to a variable name
"""

a = 'apple'

print(a)

b = "banana"

print(b)

"""You can concatenate strings (smoosh them together), note no space!"""

c=a+b

print(c)

"""You can get a space, but you need to add it manually."""

c=a+" "+b
print(c)

"""You can repeat a string"""

a*5

"""### Slicing 
Python supports strings indexing and slicing. <br>
**Indexing** means each character has its own index. <br>
**Slicing** means to extract a contiguous piece of a string. <br>

**Python uses zero index!!** The first index starts from 0 instead of 1. 
"""

a[0]

"""You can even index in from the end of a string by using negative indexes!"""

a[-1]

"""You can use a ":" (colon) to slice a section of string.  Note that the end index is **not** included in the slice."""

a[0:3]

"""You can also slice from the start of a string to a specific point, or from some specific point to the end."""

a[:3]

a[3:]

"""### Functions
Each type of object in Python has lots (and lots) of built in functions.  Knowing some of these will help you.

# New Section
"""

len(a)

type(a)

"""### Methods
1. string.split(maxsplit) ??? create a list from characters in a string
2. maxsplit argument ??? defines how many times you want to split the string
"""

str = 'I am learning Python'

# split the string using spaces
str.split(' ')

# split the string using spaces, maximum of 2 times
str.split(' ', maxsplit = 2)

"""### Numbers
Python has integers and floats.<br>
Python can do lots of math without any packages installed
"""

a=3.9
type (a)

"""Note that turning a float into an integer is **not** the same thing as rounding!"""

int(a)

"""round(float, # decimals)"""

round(a,0)

"""If you'd like to represent the rounded value of a as an integer,"""

int(round(a,0))

3+2

3*3

"""Exponents are a tad odd.  4^2 needs to be written as $4**2$.  The '^' operator does bitwise comparisions, which is way outside scope of this class.  """

#Not the way to write 4 squared
4^2

#This is the way
4**2

4/2

5/2

"""Example of floor divison"""

5//2

a=-5.2

"""Example of modulo operator that generates the remainder of a division calculation"""

5%2

abs(a)

"""### Lists
Python can save a group of objectives together. This is called a list. A list will be hold by square brackets [ ]. A list can hold numeric, string and list data together. <br>

Lists are mutable - They can be changed
"""

mylist = [1, 2, 3, 4, 5, 6]

"""You can have odd lists too:"""

oddlist = ['apple pie', [1,2], 'ice cream']

"""You can index and slice lists, just like above with strings"""

mylist[1]

oddlist[0]

oddlist[1]

mylist[1:3]

"""You can change values of lists, one element at a time!"""

mylist[1] = 3.14

mylist

"""Python has several build in methods to provide information about your list"""

len(mylist)

max(mylist)

min(mylist)

"""You can grow lists"""

mylist.append('horse')

mylist

"""You can insert a new element where ever you want<br>
*list.insert(index, new element value)*
"""

mylist.insert(3, 100)

mylist

"""You can delete a value from the list, note this only deletes first occurance"""

mylist.remove(4)

mylist

"""*list.pop(index)* ??? return the element based on the index provided and remove it from a list"""

mylist.pop(2)


mylist

mylist.sort()

mylist

"""Above failed because Python doesn't know how to sort 'horse', when everythiong else is a number.  It can sort by value or alphabetoically but not mixed.  Lets 'pop' horse and try again"""

mylist.pop(5)

mylist

mylist.sort()

mylist

"""### Tuples 
A tuple is very similar to list, except that it is immutable. Once a tuple is created, it cannot be modified. Tuples are useful because of the following reasons:

1. faster than lists
2. protect the data since it is immutable
3. there are some situations where tuples are required (e.g. keys on dictionaries)

Tuples are created by listing several values. You can use () to surround the values, but it is optional. () is only required when you create an empty or one element tuple. If you want to create a tuple with only 1 element, add a comma (,) after it.
"""

mytuple = 1, 2, 3

mytuple + (7,)
(1, 2, 3, 7)

len(mytuple)

max(mytuple)

"""What!!  I thought I added '7' to mytuple! <br>
Nope, tuples are immutable.  You just concatanted a 7  
"""

min(mytuple)

"""### Dictionaries
**Definition & Creation** <br>
A dictionary is like a map. You have keys paired with values.<br>
To create a dictionary, use {} <br>
Use colon ":" to connect between keys and values. **Keys must be unique, and immutable, which mean they cannot be lists.** <br>
*mydict = {key1: value1, key2: value2}*
"""

dict = {'a': 'apple', 'b': 'banana'}

""""a" and "b" are my keys. These keys are connected to the values "apple" and "banana"."""

dict['a']

"""Dictonary keys are immutable (i.e. you cannot change the "a", however you can change the value associated with a key."""

dict['a'] = 'appricot'

dict['a']

"""You can grow a dictonary by adding new key:value pairs"""

dict['c'] = 'carrot'

dict

"""There are a few built in dictonary methods which may be useful <br>
dict.keys() ??? return list of dictionary???s keys <br>
dict.values() ??? return list of dictionary???s values <br>
dict.items() ??? return a list of dictionary???s (key, value) tuple pairs <br>
dict.clear ??? remove all elements of a dictionary <br>
dict.get(key, default = None) ??? return the value paired with the key argument if the key exists, return None or other value if key is not in dictionary
"""

dict.get('a')

dict.get('d', "error")

"""### If then statements
This is where alot of the real power of coding starts to appear. <br>
if expression: <br>
&nbsp; &nbsp; &nbsp; statement <br>
 elif expression: # short for else if <br>
&nbsp; &nbsp; &nbsp; statement <br>
 else: <br>
&nbsp; &nbsp; &nbsp; statement <br>

**Logical operators** <br>
and ??? overall statement is true if *all* statements are true <br>
or ??? overall statement is true if *one* statement is true <br>
"""

a = 5
b = 7

if a > b:
    print("Small numbers rule!")
else:
    print("Large numbers rule!")

"""### for loops
for loops iterate over all the values in a sequence (lists, strings, dictonaries, tuples). <br>
**This is very powerful** <br>

One of the most common things you will see are data analysts cleaning data and turning the information from a spreadhseet into a list, or a dictonary.  Then using for loops to do things.   <br>

*for name_whatever_you_want in sequence: <br>
&nbsp; &nbsp; statements*
"""

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

for i in range(len(x)):
        print(x[i] * y[i])

"""Examining the workings of the for loop ..."""

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

loop_results = np.zeros([4, 4])

for i in range(len(x)):
    z = (i, x[i], y[i], x[i] * y[i])
    loop_results[i, :] = z    
    
loop_results

dict

for key in dict:
    print(key)

for key in dict:
    print(dict[key])