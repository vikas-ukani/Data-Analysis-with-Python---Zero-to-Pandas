#!/usr/bin/env python
# coding: utf-8

# # Top 5 String Formatting NumPy methods
# 
# 
# ### Numpy is the best way to deal with string type of data and convert intothe number and floating point values.. 
# 
# 
# > `array2string` *(a[, max_line_width, precision, …])*  **Return a string representation of an array.**
# 
# > `array_repr` *(arr[, max_line_width, precision, …])*  **Return the string representation of an array.**
# 
# > `array_str` *(a[, max_line_width, precision, …])* **Return a string representation of the data in an array.**
# 
# > `format_float_positional` *(x[, precision, …])* **Format a floating-point scalar as a decimal string in positional notation.**
# 
# > `format_float_scientific` *(x[, precision, …])* **Format a floating-point scalar as a decimal string in scientific notation.**

# ### The Basics
# 
# ---
# 
# NumPy’s main object is the **homogeneous multidimensional array**. It is a table of elements, all of the same type, indexed by a tuple of non-negative integers and many more. In NumPy dimensions are known as `axes`.
# 
# - For example, the coordinates of a point in 3D space [1, 2, 1] has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.
# 
# ```
# [[ 1., 0., 0.],
#  [ 0., 1., 2.]]
# ```
# 
# NumPy’s array class is called `ndarray`. It is also known by the `alias` array. 
# > Note that `numpy.array` is not the same as the **Standard Python Library** class `array.array`, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an ndarray object are:
# 
# ---
# 
# > ### `ndarray.ndim`
# > - To know, What are the number of axes (dimensions) of the array.
# 
# > ### `ndarray.shape`
# > To know the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, `shape` will be `(n,m)`. The length of the shape tuple is therefore the number of axes, ndim.
# 
# > ### `ndarray.size`
# > To know the total number of elements of the array. This is equal to the product of the elements of shape.
# 
# > ### `ndarray.dtype`
# > An object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally, NumPy provides types of its own. `numpy.int32`, `numpy.int16`, and `numpy.float64` are some examples.
# 
# > ### `ndarray.itemsize`
# > The size in bytes of each element of the array. For example, an array of elements of type `float64` has itemsize `8 (=64/8)`, while one of type `complex32` has itemsize `4 (=32/8)`. It is equivalent to `ndarray.dtype.itemsize`.
# 
# > ### `ndarray.data`
# > The buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
# 
# 
# ### An example 
# 
# --- 
# 
# ```
# >>> import numpy as np
# 
# >>> a = np.arange(15).reshape(3, 5)
# >>> a
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
#        
#        
# >>> a.shape
# (3, 5)
# 
# >>> a.ndim
# 2
# >>> a.dtype.name
# 'int64'
# >>> a.itemsize
# 8
# >>> a.size
# 15
# >>> type(a)
# <class 'numpy.ndarray'>
# >>> b = np.array([6, 7, 8])
# >>> b
# array([6, 7, 8])
# >>> type(b)
# <class 'numpy.ndarray'>
# 
# ```

# In[1]:


get_ipython().system('pip install jovian --upgrade -q')


# In[2]:


import jovian


# In[3]:


jovian.commit(project='numpy-array-string-operations')


# Let's begin by importing Numpy and listing out the functions covered in this notebook.

# In[4]:


import numpy as np 


# # String Functions
# 
# ---
# 
# > ### function1 = [numpy.array2string](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string) 
# > ### function2 = [numpy.array_repr](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr)
# > ### function3 = [numpy.array_str](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str)
# > ### function4 = [numpy.format_float_positional](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional)
# > ### function5 = [numpy.format_float_scientific](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific)

# ## Function 1 - numpy.array2string
# 
# In this function, we discuss about `array2string` method, This method simply `Return a string representation of an array.` 
# 
# - Let's understand from an simple examples

# #### Example 1

# In[5]:



# Create and simple array with complex numer
arr_1 = np.array([1e-16,1,2,3]) 

# Convert arrat to string using this function
result = np.array2string(arr_1,
                precision=2,
                separator=',',
                suppress_small=True)

 


# In[6]:


result


# - As we can see above output returning the output in string format, we can check the data type of the result variable

# In[7]:


type(result)


# #### Example 2 
# 

# ## Function 2 - numpy.array_repr
# 
# In this function, we discuss about `array_repr` method, This method simply `Return the string representation of an array.` 
# 
# > *numpy.array_repr(arr, max_line_width=None, precision=None, suppress_small=None)*
# 
# 

# - Let's understand from an simple examples

# In[8]:


# Example 1
arr_1 = np.array_repr(np.array([1,2]))


# In[9]:


arr_1


# In[10]:


arr_2 = np.array_repr(np.ma.array([0.]))


# In[11]:


arr_2


# In[12]:


arr_3 = np.array_repr(np.array([], np.int32))


# In[13]:


arr_3


# In[14]:


arr_4 = np.array_repr(np.array([], np.int64)) # int4, int8, int16, int32, int64


# In[15]:


arr_4


# In[16]:


# Example 2
array_1 = np.array([1e-6, 4e-7, 2, 3])


# In[17]:


array_1


# In[18]:


array_2 = np.array_repr(array_1, precision=6, suppress_small=True)


# In[19]:


array_2


# In[20]:


jovian.commit()


# ---
# 
# ## Function 3 - numpy.array_str
# 
# Return a string representation of the data in an array.
# 
# - The data in the array is returned as a single string. This function is similar to array_repr, the difference being that array_repr also returns information on the kind of array and its data type

# In[21]:


# Example 1 - working
array_1 = np.array_str(np.arange(3))


# In[22]:


array_1


# In[23]:


array_2 = np.array_str(np.arange(3, 6))


# In[24]:


array_2


# In[25]:


array_3 = np.array_str(np.arange(20, 500, 5))


# In[26]:


array_3


# In[27]:


jovian.commit()


# 
# ---
# 
# 
# ## Function 4 - numpy.format_float_positional
# 
# ---
# 
# Format a floating-point scalar as a decimal string in positional notation
# 
# Provides control over rounding, trimming and padding. Uses and assumes IEEE unbiased rounding. Uses the “Dragon4” algorithm.
# 
# > *numpy.format_float_positional(x, precision=None, unique=True, fractional=True, trim='k', sign=False, pad_left=None, pad_right=None)*

# In[28]:


# Example 1 - working
array_1 = np.format_float_positional(np.float64(np.pi))


# In[29]:


array_1


# In[30]:


# Example 2 - working

array_2 = np.format_float_positional(np.float32(np.pi))


# In[31]:


array_2


# In[32]:


# Example 2 - working

array_3 = np.format_float_positional(np.float16(np.pi))


# In[33]:


array_3


# In[34]:


# Example 3 - breaking (to illustrate when it breaks)

array_4 = np.format_float_positional(np.float8(np.pi))


# Explanation about example (why it breaks and how to fix it)

# Some closing comments about when to use this function.

# In[35]:


jovian.commit()


# ---
# 
# ## Function 5 - numpy.format_float_scientific
# 
# ---
# 
# Format a floating-point scalar as a decimal string in scientific notation.
# 
# Provides control over rounding, trimming and padding. Uses and assumes IEEE unbiased rounding. Uses the “Dragon4” algorithm.
# 
# 

# In[36]:


# Example 1 - working
array_1 = np.format_float_scientific(np.float32(np.pi))


# In[37]:


array_1


# In[38]:


# Example 2 - working
array_2 = np.format_float_scientific(np.float64(np.pi))


# In[39]:


array_2


# In[40]:


array_3 = np.float32(1.23e24)


# In[41]:


array_3


# In[42]:


array_4 = np.format_float_scientific(array_3, unique=False, precision=15)


# In[43]:


array_4


# In[44]:


array_5 = np.format_float_scientific(array_3, exp_digits=4)


# In[45]:


array_5


# In[46]:


# Example 3 - breaking (to illustrate when it breaks)
array_6 = np.format_float_scientific(array_3, exp_digits=50)


# In[47]:


jovian.commit()


# ## Conclusion
# 
# In this notebook, I'd  explain every numpy string function with many examples.

# ## Reference Links
# 
#  * Numpy official tutorial : https://numpy.org/doc/stable/user/quickstart.html
# - [numpy.array2string](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string) 
# - [numpy.array_repr](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr)
# - [numpy.array_str](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str)
# - [numpy.format_float_positional](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional)
# - [numpy.format_float_scientific](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific)

# In[ ]:




