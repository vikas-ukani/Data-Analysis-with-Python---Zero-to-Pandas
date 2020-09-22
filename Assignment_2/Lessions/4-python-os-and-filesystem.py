#!/usr/bin/env python
# coding: utf-8

# # Reading from and Writing to Files using Python
# 
# ### Part 5 of "A Gentle Introduction to Programming with Python"
# 
# This tutorial is the fifth in a series on introduction to programming using the Python language. These tutorials take a practical coding-based approach, and the best way to learn the material is to execute the code and experiment with the examples. Check out the full series here: 
# 
# 1. [First Steps with Python and Jupyter](https://jovian.ml/aakashns/first-steps-with-python)
# 2. [A Quick Tour of Variables and Data Types](https://jovian.ml/aakashns/python-variables-and-data-types)
# 3. [Branching using Conditional Statements and Loops](https://jovian.ml/aakashns/python-branching-and-loops)
# 4. [Writing Reusable Code Using Functions](https://jovian.ml/aakashns/python-functions-and-scope)
# 5. [Reading from and Writing to Files](https://jovian.ml/aakashns/python-os-and-filesystem)
# 6. [Object Oriented Programming with Classes](https://jovian.ml/aakashns/python-object-oriented-programming)
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
# 2. Create and activate a [Conda virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) called `intro-to-python` which you can use for this tutorial series:
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
# jovian clone aakashns/python-os-and-filesystem
# ```
# The notebook is downloaded to the directory `python-os-and-filesystem`.
# 
# 
# 5. Enter the project directory and start the Jupyter notebook:
# ```
# cd python-os-and-filesystem
# jupyter notebook
# ```
# 
# 6. You can now access Jupyter's web interface by clicking the link that shows up on the terminal or by visiting http://localhost:8888 on your browser. Click on the notebook `python-os-and-filesystem.ipynb` to open it and run the code. If you want to type out the code yourself, you can also create a new notebook using the "New" button.
# 
# 
# 

# ## Interacting with the OS and filesystem
# 
# The `os` module in Python provides many functions for interacting with the OS and the filesystem. Let's import it and try out some examples.

# In[1]:


import os


# We can check the present working directory using the `os.getcwd` function.

# In[2]:


os.getcwd()


# To get the list of files in a directory, use `os.listdir`. You pass an absolute or relative path of a directory as the argument to the function.

# In[3]:


help(os.listdir)


# In[4]:


os.listdir('.') # relative path


# In[5]:


os.listdir('/usr') # absolute path


# A new directory can be created using `os.makedirs`. Let's create a new directory called `data`, where we'll later download some files.

# In[6]:


os.makedirs('./data', exist_ok=True)


# Can you figure out what the argument `exist_ok` does? Try using the `help` function or [read the documentation](https://docs.python.org/3/library/os.html#os.makedirs).
# 
# Let's verify that the directory was in fact, created, and is currently empty.

# In[7]:


'data' in os.listdir('.')


# In[8]:


os.listdir('./data')


# Let us download some files into the `data` directory using the `urllib` module.

# In[22]:


url1 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans1.txt'
url2 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans2.txt'
url3 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans3.txt'


# In[23]:


import urllib.request


# In[24]:


urllib.request.urlretrieve(url1, './data/loans1.txt')


# In[25]:


urllib.request.urlretrieve(url2, './data/loans2.txt')


# In[26]:


urllib.request.urlretrieve(url3, './data/loans3.txt')


# Let's verify that the files were downloaded.

# In[27]:


os.listdir('./data')


# ### Reading from a file 
# 
# To read the contents of a file, we first need to open the file using the built-in `open` function. The `open` function returns a file object, provides several methods for interacting with the contents of the file. It also accepts a `mode` argument

# In[28]:


file1 = open('./data/loans1.txt', mode='r')


# The `open` function also accepts a `mode` argument to specifies how we can interact with the file. The following options are supported:
# 
# ```
#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================
# ```
# 
# To view the contents of the file we can use the `read` method of the file object.

# In[29]:


file1_contents = file1.read()


# In[30]:


print(file1_contents)


# The file contains information about loans. It is a set of comma-separated values (CSV). 
# 
# > **CSVs**: A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields. (Wikipedia)
# 
# The first line of the file is the header, which indicates what each of the numbers on the remaining lines represent. Each of the remaining lines provides information about a loan. Thus, the second line `10000,36,0.08,20000` represents a loan with:
# 
# * an *amount* of `$10000`, 
# * *duration* of `36` months, 
# * *rate of interest* of `8%` per annum, and 
# * a down payment of `$20000`
# 
# The CSV is a common file format used for sharing data for analysis and visualization. Over the course of this tutorial, we will read the data from these CSV files, process it, and write the results back to files. Before we continue, let's close the file using the `close` method (otherwise Python will continue to hold the entire file in the RAM)

# In[31]:


file1.close()


# Once a file is closed, it can no longer be read.

# In[32]:


file1.read()


# ### Closing files automatically using `with`
# 
# To make it easy to automatically close a file once you are done processing it, you can open it using the `with` statement.

# In[33]:


with open('./data/loans2.txt') as file2:
    file2_contents = file2.read()
    print(file2_contents)


# Once the statements within the `with` block are executed, the `.close` method on `file2` is automatically invoked. Let's verify this by trying to read from the file object again.

# In[34]:


file2.read()


# ### Reading a file line by line
# 
# 
# File objects provide a `readlines` method to read a file line-by-line. 

# In[35]:


with open('./data/loans3.txt', 'r') as file3:
    file3_lines = file3.readlines()


# In[36]:


file3_lines


# ### Processing data from files
# 
# Before performing any operations on the data stored in a file, we need to convert the contents of the file from one large string into Python data types. For the file `loans1.txt` containing information about loans in a CSV format, we can do the following:
# 
# * Read the file line by line
# * Parse the first line to get list of the column names or headers
# * Split each remaining line and convert each value into a float
# * Create a dictionary for each loan using the headers as keys
# * Create a list of dictionaries to keep track of all the loans
# 
# Since we will perform the same operations for multiple files, it would be useful define a function `read_csv` to do this. We'll also define some helper functions to build up the functionality step by step. 
# 
# Let's start by defining a function `parse_header` which takes a line as input and returns a list of column headers.

# In[37]:


def parse_headers(header_line):
    return header_line.strip().split(',')


# The `strip` method removes any extra spaces and the newline character `\n`, and the split method breaks a string into a list using the given separator (`,` in this case).

# In[38]:


file3_lines[0]


# In[39]:


headers = parse_headers(file3_lines[0])


# In[40]:


headers


# Next, let's define a function `parse_values` which takes a line containing some data, and returns a list of floating point numbers.

# In[41]:


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        values.append(float(item))
    return values


# In[42]:


file3_lines[1]


# In[43]:


parse_values(file3_lines[1])


# The values were parsed and converted to floating point numbers, as expected. Let's try it for another line from the file, which does not contain a value for the down payment.

# In[44]:


file3_lines[2]


# In[45]:


parse_values(file3_lines[2])


# This leads to a `ValueError` because the empty string `''` cannot be converted to a float. We can enhance the `parse_values` function to handle this *edge case*.

# In[46]:


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values


# In[47]:


file3_lines[2]


# In[48]:


parse_values(file3_lines[2])


# Next, let's define a function `create_item_dict` which takes a list of values and a list of headers as inputs, and returns a dictionary with the values associated with their respective headers as keys.

# In[49]:


def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


# Can you figure out what the Python built-in function `zip` does? Try out an example, or [read the documentation](https://docs.python.org/3.3/library/functions.html#zip).

# In[50]:


for item in zip([1,2,3], ['a', 'b', 'c']):
    print(item)


# Let's try out `crate_item_dict` with a couple of examples.

# In[51]:


file3_lines[1]


# In[52]:


values1 = parse_values(file3_lines[1])
create_item_dict(values1, headers)


# In[53]:


file3_lines[2]


# In[54]:


values2 = parse_values(file3_lines[2])
create_item_dict(values2, headers)


# As expected, the values & header are combined to create a dictionary with the approriate key-value pairs.
# 
# We are now ready to put it all together and define the `read_csv` function.

# In[55]:


def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# Let's try it out!

# In[56]:


with open('./data/loans2.txt') as file2:
    print(file2.read())


# In[57]:


read_csv('./data/loans2.txt')


# The file is read and converted to a list of dictionaries, as expected. The `read_csv` file is generic enough that it can parse any file in the CSV format, with any number of rows or columns. Here's the full code for `read_csv` along with the helper functions:

# In[58]:


def parse_headers(header_line):
    return header_line.strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# Try to create small, generic and reusable functions whenever possible, as they will likely be useful beyond just the problem at hand, and save you a lot of effort in the future.
# 
# In the [previous tutorial](https://jovian.ml/aakashns/python-functions-and-scope), we defined a function to calculate the equal monthly installments for a loan. Here's what it looked like:

# In[59]:


import math

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi


# We can use this function to calculate EMIs for all the loans in a file.

# In[63]:


loans2 = read_csv('./data/loans2.txt')


# In[64]:


loans2


# In[65]:


for loan in loans2:
    loan['emi'] = loan_emi(loan['amount'], 
                           loan['duration'], 
                           loan['rate']/12, # the CSV contains yearly rates
                           loan['down_payment'])


# In[66]:


loans2


# You can see that each loan now has a new key `emi`, which provides the EMI for the loan. We can extract this logic into a function, so that we can be used for other files too.

# In[67]:


def compute_emis(loans):
    for loan in loans:
        loan['emi'] = loan_emi(
            loan['amount'], 
            loan['duration'], 
            loan['rate']/12, # the CSV contains yearly rates
            loan['down_payment'])


# ### Writing to files
# 
# Now that we have performed some processing on the data, it would be a good idea to write the results back to a file in the CSV format. We can do this by creating/opening a file in write mode with `open` and using the `.write` method of the file object. The string `format` method will be useful for 

# In[69]:


loans2 = read_csv('./data/loans2.txt')


# In[70]:


compute_emis(loans2)


# In[71]:


loans2


# In[74]:


with open('./data/emis2.txt', 'w') as f:
    for loan in loans2:
        f.write('{},{},{},{},{}\n'.format(
            loan['amount'], 
            loan['duration'], 
            loan['rate'], 
            loan['down_payment'], 
            loan['emi']))


# Let's verify that the file was created and written to as expected.

# In[75]:


os.listdir('data')


# In[76]:


with open('./data/emis2.txt', 'r') as f:
    print(f.read())


# Great, looks like the loan details (along with the computed EMIs) were written into the file.
# 
# Let's define a generic function `write_csv` which takes a list of dictionaries and writes it to a file in CSV format. We will also include the column headers in the first line.

# In[83]:


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


# Do you understand how the function works? If now, try executing each statement by line by line or a different cell to figure out how it works. 
# 
# Let's try it out!

# In[84]:


loans3 = read_csv('./data/loans3.txt')


# In[85]:


compute_emis(loans3)


# In[88]:


write_csv(loans3, './data/emis3.txt')


# In[89]:


with open('./data/emis3.txt', 'r') as f:
    print(f.read())


# With just 4 lines of code, we can now read each downloaded file, calcualte the EMIs, and write the results back to new files:

# In[90]:


for i in range(1,4):
    loans = read_csv('./data/loans{}.txt'.format(i))
    compute_emis(loans)
    write_csv(loans, './data/emis{}.txt'.format(i))


# In[93]:


os.listdir('./data')


# Isn't that wonderful? Once all the functions are defined, we can calculate EMIs for thousands or even millions of loans across many files with just a few lines of code, in a few seconds. Now we're starting to see the real power of using a programming language like Python for processing data!

# ## Save and upload your notebook
# 
# Whether you're running this Jupyter notebook on an online service like Binder or on your local machine, it's important to save your work from time, so that you can access it later, or share it online. You can upload this notebook to your [Jovian.ml](https://jovian.ml) account using the `jovian` Python library.

# In[94]:


# Install the library
get_ipython().system('pip install jovian --upgrade --quiet')


# In[95]:


# Import the jovian module
import jovian


# In[ ]:


jovian.commit(project='python-os-and-filesystem')


# ## Summary and Further Reading
# 
# With this we complete our discussion of reading from and writing to files in Python. We've covered the following topics in this tutorial:
# 
# * Interacting with the filesystem using the `os` module
# * Downloading files from URLs using the `urllib` module
# * Opening files using the `open` built-in function
# * Reading the contents of a file using `.read`
# * Closing file automatically using `with`
# * Reading a file line by line using `readlines`
# * Processing data from a CSV file using our own functions
# * Using helper funtions to build more complext functions
# * Writing data to a file using `.write`
# 
# 
# 
# This is by no means an exhaustive or comprehensive tutorial on working with files in Python. Following are some more resources you should check out:
# 
# * Python Tutorial at W3Schools: https://www.w3schools.com/python/
# * Practical Python Programming: https://dabeaz-course.github.io/practical-python/Notes/Contents.html
# * Python official documentation: https://docs.python.org/3/tutorial/index.html
# 
# You are ready to move on to the next tutorial: ["Object-oriented programming using classes in Python"](https://jovian.ml/aakashns/python-object-oriented-programming).

# In[ ]:




