'''
1. Conditional selection - We can use conditional operators on a dataframes like we used on numpy arrays. Where ever the
conditions are true, the result will be "True" else "False" check point 1 for the example
2. rather than applying conditions on the entire dataframe we can also apply it to one column. If we pass that condition
to a dataframe the resultant will dataframe will have values only where the condition was true. In case of column conditional
the resultant will never have NaN values
3. In point 3 we are grabbing all the rows where the value of "w" is above 0. From this filtered data we can grab a particular
column. Doesn't work with rows.
4. If we want to apply multiple operators together on a dataframe we can use the "&" operator. Do not use "and" here as python
cannot compare two series having boolean values. It can only compare one boolean to another boolean. Check point 4 for example.
Use "|" for or operator
5. BY running dataframe.reset_index() , this command will reset the index of a dataframe to the default index i.e 0,1,2 etc and
the existing index will get changed to a column of the same dataframe. This doesn't occur inplace and the original DF remains
intact. If we want the changes to be inplace we can set inplace= true
6. We can create a new column for the dataframe by using "dataframe.set_index('column_name')". Doesn't change the dataframe inplace.
7. We can add a new column to the dataframe by using dataframe['name_of_column'] = [list of values]
'''

# import numpy as np
# import pandas as pd
#
# from numpy.random import randn
# np.random.seed(101)
#
# df = pd.DataFrame(data=randn(5,4),index=['a','b','c','d','e'],columns=['w','x','y','z'])
# print(df)

# point 1
# print(df>0)
# booldf = df>0
# print(df[booldf]) # this command will return only those points where df>0 returns true. NaN will be returned if the value is false

#point 2
# print(df['w']>0) # As row c is false here that is why when it will be passed in the next statement will not return that row altogether
# print(df[df['w']>0])

#point 3
# print(df[df['w']>0]['x'])
# print(df[df['w']>0][['x','y']]) # we can also grab multiple columns after filtering the data by passing in the list of columns
# result = df[df['w']>0]
# result['x'] # this will give the same result as the first line of point 3


#point 4
# print(df[(df['w']>0)&(df['x']>0)])
# print(df[(df['w']>0)|(df['x']>0)])

#point 5
# print(df.reset_index())

#point 7 - adding a new column to the dataframe
# df['new_col'] = ['abc','efg','hij','klm','mnq']

#point 6
# x= df.set_index('new_col')
# print(x)
# print(x)