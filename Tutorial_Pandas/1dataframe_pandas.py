'''
1. By using seed after random one can get the same random values as everybody else
2. Dataframe is a bunch of series with a shared index. Column w,x,y,z in point 2 are nothing but four different series
with same index
3. We can use indexing to capture a column or a set of columns from a dataframe
4. One can create a new column which has a relationship with the other existing columns and this new column will get added
to the dataframe once the command is executed
5. If we called for a multiple column from a dataframe and check it's type the resultant will not be a series, but a dataframe
6. If we want to drop a column from the dataframe we can simply run command dataframe.drop('column_name', axis=1). Axis
attribute needs to be specified here as the default axis captured is "o" which refers to the rows in a dataframe and not
columns. This command doesn't delete the data from the main dataframe. Incase we want to drop a column in place i.e directly
from the original dataframe we can set the drop attribute - inplace = True
7. One can also drop the rows using drop function. There the axis = 0, which is a default value hence there is no need to specify it
8. we can get the shape of a dataframe by running df.shape
9. Not only columns, but rows of a dataframe are also series. For grabbing a row run command, dataframe.loc['row_name'] or
dataframe.iloc[index of the row]. One can use loc if they want to grab row based on their index label and can use iloc
if the want to grab a row by their default index positions.
10. If we want to grab a particular set of data from a dataframe we can use the syntax - dataframe.loc['row_name','column_name']



'''
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

#point 2
df = pd.DataFrame(data=randn(5,4),index=['a','b','c','d','e'],columns=['w','x','y','z'])
print(df)

# point 3
print(df['w'])
print(type(df['w']))
print(df[['w','x']]) #need to pass a list of columns if we want to grab multiple columns

#point 4
df['new'] = df['x']+df['y']
print(df)

# point 6
x= df.drop('new',axis=1)
print(df)
print(x)

# point 9
print(df.loc['a'])
print(df.iloc[0]) # both of these commands will return the same results

# point 10
print(df.loc['a','x'])
print(df.loc[['a','b'],['x','y']])
