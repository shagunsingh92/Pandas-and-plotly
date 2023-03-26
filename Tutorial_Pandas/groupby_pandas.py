'''
1. Group by concept is same as in SQL. Here values of a dataframe/table is grouped based on the values of a column and
later on an arithmetic function is performed on it
2. The resultant dataframe after groupby and arithmetic operation in point 1 will not return the second column of the
dataframe as arithmetic operation cannot be performed on strings
3. We can perform all in one line, check point 2
4. We can calculate apply the following common aggregate functions after groupby the dataframe - count()[will count the
number of instances under a groupby category. max()/min()[if applied on a string column will return max/min length of the
string], describe()[this returns all the important arithmetic info in one go], transpose()[will transpose the resultant
dataframe]

'''

import numpy as np
import pandas as pd

data = {'Company': ['Google','Google','FB','FB','MSFT','MSFT'], 'Person':['Sam','Charlie','Amy','Carl','tim','pam'],
        'Sales': [200,120,340,570,680,780]}
df = pd.DataFrame(data)
print(df)

#point 1
# x= df.groupby('Company')
# print(x) # this will return a groupy object
# print(x.mean()) #this will perform an arithmetic operation on the groupby object created

#point 2
print(df.groupby('Company').mean().loc['FB'])