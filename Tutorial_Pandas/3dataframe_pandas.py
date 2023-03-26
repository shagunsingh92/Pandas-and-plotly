'''
1. Multiindex with index hirarchy - point 1
2. In order to learn how to grab data from a multilevel hirarchy, check example in point 2
3. We can rename the columns containing index. Check point 3
4. We can return the cross section of a dataframe
5. xs(cross section method) will let us skip one level altogether and will help is grabbing everything under the index
'''

import numpy as np
import pandas as pd

# point 1 - creating a multilevel hirarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)
df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
print(df)

#point 2 - grabing data from a multilevel hirarchy
print(df.loc['G1'].loc[1])

#point 3 - renaming the index
df.index.names = ['Groups','Nums']
print(df)

#point 4- other way of grabbing rows and columns in a multilevel indexing is by using xs method
print(df.xs('G1')) # this will return everything under G1

#point 5 - for grabbing everything under index 1
print(df.xs(1, level= 'Nums')) # specify the level which you want to grab