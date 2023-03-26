'''
1. we can drop the null values from a dataframe by using "dataframe.dropna
2. we can set a thresh(threshold) while dropping the null values.
3. we can fill the null values by using "dataframe.fillna"
4. dropna and fillna are not inplace methods and will not make any changes to the actual dataframe
5. Most of the time people fill the null values with the mean of that column
'''

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[1,2,3],'C':[1,np.nan,np.nan]}
df = pd.DataFrame(d)
print(df)

# point 1 and 2
# print(df.dropna())
# print(df.dropna(axis=1,thresh = 2)) # by default the axis is 0, if we want to remove null from columns, set axis to 1

#point 3
# print(df.fillna('Filled'))

#point 4
print(df['A'].fillna(value = df['A'].mean()))