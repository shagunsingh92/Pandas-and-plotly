'''
1. In order to find the unique values in a column of a dataframe we can use the unique method on the column
2. If we want the number of unique values in a column, we can either use the length method or nuique method of pandas
3. If we want to find out the number of times unique values appears in a column, we can use value_counts() function
4. If we want to apply a custom function/lambda function on a column, we can do that by using the apply method.
The function passed in under the apply method will be broadcasted ove the entire column. we can also pass in built in
functions to apply eg. len, sum, count etc
5. If we want to remove a column from the dataframe we can use drop() function. We need to specify the column that we
want to drop and the axis where the column belongs
6. If we want to get the list of all the columns in a dataframe, we can run the command dataframe.columns. Same thing
can be done for Index.
7. We can sort a column values by using function sort_values(by= 'column_name'). The index remains attached to the column
values even after sorting.
8. We cna find null values in a dataframe by using isnull() function
9. We can pivot a table by using pivot_table(values= [takes in the column name which will give the values to the pivot table]
,index= [takes in the list of columns which will serve as an index] , columns= [takes in the name of the column which will specify
the name column name]). If there is no corresponding values available in the pivot table for the columns selected, it will be
replaced by NaN
'''
import numpy as np
import pandas as pd
#
# df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
# print(df)

#point 1
# print(df['col2'].unique())

#point 2
# print(len(df['col2'].unique()))
# print(df['col2'].nunique())

# point 3
# print(df['col2'].value_counts())

#point 4
# def times(x):
#     return x*2
# print(df['col1'].apply(times)) # we do not call the function in a usual way, paranthesis is missing
# print(df['col3'].apply(len))
# print(df['col1'].apply(lambda x:x*2)) # this command will broadcast the lambda expression to each element of col 2

#point 5
# print(df.drop('col1',axis=1)) # this will not alter the actual dataframe, if we want a permanent change, set inplace= true
# print(df)

#point 6
# print(df.columns)
# print(df.index) # this will not return a list

#point 7
# print(df.sort_values(by='col2')) # doesn't make the change to the actual dataframe
# print(df)

#point8
# print(df.isnull()) # this will return booleans

#point9
data = {'A':['foo','foo','foo','bar','bar','bar'],
'B':['one','one','two','two','one','one'],
'C':['x','y','x','y','x','y'],
'D':[1,3,2,5,4,1]
        }
df = pd.DataFrame(data)
print(df)

print(df.pivot_table(values='D',index=['A','B'],columns='C')) #Column 'A' and 'B' will become a multilevel index