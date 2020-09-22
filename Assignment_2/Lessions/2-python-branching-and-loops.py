#!/usr/bin/env python
# coding: utf-8

# # Branching using Conditional Statements and Loops in Python
# 
# ### Part 3 of "A Gentle Introduction to Programming with Python"
# 
# This tutorial is the third in a series on introduction to programming using the Python language. These tutorials take a practical coding-based approach, and the best way to learn the material is to execute the code and experiment with the examples. Check out the full series here: 
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
# jovian clone aakashns/python-branching-and-loops
# ```
# The notebook is downloaded to the directory `python-branching-and-loops`.
# 
# 
# 5. Enter the project directory and start the Jupyter notebook:
# ```
# cd python-branching-and-loops
# jupyter notebook
# ```
# 
# 6. You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by visiting http://localhost:8888 on your browser. Click on the notebook `python-branching-and-loops.ipynb` to open it and run the code. If you want to type out the code yourself, you can also create a new notebook using the "New" button.
# 
# 
# 
# 

# ## Branching with `if`, `else` and `elif`
# 
# A really powerful feature of programming languages is *branching*: the ability to make decisions and execute a different set of statements based on whether one or more conditions are true.
# 
# ### The `if` statement
# 
# In Python, branching is done using the `if` statement, which is written as follows:
# 
# ```
# if condition:
#     statement1
#     statement2
# ```
# 
# The `condition` can either be a variable or an expression. If the condition evaluates to `True`, then the statements within the *`if` block* are executed. Note the 4 spaces before `statement1`, `statement 2` etc. The spaces inform Python that these statements are associated with the `if` statement above. This technique of structuring code by adding spaces is called *indentation*.
# 
# > **Indentation**: Python relies heavily on *indentation* (white space before a statement) to define structure in code. This makes Python code easy to read and understand, but you can run into problems if you don't use indentation properly. Indent your code by placing the cursor at the start of the line and pressing the `Tab` key once to add 4 spaces. Pressing `Tab` again will indent the code further by 4 more spaces, and press `Shift+Tab` will reduce the indentation by 4 spaces. 
# 
# 
# As an example, let's write some code to check and print a message if a given number is even.

# In[1]:


a_number = 34


# In[2]:


if a_number % 2 == 0:
    print("We're inside an if block")
    print('The given number {} is even.'.format(a_number))


# Note that we are using the modulus operator `%` to find the remainder from the division of `a_number` by `2`, and then we are using the comparision operator `==` check if the reminder is `0`, indicating that the number is divisible by 2 i.e. it is even. 
# 
# Since the number `34` is indeed divisible by `2` the expression `a_number % 2 == 0` evaluates to `True`, so the `print` statement under the `if` statement is executed. Also note that we are using the string `format` method to include the number within the message.
# 
# Let's try the above again with an odd number.

# In[4]:


another_number = 33


# In[5]:


if another_number % 2 == 0:
    print('The given number {} is even.'.format(a_number))


# As expected, since the condition `another_number % 2 == 0` evluates to `False`, no message is printed. 
# 
# ### The `else` statement
# 
# It would be nice to print a different method if the number is not even in the above example. This can be done by adding the `else` statement. It is written as follows:
# 
# ```
# if condition:
#     statement1
#     statement2
# else:
#     statement4
#     statement5
# 
# ```
# 
# If the `condition` evaluates to `True`, the statements in the `if` block are executed, and if it evaluates to `False`, the statements in the `else` block are executed.

# In[6]:


a_number = 34


# In[7]:


if a_number % 2 == 0:
    print('The given number {} is even.'.format(a_number))
else:
    print('The given number {} is odd.'.format(a_number))


# In[8]:


another_number = 33


# In[9]:


if another_number % 2 == 0:
    print('The given number {} is even.'.format(another_number))
else:
    print('The given number {} is odd.'.format(another_number))


# Here's another example, which uses the `in` operator to check membership within a tuple.

# In[21]:


the_3_musketeers = ('Athos', 'Porthos', 'Aramis')


# In[22]:


a_candidate = "D'Artagnan"


# In[23]:


if a_candidate in the_3_musketeers:
    print("{} is a musketeer".format(a_candidate))
else:
    print("{} is not a musketeer".format(a_candidate))


# ### The `elif` statement
# 
# Python also provides an `elif` statement (short for "else if"), to chain a series of conditional blocks. The conditions are evaluated one by one. For the first condition that evaluates to `True`, the statements in the respective block are executed, and the remaining conditions are not evaluated. So, in a chain of `if`, `elif`, `elif`... statements, exactly one conditional block is evaluted.

# In[10]:


today = 'Wednesday'


# In[11]:


if today == 'Sunday':
    print("Today is the day of the sun.")
elif today == 'Monday':
    print("Today is the day of the moon.")
elif today == 'Tuesday':
    print("Today is the day of Tyr, the god of war.")
elif today == 'Wednesday':
    print("Today is the day of Odin, the supreme diety.")
elif today == 'Thursday':
    print("Today is the day of Thor, the god of thunder.")
elif today == 'Friday':
    print("Today is the day of Frigga, the goddess of beauty.")
elif today == 'Saturday':
    print("Today is the day of Saturn, the god of fun and feasting.")


# In the above example, the first 3 conditions evalute to `False`, so none of the first 3 message are printed. The fourth condition evalues to `True`, so the corresponding message is printed. The remaining conditions are skipped. Try changing the value of `today` above and re-executing the cells to print all the different messages.
# 
# 
# To verify that the remaining conditions are skipped, let us try another example.

# In[12]:


a_number = 15


# In[13]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
elif a_number % 7 == 0:
    print('{} is divisible by 7'.format(a_number))


# Note that the message `15 is divisible by 5` is not printed because the condition `a_number % 5 == 0` isn't evaluted, since the previous condition `a_number % 3 == 0` evaluates to `True`. This is the key differnce between using a chain of `if`, `elif`, `elif`... statements vs. simply using a chain of `if` statements, where each condition is evaluted independently.

# In[14]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
if a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
if a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
if a_number % 7 == 0:
    print('{} is divisible by 7'.format(a_number))


# ### Using `if`, `elif` and `else` together
# 
# You can also include an `else` statement at the end of a chain of `if`, `elif`... statements. This code within the `else` block are evaluted when none of the conditions hold true.

# In[15]:


a_number = 49


# In[16]:


if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
else:
    print('All checks failed!')
    print('{} is not divisible by 2, 3 or 5'.format(a_number))


# Conditions can also combined using the logical operators `and`, `or` and `not`. Logical operators are explained in detail in the [first tutorial](https://jovian.ml/aakashns/first-steps-with-python/v/4#C49).

# In[30]:


a_number = 12


# In[31]:


if a_number % 3 == 0 and a_number % 5 == 0:
    print("The number {} is divisible by 3 and 5".format(a_number))
elif not a_number % 5 == 0:
    print("The number {} is not divisible by 5".format(a_number))


# ### Non-Boolean Conditions
# 
# Note that conditions do not necessarily have to be booleans. In fact, a condition can be any value. The value is convered into a boolean automatically using the `bool` operator. This means that falsy values like `0`, `''`, `{}`, `[]` etc. evalute to `False` and all other values evalute to `True`.

# In[17]:


if '':
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')


# In[18]:


if 'Hello':
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')


# In[19]:


if { 'a': 34 }:
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')


# In[20]:


if None:
    print('The condition evaluted to True')
else:
    print('The condition evaluted to False')


# ### Nested conditional statements
# 
# The code inside an `if` block can also include an `if` statement inside it. This pattern is called `nesting` and is used when you need to check for another condition after a certain condition is evaluted as true.

# In[32]:


a_number = 15


# In[34]:


if a_number % 2 == 0:
    print("{} is even".format(a_number))
    if a_number % 3 == 0:
        print("{} is also divisible by 3".format(a_number))
    else:
        print("{} is not divisibule by 3".format(a_number))
else:
    print("{} is odd".format(a_number))
    if a_number % 5 == 0:
        print("{} is also divisible by 5".format(a_number))
    else:
        print("{} is not divisibule by 5".format(a_number))


# Notice how the `print` statements are indented by 8 spaces, to indicate that they are part of the inner `if`/`else` blocks.
# 
# > Nested `if`, `else` statements are often confusing to read and prone to human error. It's a good idea to avoid nesting whenever possible, or limit the nesting to 1 or 2 levels.

# ### Shorthand `if` conditional expression
# 
# A common use case of the `if` statement involves testing a condition and setting the value of a variable based on the condition.

# In[36]:


a_number = 13

if a_number % 2 == 0:
    parity = 'even'
else:
    parity = 'odd'

print('The number {} is {}.'.format(a_number, parity))


# Python provides a shorter syntax, which allows writing such conditions in a in a single line of code. It is known as a *conditional expression*, sometimes also referred to as a *ternary operator*. It has the following syntax:
# 
# ```
# x = true_value if condition else false_value
# ```
# 
# It has the same behaviour as the following `if`-`else` block:
# 
# ```
# if condition:
#     x = true_value
# else:
#     x = false_value
# ```
# 
# Let's try it out for the example above.

# In[37]:


parity = 'even' if a_number % 2 == 0 else 'odd'


# In[38]:


print('The number {} is {}.'.format(a_number, parity))


# ### Statements and Expressions
# 
# The conditional expression highlights an important distinction between *statements* and *expressions* in Python. 
# 
# > **Statements**: A statement is an instruction that can be executed. Every line of code we have written so far is a statement e.g. assigning a variable, calling a function, conditional statements using `if`, `else` and `elif`, loops using `for` and `while` etc.
# 
# > **Expressions**: An expression is some code that evalutes to a value. Examples include values of different data types, arithmetic expressions, conditions, variables, function calls, conditional expressions etc. 
# 
# 
# Most expressions can be executed as statements, but not all statements are expressions e.g. the `if` statement is not an expression since it does not evluate it a value, it simply performs some braching in the code. Similarly, loops and function definitions are not expressions (we'll learn more about these in later sections).
# 
# As a rule of thumb, an expression is anything that can appear on the right side of the assignment operator `=`. You can use this as a test for checking whether something is an expression or not. You'll get a syntax error if you try to assign something that is not an expression.

# In[42]:


# if statement
result = if a_number % 2 == 0: 
    'even'
else:
    'odd'


# In[44]:


# if expression
result = 'even' if a_number % 2 == 0 else 'odd'


# ### The `pass` statement
# 
# `if` statements cannot be empty, there must be at least one statement in every `if` and `elif` block. You can use the `pass` statement to do nothing and avoid getting an error.

# In[49]:


a_number = 9


# In[50]:


if a_number % 2 == 0:
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2')


# In[52]:


if a_number % 2 == 0:
    pass
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2'.format(a_number))


# ### Save and upload your notebook
# 
# Whether you're running this Jupyter notebook on an online service like Binder or on your local machine, it's important to save your work from time, so that you can access it later, or share it online. You can upload this notebook to your [Jovian.ml](https://jovian.ml) account using the jovian Python library.

# In[1]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[2]:


import jovian


# In[ ]:


jovian.commit(project='python-branching-and-loops')


# The first time you run `jovian.commit`, you'll be asked to provide an API Key, to securely upload the notebook to your Jovian.ml account. You can get the API key from your Jovian.ml profile page after logging in / signing up.
# 
# ![api-key](https://i.imgur.com/YGGLH3e.png)
# 
# `jovian.commit` uploads the notebook to your Jovian.ml account, captures the Python environment and creates a shareable link for your notebook as shown above. You can use this link to share your work and let anyone (including you) run your notebooks and reproduce your work.

# ## Iteration with `while` loops
# 
# Another powerful feature of programming languages, closely related to branching, is the ability to run one or more statements multiple times. This feature is often referred to as *iteration* on *looping*, and there are two ways to do this in Python: using `while` loops and `for` loops. 
# 
# `while` loops have the following syntax:
# 
# ```
# while condition:
#     statement(s)
# ```
# 
# The statements in block under `while` are executed repeatedly as long as the `condition` evalutes to `True`. In most cases, the block of statements makes some change to a variable which causes the condition to evalute to `False` after a certain number of iterations.
# 
# Let's try to calculate the factorial of `100` using a `while` loop, as an example. The factorial of a number `n` is defined as the product or multiplication of all the numbers from `1` to `n` i.e. `1*2*3*...*(n-2)*(n-1)*n`.

# In[59]:


result = 1
i = 1

while i <= 100:
    result = result * i
    i = i+1

print('The factorial of 100 is: {}'.format(result))


# Here's how the above code works:
# 
# * We initialize two variables `result` and `i`. `result` will contain the final result of the computation. And `i` is used to keep track of the next number to be multiplied with `result`. Both are initialized to 1 (can you explain why?)
# 
# * The condition `i<=100` holds true (since `i` is initially `1`), so the statements in the block below `while` are executed.
# 
# * The `result` is updated to `result * i`, and `i` is increased by `1` and now has the value `2`.
# 
# * At this point, condition `i<=100` is executed again, and since it continues to hold true, the `result` is once again updated to `result * i` and `i` is increased to `3`.
# 
# * This process is repeated till the condition becomes false, which happens when `i` holds the value `101`. Once the condition evalues to `False`, the execution of the loop ends and the `print` statement below it is executed. 
# 
# Can you see why `result` holds the value of the factorial of 100 at the end of the loop? If not, try adding `print` statements inside inside the loop to print the values of `result` and `i` and the end of each loop.
# 
# 
# > Iteration is a really powerful technique because it gives computers a huge advantage over human beings in performing hundreds or millions of repetitive operations really fast. With just 4-5 lines of code, we were able to multiply 100 numbers almost instantly. What's even more interesting is that the same code can be used to multiply a thousand number (just change the condition to `i <= 1000`) in just a few seconds.
# 
# You can check how long a cell takes to execute by adding the special *magic* command `%%time` at the top of a cell. Try checking how long it takes to compute the factorial of `100`, `1000`, `10000`, `100000` etc. 

# In[68]:


get_ipython().run_cell_magic('time', '', '\nresult = 1\ni = 1\n\nwhile i <= 1000:\n    result *= i # same as result = result * i\n    i += 1 # same as i = i+1\n\nprint(result)')


# Here's another example that uses two `while` loops to create an interesting pattern.

# In[72]:


line = '*'
max_length = 10

while len(line) <= max_length:
    print(line)
    line += "*"
    
while len(line) > 0:
    print(line)
    line = line[:-1]


# Can you see how the above example works? As an exercise, try printing the following pattern using a while loop (Hint: use string concatenation):
# 
# ```
#           *
#          **
#         ***
#        ****
#       *****
#      ******
#       *****
#        ****
#         ***
#          **
#           *
# ```
# 
# Here's another one, putting the two together:
# 
# 
# ```
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#       *********
#        *******
#         *****
#          ***
#           *
# ```

# ### Infinite Loops
# 
# If the condition in a `while` loop always holds true, then Python repeatedly executes the code within the loop forever, and the execution of the code never completes. This situation is called an infinite loop, and it generally indicates that there's you've made a mistake in your code e.g. using the wrong condition or forgetting to update a variable with an loop which will ultimately make the condition false.
# 
# If your code is *stuck* in an infinite loop during execution, just press the "Stop" button from the toolbar (next to "Run") or select "Kernel > Interrupt" from the Jupyter menu bar to stop or *interrupt* the execution of the code. The next 2 cells both lead to infinite loops, and need to be interrupted.

# In[77]:


# INFINITE LOOP - INTERRUPT THIS CELL

result = 1
i = 1

while i <= 100:
    result = result * i
    # forgot to increment i


# In[78]:


# INFINITE LOOP - INTERRUPT THIS CELL

result = 1
i = 1

while i > 0 : # wrong condition
    result *= i
    i += 1


# ### `break` and `continue` statements
# 
# You can use the `break` statment within the body of the loop to immediately stop the execution and *break* out of the loop (even if the condition provided to `while` still holds true).

# In[85]:


i = 1
result = 1

while i <= 100:
    result *= i
    if i == 42:
        print('Magic number 42 reached! Stopping execution..')
        break
    i += 1
    
print('i:', i)
print('result:', result)


# As you can see above, the value of `i` at the end of execution is 42. This example also shows how you can use an `if` statement within a `while` loop.
# 
# Sometimes you may not want to end the loop entirely, but simply skip the remaining statements in the loop and *continue* to the next loop. You can do this using the `continue` statement.

# In[86]:


i = 1
result = 1

while i < 20:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue
    print('Multiplying with {}'.format(i))
    result = result * i
    
print('i:', i)
print('result:', result)


# In the example above, the final statement of the loop `result = result * i` is skipped when `i` is even, as indicated by the messages printed during execution.
# 
# > **Logging**: The process of adding `print` statements at different points in the code (often within loops and conditional statements) for inspecting the values of variables at various stages of execution is called logging. As our programs get more complex, they naturally become prone to human errors. Logging can help in verifying the the program is working as expected. In many cases, `print` statements are added while writing & testing some code, and are removed at the end.

# Let us record a snapshot of our work before continuing using `jovian.commit`.

# In[117]:


jovian.commit()


# ## Iteration with `for` loops
# 
# A `for` loop is used for iterating or looping over sequences i.e. lists, tuples, dictionaries, strings and *ranges*. For loops have the following syntax:
# 
# ```
# for value in sequence:
#     statement(s)
# ```
# 
# The statements within the loop are executed once for each element in `sequence`. Here's an example that prints all the element of a list.

# In[87]:


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in days:
    print(day)


# Let's try using `for` loops with some other data types.

# In[89]:


# Looping over a string
for char in 'Monday':
    print(char)


# In[94]:


# Looping over a tuple
for fruit in ['Apple', 'Banana', 'Guava']:
    print("Here's a fruit:", fruit)


# In[96]:


# Looping over a dictionary
person = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}

for key in person:
    print("Key:", key, ",", "Value:", person[key])


# Note that while using a dictionary with a `for` loop, the iteration happens over keys within the dictionary. The key can be used within the loop to access the value. You can also iterate directly over the values using the `.values` method of the dictionary, or over key-value pairs using the `.items` method.

# In[97]:


for value in person.values():
    print(value)


# In[98]:


for key_value_pair in person.items():
    print(key_value_pair)


# Since a key-value pair is a tuple, we can also extract out the key & value into separate variables.

# In[99]:


for key, value in person.items():
    print("Key:", key, ",", "Value:", value)


# ### Iterating using `range` and `enumerate`
# 
# The `range` function is used to create a sequence of numbers that can be iterated over using a `for` loop. It can be used in 3 ways:
#  
# * `range(n)` - Creates a sequence of numbers from `0` to `n-1`
# * `range(a, b)` - Creates a sequence of numbers from `a` to `b-1`
# * `range(a, b, step)` - Creates a sequence of numbers from `a` to `b-1` with increments of `step`
# 
# Let's try it out.

# In[101]:


for i in range(7):
    print(i)


# In[102]:


for i in range(3, 10):
    print(i)


# In[103]:


for i in range(3, 14, 4):
    print(i)


# Ranges are used for iterating over lists, when you need to track the index of elements while iterating.

# In[105]:


a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(len(a_list)):
    print('The value at position {} is {}.'.format(i, a_list[i]))


# Another way to achieve the same result as above is using the `enumerate` function with `a_list` as an input, which returns a tuple containing the index and the corresponding element.

# In[112]:


for i, val in enumerate(a_list):
    print('The value at position {} is {}.'.format(i, val))


# ### `break`, `continue` and `pass` statements
# 
# Similar to `while` loops, `for` loops also support the `break` statement for breaking out of the loop and `continue` for skipping ahead to the next iteration.

# In[107]:


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


# In[109]:


for day in weekdays:
    print('Today is {}'.format(day))
    if (day == 'Wednesday'):
        print("I don't work beyond Wednesday!")
        break


# In[111]:


for day in weekdays:
    if (day == 'Wednesday'):
        print("I don't work on Wednesday!")
        continue
    print('Today is {}'.format(day))


# Simlar to `if` statements, `for` loops cannot be empty, so you can use a `pass` statement in case you don't want do execute any statements inside the loop.

# In[116]:


for day in weekdays:
    pass


# ### Nested `for` and `while` loops
# 
# Similar to conditional statements, loops can be nested inside other loops. This is useful for looping over each element in a list of lists, a list of dictionaries etc.

# In[121]:


persons = [{'name': 'John', 'sex': 'Male'}, {'name': 'Jane', 'sex': 'Female'}]

for person in persons:
    for key in person:
        print(key, ":", person[key])
    print(" ")


# In[122]:


days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['apple', 'banana', 'guava']

for day in days:
    for fruit in fruits:
        print(day, fruit)


# With this, we conclude our discussion of branching and loops in Python. Let us save a snapshot of our work using `jovian.commit`

# ## Further Reading and References
# 
# We've covered a lot of ground in just 3 tutorials. Practice your skills by doing this assignment: https://jovian.ml/aakashns/python-practice-assignment
# 
# Following are some resources to learn about more about conditional statements and loops in Python:
# 
# * Python Tutorial at W3Schools: https://www.w3schools.com/python/
# * Practical Python Programming: https://dabeaz-course.github.io/practical-python/Notes/Contents.html
# * Python official documentation: https://docs.python.org/3/tutorial/index.html
# 
# 

# In[118]:


jovian.commit()


# In[ ]:




