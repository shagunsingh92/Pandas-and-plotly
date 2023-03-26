'''
Check the udemy lecture for this.
1. Merging data syntax - pd.merge(dataframe1,dataframe2,how = 'inner/outer/left/right', on =[column_name])
merging the dataframes happen when we want to join on the columns of a dataframe
2. Joining of the dataframes happen when we try to join on the index of two different dataframes
Joining syntax is dataframe1.join(dataframe2). Here also just like merge we can specify how i.e
dataframe1.join(dataframe2 , how= 'outer/inner/left/right)
3. Joining will not have on attribute as joining happens by default on the index position
'''