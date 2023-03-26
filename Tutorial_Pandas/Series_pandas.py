'''
1. pandas is a library which is built on the top of numpy. It allows fast analysis and is used for data cleaning
2. Pandas has it's own visualization tools and can work with different types of data sources
3. This is called as the python version of excel
4. Series is similar to Numpy array
5. Series(S should be capital) can take any data type eg. integer, string, dictionary,numpy array, built in functions etc
6. We need not to specify data and index attributes in the Series. Check ex 6, but the order should be considered
7. We can use index inorder to grab values from a list. We can also add two series. The resultant list will have NaN
wherever the index doesn't match. check example
8. In numpy and pandas the resultant of an arithematic operation is always a float, so that we do not end up loosing information
'''
import numpy as np
import pandas as pd

label = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
# print(pd.Series(data= my_data,index=label))
# print(pd.Series(data=my_data)) # this will create a default index position
# print(pd.Series(data=d)) # this will consider the keys as index and values as the value points of the dictionary

# print(pd.Series(my_data,label)) # ex 6 - this will give the same result as above
# print(pd.Series(arr))

#ex point 7
# ser1 = pd.Series(data=my_data,index=label)
# ser2 = pd.Series(data=arr,index= label)
# print(ser1['a'])
# print(ser1+ser2)