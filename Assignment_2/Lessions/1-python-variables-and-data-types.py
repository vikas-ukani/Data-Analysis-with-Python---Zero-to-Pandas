#!/usr/bin/env python
# coding: utf-8

# # A Quick Tour of Variables and Data Types in Python
# 
# ### Part 2 of "A Gentle Introduction to Programming with Python"
# 
# This tutorial is the second in a series on introduction to programming using the Python language. These tutorials take a practical coding-based approach, and the best way to learn the material is to execute the code and experiment with the examples. Check out the full series here: 
# 
# 1. [First Steps with Python and Jupyter](https://jovian.ml/aakashns/first-steps-with-python)
# 2. [A Quick Tour of Variables and Data Types](https://jovian.ml/aakashns/python-variables-and-data-types)
# 3. [Branching using Conditional Statements and Loops](https://jovian.ml/aakashns/python-branching-and-loops)
# 4. [Writing Reusable Code Using Functions](https://jovian.ml/aakashns/python-functions-and-scope)
# 5. [Reading from and Writing to Files](https://jovian.ml/aakashns/python-os-and-filesystem)
# 6. [Object Oriented Programming with Classes](https://jovian.ml/aakashns/python-object-oriented-programming)
# 
# 

# ## How to run the code
# 
# This tutorial hosted on [Jovian.ml](https://www.jovian.ml), a platform for sharing data science projects online. You can "run" this tutorial and experiment with the code examples in a couple of ways: *using free online resources* (recommended) or *on your own computer*.
# 
# >  This tutorial is a [Jupyter notebook](https://jupyter.org) - a document made of "cells", which can contain explanations in text or code written in Python. Code cells can be executed and their outputs e.g. numbers, messages, graphs, tables, files etc. can be viewed within the notebook, which makes it a really powerful platform for experimentation and analysis. Don't afraid to experiment with the code & break things - you'll learn a lot by encoutering and fixing errors. You can use the "Kernel > Restart & Clear Output" menu option to clear all outputs and start again from the top of the notebook.
# 
# ### Option 1: Running using free online resources (1-click, recommended)
# 
# The easiest way to start executing this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. You can also select "Run on Colab" or "Run on Kaggle", but you'll need to create an account on [Google Colab](https://colab.research.google.com) or [Kaggle](https://kaggle.com) to use these platforms.
# 
# 
# ### Option 2: Running on your computer locally
# 
# You'll need to install Python and download this notebook on your computer to run in locally. We recommend using the [Conda](https://docs.conda.io/en/latest/) distribution of Python. Here's what you need to do to get started:
# 
# 1. Install Conda by [following these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Make sure to add Conda binaries to your system `PATH` to be able to run the `conda` command line tool from your Mac/Linux terminal or Windows command prompt. 
# 
# 
# 2. Create and activate a [Conda virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) called `zerotopandas` which you can use for this tutorial series:
# ```
# conda create -n intro-to-python -y python=3.8 
# conda activate intro-to-python
# ```
# You'll need to create the environment only once, but you'll have to activate it every time want to run the notebook. When the environment is activated, you should be able to see a prefix `(intro-to-python)` within your terminal or command prompt.
# 
# 
# 3. Install the required Python libraries within the environmebt by the running the following command on your  terminal or command prompt:
# ```
# pip install jovian jupyter numpy pandas matplotlib seaborn --upgrade
# ```
# 
# 4. Download the notebook for this tutorial using the `jovian clone` command:
# ```
# jovian clone aakashns/python-variables-and-data-types
# ```
# The notebook is downloaded to the directory `python-variables-and-data-types`.
# 
# 
# 5. Enter the project directory and start the Jupyter notebook:
# ```
# cd python-variables-and-data-types
# jupyter notebook
# ```
# 
# 6. You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by visiting http://localhost:8888 on your browser. Click on the notebook `python-variables-and-data-types.ipynb` to open it and run the code. If you want to type out the code yourself, you can also create a new notebook using the "New" button.
# 
# 
# 

# ## Storing information using variables
# 
# Computers are useful for two purposes: storing information and performing operations on stored information. While working with a programming language such as Python, informations is stored in *variables*. You can think of variables are containers for storing data. The data stored within a variable is called it's *value*. It's really easy to create variables in Python, as we've already seen in the [previous tutorial](https://jovian.ml/aakashns/first-steps-with-python/v/4#C15).
# 
# 

# In[1]:


my_favorite_color = "blue"


# In[2]:


my_favorite_color


# A variable is created using an *assignment statement*, which begins with the variable's name, followed by the assignment operator `=` (different from the equality comparision operator `==`), followed by the value to be stored within the variable. 
# 
# You can also values to multiple variables in a single statement by separating the variable names and values with commas.

# In[3]:


color1, color2, color3 = "red", "green", "blue"


# In[4]:


color1


# In[5]:


color2


# In[6]:


color3


# You can assign the same value to multiple variables by chaining multiple assignment operations within a single statement.

# In[7]:


color4 = color5 = color6 = "magenta"


# In[8]:


color4


# In[9]:


color5


# In[10]:


color6


# You can change the value stored within a variable simply by assigning a new value to it using another assignment statement. Be careful while reassgining variables: when you assign a new value to the variable, the old value is lost and no longer accessible.

# In[11]:


my_favorite_color = "red"


# In[12]:


my_favorite_color


# While assigning a new value to a variable, you can also use the previous value of the variable to determine the new value.

# In[13]:


counter = 10


# In[14]:


counter = counter + 1


# In[15]:


counter


# The pattern `var = var op something` (where `op` is an arithmetic operator like `+`, `-`, `*`, `/`) is very commonly used, so Python provides a *shorthand* syntax for it.

# In[16]:


counter = 10


# In[17]:


# Same as `counter = counter + 4`
counter += 4


# In[18]:


counter


# Variable names can be short (`a`, `x`, `y` etc.) or descriptive ( `my_favorite_color`, `profit_margin`, `the_3_musketeers` etc.). Howerver, you must follow these rules while naming Python variables:
# 
# * A variable's name must start with a letter or the underscore character `_`. It cannot start with a number.
# * A variable name can only contain lowercase or uppercase letters, digits or underscores (`a`-`z`, `A`-`Z`, `0`-`9` and `_`).
# * Variable names are case-sensitive i.e. a_variable, A_Variable and A_VARIABLE are all different variables.
# 
# Here are some valid variable names:

# In[19]:


a_variable = 23
is_today_Saturday = False
my_favorite_car = "Delorean"
the_3_musketeers = ["Athos", "Porthos", "Aramis"] 


# Let's also try creating some variables with invalid names. Python prints a syntax error if your variable's name is invalid.
# 
# > **Syntax**: The syntax of a programming language refers to the rules which govern what a valid instruction or *statement* in the language should look like. If a statement does not follow these rules, Python stops execution and informs you that there is a *syntax error*. You can think of syntax as the rules of grammar for a programming language.

# In[20]:


a variable = 23


# In[21]:


is_today_$aturday = False


# In[22]:


my-favorite-car = "Delorean"


# In[23]:


3_musketeers = ["Athos", "Porthos", "Aramis"]


# ### Save and upload your notebook
# 
# Whether you're running this Jupyter notebook on an online service like Binder or on your local machine, it's important to save your work from time, so that you can access it later, or share it online. You can upload this notebook to your [Jovian.ml](https://jovian.ml) account using the `jovian` Python library.

# In[24]:


# Install the jovian library
get_ipython().system('pip install jovian --upgrade --quiet')


# In[25]:


import jovian


# In[26]:


jovian.commit(project='python-variables-and-data-types')


# The first time you run `jovian.commit`, you'll be asked to provide an API Key, to securely upload the notebook to your Jovian.ml account. You can get the API key from your Jovian.ml profile page after logging in / signing up.
# 
# ![api-key](https://i.imgur.com/YGGLH3e.png)
# 
# `jovian.commit` uploads the notebook to your Jovian.ml account, captures the Python environment and creates a shareable link for your notebook as shown above. You can use this link to share your work and let anyone (including you) run your notebooks and reproduce your work.

# ## Built-in data types in Python
# 
# Any data or information stored within a Python variable has a *type*. The type of data stored within a variable can be checked using the `type` function.

# In[27]:


a_variable


# In[28]:


type(a_variable)


# In[29]:


is_today_Saturday


# In[30]:


type(is_today_Saturday)


# In[31]:


my_favorite_car


# In[32]:


type(my_favorite_car)


# In[33]:


the_3_musketeers


# In[34]:


type(the_3_musketeers)


# Python has several built-in data types for storing different types of information in variables. Following are at some commonly used data types:
# 
# 1. Integer
# 2. Float
# 3. Boolean
# 4. None
# 5. String
# 6. List
# 7. Tuple
# 8. Dictionary
# 
# Integer, float, boolean, None and string are *primitive data types* because they represent a single value. Other data types like list, tuple and dictionary are often called *data structures* or *containers* because they hold multiple pieces of data together.

# ### Integer
# 
# Integers represent positive or negative whole numbers, from negative infinity to infinity. Note that integers should not include decimal points. Integers have the type `int`.

# In[35]:


current_year = 2020


# In[36]:


current_year


# In[37]:


type(current_year)


# Unlike some other programming languages, integers in Python can be arbirarily large (or small). There's no lowest or highest value for integers, and there's just one `int` type (as opposed to `short`, `int`, `long`, `long long`, `unsigned int` etc. in C/C++/Java).

# In[38]:


a_large_negative_number = -23374038374832934334234317348343


# In[27]:


a_large_negative_number


# In[28]:


type(a_large_negative_number)


# ### Float
# 
# Floats (or floating point numbers) are numbers with a decimal point. There are no limits on the value of a float or the number of digits before or after the decimal point. Floating point numbers have the type `float`.

# In[29]:


pi = 3.141592653589793238


# In[30]:


pi


# In[31]:


type(pi)


# Note that a whole number is treated as a float if it is written with a decimal point, even though the decimal portion of the number is zero.

# In[32]:


a_number = 3.0


# In[33]:


a_number


# In[34]:


type(a_number)


# In[35]:


another_number = 4.


# In[36]:


another_number


# In[37]:


type(another_number)


# Floating point numbers can also be written using the scientific notation with an "e" to indicate the power of 10.

# In[38]:


one_hundredth = 1e-2


# In[39]:


one_hundredth


# In[40]:


type(one_hundredth)


# In[41]:


avogadro_number = 6.02214076e23


# In[42]:


avogadro_number


# In[43]:


type(avogadro_number)


# Floats can be converted into integers and vice versa using the `float` and `int` functions. The operation of coverting one type of value into another is called casting.

# In[44]:


float(current_year)


# In[45]:


float(a_large_negative_number)


# In[46]:


int(pi)


# In[47]:


int(avogadro_number)


# While performing arithmetic operations, integers are automatically converted to floats if any of the operands is a float. Also, the division operator `/` always returns a float, even if both operands are integers. Use the `//` operator if you want the result of division to be an `int`.

# In[48]:


type(45 * 3.0)


# In[49]:


type(45 * 3)


# In[50]:


type(10/3)


# In[52]:


type(10/2)


# In[53]:


type(10//2)


# ### Boolean
# 
# Booleans represent one of 2 values: `True` and `False`. Booleans have the type `bool`.

# In[54]:


is_today_Sunday = True


# In[55]:


is_today_Sunday


# In[56]:


type(is_today_Saturday)


# Booleans are generally returned as the result of a comparision operation (e.g. `==`, `>=` etc.).

# In[57]:


cost_of_ice_bag = 1.25
is_ice_bag_expensive = cost_of_ice_bag >= 10


# In[58]:


is_ice_bag_expensive


# In[59]:


type(is_ice_bag_expensive)


# Booleans are automatically converted to `int`s when used in arithmetic operations. `True` is converted to `1` and `False` is converted to `0`.

# In[60]:


5 + False


# In[61]:


3. + True


# Any value in Python can be converted to a Boolean using the `bool` function. 
# 
# Only the following values evaluate to `False` (they are often called *falsy* values):
# 
# 1. The value `False` itself
# 2. The integer `0`
# 3. The float `0.0`
# 4. The empty value `None`
# 5. The empty text `""`
# 6. The empty list `[]`
# 7. The empty tuple `()`
# 8. The empty dictionary `{}`
# 9. The emtpy set `set()`
# 10. The empty range `range(0)`
# 
# Everything else evaluates to `True` (a value that evalutes to `True` is often called a *truthy* value).

# In[62]:


bool(False)


# In[63]:


bool(0)


# In[64]:


bool(0.0)


# In[65]:


bool(None)


# In[66]:


bool("")


# In[67]:


bool([])


# In[68]:


bool(())


# In[69]:


bool({})


# In[70]:


bool(set())


# In[71]:


bool(range(0))


# In[72]:


bool(True), bool(1), bool(2.0), bool("hello"), bool([1,2]), bool((2,3)), bool(range(10))


# ### None
# 
# The None type includes a single value `None`, used to indicate the absence of a value. `None` has the type `NoneType`. It is often used to declare a variable whose value may be assigned later.

# In[73]:


nothing = None


# In[74]:


type(nothing)


# ### String
# 
# A string is used to represent text (*a string of characters*) in Python. Strings must be surrounded using quotations (either the single quote `'` or the double quote `"`). Strings have the type `string`.

# In[75]:


today = "Saturday"


# In[76]:


today


# In[77]:


type(today)


# You can use single quotes inside a string written with double quotes, and vice versa.

# In[78]:


my_favorite_movie = "One Flew over the Cuckoo's Nest" 


# In[79]:


my_favorite_movie


# In[80]:


my_favorite_pun = 'Thanks for explaining the word "many" to me, it means a lot.'


# In[81]:


my_favorite_pun


# To use the a double quote within a string written with double quotes, *escape* the inner quotes by prefixing them with the `\` character.

# In[82]:


another_pun = "The first time I got a universal remote control, I thought to myself \"This changes everything\"."


# In[83]:


another_pun


# Strings created using single or double quotes must begin and end on the same line. To create multiline strings, use three single quotes `'''` or three double quotes `"""` to begin and end the string. Line breaks are represented using the newline character `\n`.

# In[84]:


yet_another_pun = '''Son: "Dad, can you tell me what a solar eclipse is?" 
Dad: "No sun."'''


# In[85]:


yet_another_pun


# Multiline strings are best displayed using the `print` function.

# In[86]:


print(yet_another_pun)


# In[87]:


a_music_pun = """
Two windmills are standing in a field and one asks the other, 
"What kind of music do you like?"  

The other says, 
"I'm a big metal fan."
"""


# In[88]:


print(a_music_pun)


# You can check the length of a string using the `len` function.

# In[90]:


len(my_favorite_movie)


# Note that special characters like `\n` and escaped characters like `\"` count as a single character, even though they are written and sometimes printed as 2 characters.

# In[92]:


multiline_string = """a
b"""
multiline_string


# In[93]:


len(multiline_string)


# A string can be converted into a list of characters using `list` function.

# In[94]:


list(multiline_string)


# Strings also support several list operations, which are discussed in the next section. We'll look at a couple of examples here.
# 
# You can access individual characters within a string using the `[]` indexing notation. Note the character indices go from `0` to `n-1`, where `n` is the length of the string.

# In[95]:


today = "Saturday"


# In[96]:


today[0]


# In[97]:


today[3]


# In[98]:


today[7]


# You can access a part of a string using by providing a `start:end` range instead of a single index in `[]`.

# In[99]:


today[5:8]


# You can also check whether a string contains a some text using the `in` operator. 

# In[100]:


'day' in today


# In[101]:


'Sun' in today


# Two or more strings can be joined or *concatenated* using the `+` operator. Be careful while concatenating strings, sometimes you may need to add a space character `" "` between words.

# In[102]:


full_name = "Derek O'Brien"


# In[103]:


greeting = "Hello"


# In[104]:


greeting + full_name


# In[105]:


greeting + " " + full_name + "!" # additional space


# String in Python have many built-in *methods* that can be used to manipulate them. Let's try out some common string methods.
# 
# > **Methods**: Methods are functions associated with data types, and are accessed using the `.` notatation e.g. `variable_name.method()` or `"a string".method()`. Methods are a powerful technique for associating common operations with values of specific data types.
# 
# The `.lower()`, `.upper()` and `.capitalize()` methods are used to change the case of the characters.

# In[106]:


today.lower()


# In[107]:


"saturday".upper()


# In[108]:


"monday".capitalize() # changes first character to uppercase


# The `.replace` method is used to replace a part of the string with another string. It takes the portion to be replaced and the replacement text as *inputs* or *arguments*.

# In[109]:


another_day = today.replace("Satur", "Wednes")


# In[110]:


another_day


# Note that a new string is returned, and the original string is not modified.

# In[111]:


today


# The `.split` method can be used to split a string into a list of strings based using the character(s) provided.

# In[112]:


"Sun,Mon,Tue,Wed,Thu,Fri,Sat".split(",")


# The .strip method is used to remove whitespace characters from the beginning and end of a string.

# In[113]:


a_long_line = "       This is a long line with some space before, after,     and some space in the middle..    "


# In[114]:


a_long_line_stripped = a_long_line.strip()


# In[115]:


a_long_line_stripped


# The `.format` method is used to combine values of other data types e.g. integers, floats, booleans, lists etc. with strings. It is often used to create output messages for display.

# In[116]:


# Input variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Template for output message
output_template = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}."""

print(output_template)


# In[117]:


# Inserting values into the string
total_profit = cost_of_ice_bag * profit_margin * number_of_bags
output_message = output_template.format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit)

print(output_message)


# Notice how the placeholders `{}` in the `output_template` string are replaced with the arguments provided to the `.format` method.
# 
# It is also possible use the string concatenation operator `+` to combine strings with other values, however, those values must first be converted to strings using the `str` function.

# In[118]:


"If a grocery store sells ice bags at $ " + cost_of_ice_bag + ", with a profit margin of " + profit_margin


# In[119]:


"If a grocery store sells ice bags at $ " + str(cost_of_ice_bag) + ", with a profit margin of " + str(profit_margin)


# In fact, the `str` can be used to convert a value of any data type into a string.

# In[120]:


str(23)


# In[121]:


str(23.432)


# In[122]:


str(True)


# In[123]:


the_3_musketeers = ["Athos", "Porthos", "Aramis"]
str(the_3_musketeers)


# Note that all string methods returns new values, and DO NOT change the existing string. You can find a full list of string methods here: https://www.w3schools.com/python/python_ref_string.asp. 

# Strings also support the comparision operators `==` and `!=` for checking whether two strings are equal

# In[124]:


first_name = "John"


# In[125]:


first_name == "Doe"


# In[126]:


first_name == "John"


# In[127]:


first_name != "Jane"


# We've looked at the primitive data types in Python, and we're now ready to explore non-primitive data structures or containers.
# 
# Before continuing, let us run `jovian.commit` once again to record another snapshot of our notebook.

# In[235]:


jovian.commit()


# Running `jovian.commit` multiple times within a notebook automatically records new versions. You will continue to have access to all the previous versions of your notebook, using the versions dropdown on the Jovian.ml web interface.

# ### List
# 
# A list in Python is an ordered collection of values. Lists can hold values of different data types, and support operations to add, remove and change values. Lists have the type `list`.
# 
# To create a list, enclose a list of values within square brackets `[` and `]`, separated by commas.

# In[128]:


fruits = ['apple', 'banana', 'cherry']


# In[129]:


fruits


# In[130]:


type(fruits)


# Let's try creating a list containing values of different data types, including another list.

# In[131]:


a_list = [23, 'hello', None, 3.14, fruits, 3 <= 5]


# In[132]:


a_list


# In[168]:


empty_list = []


# In[169]:


empty_list


# To determine the number of values in a list, use the `len` function. In general, the `len` function can be used to determine of values in several other data types.

# In[133]:


len(fruits)


# In[134]:


print("Number of fruits:", len(fruits))


# In[135]:


len(a_list)


# In[170]:


len(empty_list)


# You can access the elements of a list using the the *index* of the element, starting from the index 0.

# In[136]:


fruits[0]


# In[137]:


fruits[1]


# In[138]:


fruits[2]


# If you try to access an index equal to or higher than the length of the list, Python returns an `IndexError`.

# In[139]:


fruits[3]


# In[140]:


fruits[4]


# In[141]:


fruits[-1]


# In[142]:


fruits[-2]


# In[143]:


fruits[-3]


# In[144]:


fruits[-4]


# You can also access a range of values from the list. The result is itself a list. Let us look at some examples.

# In[145]:


a_list = [23, 'hello', None, 3.14, fruits, 3 <= 5]


# In[146]:


a_list


# In[147]:


len(a_list)


# In[148]:


a_list[2:5]


# Note that the start index (`2` in the above example) of the range is included in the list, but the end index (`5` in the above example) is not included. So, the result has 3 values (indices `2`, `3` and `4`).
# 
# Here are some experiments you should try out (use the empty cells below):
# 
# * Try setting one or both indices of the range are larger than the size of the list e.g. `a_list[2:10]`
# * Try setting the start index of the range to be larger than the end index of the range e.g. `list_a[2:10]`
# * Try leaving out the start or end index of a range e.g. `a_list[2:]` or `a_list[:5]`
# * Try using negative indices for the range e.g. `a_list[-2:-5]` or `a_list[-5:-2]` (can you explain the results?)
# 
# > The flexible and interactive nature of Jupyter notebooks makes them a great tool for learning and experimentation. Most questions that arise while you are learning Python for the first time can be resolved by simply typing the code into a cell and executing it. Let your curiosity run wild, and discover what Python is capable of, and what it isn't! 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# You can also change the value at a specific index within a list using the assignment operation.

# In[149]:


fruits


# In[150]:


fruits[1] = 'blueberry'


# In[151]:


fruits


# A new value can be added to the end of a list using the `append` method.

# In[152]:


fruits.append('dates')


# In[153]:


fruits


# A new value can also be inserted a specific index using the `insert` method.

# In[154]:


fruits.insert(1, 'banana')


# In[155]:


fruits


# You can remove a value from the list using the `remove` method.

# In[156]:


fruits.remove('blueberry')


# In[157]:


fruits


# What happens if a list has multiple instances of the value passed to `.remove`? Try it out.

# In[ ]:





# In[ ]:





# To remove an element from a specific index, use the `pop` method. The method also returns the removed element.

# In[158]:


fruits


# In[159]:


fruits.pop(1)


# In[160]:


fruits


# If no index is provided, the `pop` method removes the last element of the list.

# In[161]:


fruits.pop()


# In[162]:


fruits


# You can test whether a list contains a value using the `in` operator.

# In[163]:


'pineapple' in fruits


# In[164]:


'cherry' in fruits


# To combine two or more lists, use the `+` operator. This operation is also called *concatenation*.

# In[165]:


fruits


# In[166]:


more_fruits = fruits + ['pineapple', 'tomato', 'guava'] + ['dates', 'banana']


# In[167]:


more_fruits


# To create a copy of a list, use the `copy` method. Modifying the copied list does not affect the original list.

# In[171]:


more_fruits_copy = more_fruits.copy()


# In[172]:


more_fruits_copy


# In[173]:


# Modify the copy
more_fruits_copy.remove('pineapple')
more_fruits_copy.pop()
more_fruits_copy


# In[174]:


# Original list remains unchanged
more_fruits


# Note that you cannot create a copy of a list by simply creating a new variable using the assignment operator `=`. The new variable will point to the same list, and any modifications performed using one variable will affect the other.

# In[175]:


more_fruits


# In[176]:


more_fruits_not_a_copy = more_fruits


# In[177]:


more_fruits_not_a_copy.remove('pineapple')
more_fruits_not_a_copy.pop()


# In[178]:


more_fruits_not_a_copy


# In[179]:


more_fruits


# Just like strings, there are several in-built methods to manipulate a list. Unlike strings, however, most list methods modify the original list, rather than returning a new one. Check out some common list operations here: https://www.w3schools.com/python/python_ref_list.asp
# 
# 
# Following are some exercises you can try out with list methods (use the blank code cells below):
# 
# * Reverse the order of elements in a list
# * Add the elements of one list to the end of another list
# * Sort a list of strings in alphabetical order
# * Sort a list of numbers in decreasing order

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Tuple
# 
# A tuple is an ordered collection of values, similar to a list, however it is not possible to add, remove or modify values in a tuple. A tuple is created by enclosing values within parantheses `(` and `)`, separated by commas.
# 
# > Any data structure that cannot be modified after creation is called *immutable*. You can think of tuples as immutable lists.
# 
# Let's try some experiments with tuples.

# In[180]:


fruits = ('apple', 'cherry', 'dates')


# In[181]:


# check no. of elements
len(fruits)


# In[182]:


# get an element (positive index)
fruits[0]


# In[183]:


# get an element (negative index)
fruits[-2]


# In[184]:


# check if it contains an element
'dates' in fruits


# In[185]:


# try to change an element
fruits[0] = 'avocado'


# In[186]:


# try to append an element
fruits.append('blueberry')


# In[187]:


# try to remove an element
fruits.remove('apple')


# You can also skip the parantheses `(` and `)` while creating a tuple. Python automatically converts comma-separated values into a tuple.

# In[188]:


the_3_musketeers = 'Athos', 'Porthos', 'Aramis'


# In[189]:


the_3_musketeers


# You can also create a tuple with just one element, if you include a comma after the element. Just wrapping it with parantheses `(` and `)` won't create a tuple.

# In[192]:


single_element_tuple = 4,


# In[193]:


single_element_tuple


# In[194]:


another_single_element_tuple = (4,)


# In[195]:


another_single_element_tuple


# In[196]:


not_a_tuple = (4)


# In[197]:


not_a_tuple


# Tuples are often used to create multiple variables with a single statement.

# In[198]:


point = (3, 4)


# In[199]:


point_x, point_y = point


# In[200]:


point_x


# In[201]:


point_y


# You can convert a list into a tuple using the `tuple` function, and vice versa using the `list` function

# In[202]:


tuple(['one', 'two', 'three'])


# In[203]:


list(('Athos', 'Porthos', 'Aramis'))


# Tuples have just 2 built-in methods: `count` and `index`. Can you figure out what they do? While look could look for documentation and examples online, there's an easier way to check the documentation of a method, using the `help` function.

# In[204]:


a_tuple = 23, "hello", False, None, 23, 37, "hello"


# In[205]:


help(a_tuple.count)


# Within a Jupyter notebook, you can also start a code cell with `?` and type the name of a function or method. When you execute this cell, you will see the documentation for the function/method in a pop-up window.

# In[206]:


get_ipython().run_line_magic('pinfo', 'a_tuple.index')


# Try using `count` and `index` with `a_tuple` in the code cells below.

# In[ ]:





# In[ ]:





# ### Dictionary
# 
# A dictionary is an unordered collection of items. Each item stored in a dictionary has a key and value. Keys are used to retrieve values from the dictionary. Dictionaries have the type `dict`.
# 
# Dictionaries are often used to store many pieces of information e.g. details about a person, in a single variable. Dictionaries are created by enclosing key-value pairs within curly brackets `{` and `}`.

# In[207]:


person1 = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}


# In[208]:


person1


# Dictionaries can also be created using the `dict` function.

# In[209]:


person2 = dict(name='Jane Judy', sex='Female', age=28, married=False)


# In[210]:


person2


# In[211]:


type(person1)


# Keys can be used to access values using square brackets `[` and `]`.

# In[212]:


person1['name']


# In[213]:


person1['married']


# In[214]:


person2['name']


# If a key isn't present in the dictionary, then a `KeyError` is returned.

# In[215]:


person1['address']


# The `get` method can also be used to access the value associated with a key.

# In[216]:


person2.get("name")


# The `get` method also accepts a default value which is returned if the key is not present in the dictionary.

# In[217]:


person2.get("address", "Unknown")


# You can check whether a key is present in a dictionary using the `in` operator.

# In[218]:


'name' in person1


# In[219]:


'address' in person1


# You can change the value associated with a key using the assignment operator.

# In[220]:


person2['married']


# In[221]:


person2['married'] = True


# In[222]:


person2['married']


# The assignment operator can also be used to add new key-value pairs to the dictonary.

# In[223]:


person1


# In[224]:


person1['address'] = '1, Penny Lane'


# In[225]:


person1


# To remove a key and the associated value from a dictionary, use the `pop` method.

# In[226]:


person1.pop('address')


# In[227]:


person1


# Dictonaries also provide methods to view the list of keys, values or key-value pairs inside it.

# In[228]:


person1.keys()


# In[229]:


person1.values()


# In[230]:


person1.items()


# In[231]:


person1.items()[1]


# The result of the `keys`, `values` or `items` look like lists but don't seem to support the indexing operator `[]` for retrieving elements. 
# 
# Can you figure out how to access an element at a specific index from these results? Try it below. *Hint: Use the `list` function*

# In[ ]:





# In[ ]:





# Dictionaries provide many other methods. You can learn more about them here: https://www.w3schools.com/python/python_ref_dictionary.asp
# 
# Here are some experiments you can try out with dictionaries (use the empty cells below):
# * What happens if you use the same key multiple times while creating a dictionary?
# * How can you create a copy of a dictionary (modifying the copy should not change the original)?
# * Can the value associated with a key itself be a dictionary?
# * How can you add the key value pairs from one dictionary into another dictionary? Hint: See the `update` method.
# * Can the keys of a dictionary be something other than a string e.g. a number, boolean, list etc.?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Further Reading
# 
# We've now completed our exploration of variables and common data types in Python. Following are some resources to learn more about data types in Python:
# 
# * Python official documentation: https://docs.python.org/3/tutorial/index.html
# * Python Tutorial at W3Schools: https://www.w3schools.com/python/
# * Practical Python Programming: https://dabeaz-course.github.io/practical-python/Notes/Contents.html
# 
# You are now ready to move on to the next tutorial: [Branching using conditional statements and loops in Python](https://jovian.ml/aakashns/python-branching-and-loops)

# Let's save a snapshot of our notebook one final time using `jovian.commit`.

# In[237]:


jovian.commit()


# In[ ]:




