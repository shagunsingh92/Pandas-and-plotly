'''
1. Pandas have two different types of data structure:
    a) series - It is a one dimensional array with indices. It stores a single column or row of data in a Dataframe. basically it is one column of a dataframe. Stores only one type of data type.
            syntax:
                variable = pd.Series(np.random.rand(334)) #here 334 is the number of rows in the series.
    b) DataFrame- Basically something like a base excel file which can be used for different analysis. It is a tabular spreadsheet like structure with one or multiple rows and columns.
                all the columns of a DataFrame contains only one type of data eg. integer, float etc. Different columns might contain different types of data. We can create a dataframe with the combination of series
            syntax:
                newdf = pd.DataFrame(np.random.rand(334,5),index = np.arange(334))
2. A default index is given to the DataFrame, but if we want to remove it we can set index = False in the DataFrame argument

3. We can download the DataFrame in a csv file for further analysis - step 2
    syntax:
    dataframe_variable_name.to_csv('name of the csv file',index=False/True)

    The above syntax will download the dataframe in the csv file. Ran this code in Jupyter as there is a separate folder created for it. Check the Jupyter folder
    Making and running changes in the code will also effect the already downloaded file.

4. In order to see rows from the top or bottom of a dataframe, use "dataframe_name.head(num of rows required)" or "dataframe_name.tail(num of rows required)"

5. If we want different mathematical calculations(eg. max, min, mean, st dv etc) on the numerical column of dataframe in one go then use "dataframe_name.describe()" - step 2

6. We can read a csv file. Follow the syntax: (Check Jupyter folder)
    var_name = pd.read_csv("csv_name")

7. We can do various types of manipulations on the data points of the dataframe using slicing. check jupyter folder.
    Changing the data points using slicing may trigger warnings because programer might confuse a dataframe pointer with a dataframe copy(point 21)

8. We can change the default index to index of our choice by the following syntax
    DataFrame_name.index = [Pass a list of desired indices]

    Similarly to change column names use:
    DataFrame_name.columns = [Pass a list of desired indices]

9. Pandas is an open source data analysis library which is written in python

10. We use numpy as it is written in c and is faster. Also it consumes less storage if we are using lists etc.

11. We use pandas for big data analysis rather than excel because excel doesn't speak to python. Also pandas can leverage the power and speed of numpy.

12. Excel has many limitation like speed and data storage

13. All the excel tasks like removing duplicates, adding columns, appending something to the data, reading excel or csv etc, everything can be done with pandas.

14. Jupyter is an open source web application which supports 40+ programming languages including python and R. It is best IDE for data analysis as we
    can see all the manipulations, arrays, graphs etc right next to the code cell. We can share the Jupyter notebooks on GitHub, DropBox etc

15. in order to find the data type of all the columns run the following code:
        dataframe_name.dtypes()

16. If a column contains different type of data than type becomes object.

17. A list of indices of a dataframe can be found by the following code "dataframe_name.index". A range of all the columns can be found using "dataframe_name.columns"

18. We can change a DataFrame into a numpy array by - "Dataframe_name.to-numpy()"

19. We can do a transpose of the dataframe by using - "DataFrame_name.T"

20. To sort the data in a dataframe use the following:
    newdf.sort_index(axis=0,ascending= False)# axis= 0 is rows and axis=1 os column. "ascending" argument is by default True which means if not set to false the sorting will always happen from lower to higher.

21. by writing:
        newdf2 = newdf (we are not creating a copy of dataframe but newdf2 is a pointer to the same dataframe newdf. If any changes are made to newdf2, same changes will apply to newdf)
    In order to create a copy of a dataframe use:
        newdf2 = newdf.copy() (Now newdf2 will be a separate copy of newdf and not a pointer.)

22. Because of the warnings and probable errors during new value assignment in a dataframe, rather than using slicing use "df_name.loc[row_name, column_name] = value"
    loc should also be used to extract a particular set of data from data frame eg.

    dataframe_name.loc[[rowname1,rowname2],[columnname1,columnname2]] or
    dataframe)name.loc[:,[column1,column2]] -> this will return all rows but only two columns.

23. We can drop a row or column using the following syntax:
    dataframe_name.drop(column/row name, axis = 0/1)

24. We can also write complex queries with the help of LOC:
    dataframe_name.loc[(dataframe_name[column_name/row_name]>some value)]   -> Here we can apply any condition and get the value of our requirement.
    dataframe_name.loc[(dataframe_name[column_name/row_name]>some value) & (dataframe_name[column_name/row_name]<some value) ]  -> multiple queries can also be run in one line using the & operator.
    Check Jupyter for code.

25. We want to grab a data point using rows and column names of the dataframe then use loc but if you want to use only the default indexing in order to grab the data the use iloc
    dataframe_name.iloc[(0,4)] -> This will return the data which is present at 0th row and 4th column. Here 0 and 4 are not the actual names of the rows and columns.

26. if a function has an inplace attribute and we set it to True then the changes that are made to the dataframe will happen "inplace". This will change the original dataframe in realtime and
    no copy of the dataframe would be needed.

27. After all the data manipulations if the index is not consistent then we can use the following function which will add an default index column to the dataframe
    which we can keep and delete the distorted index column by setting drop attribute in the reset_index() to True
    Syntax : dataframe_name.reset_index(drop=True)

28. dataframe_name.dropna() will drop all the NA from the dataframe

29. To drop all the duplicates from the dataframe dataframe_name.drop_duplicates(). Also check the latest functions in pandas online to perform any functions.

30. dataframe[column/row_name].isnull() - this will return True where ever there is a null value.

31. Go through pandas documentation to know about any function that you might be needing.
'''

import numpy as np
import pandas as pd

#step1
dict1 = {'name': ['harry','shagun','gunjan'],'marks':[12,34,65],'city':['kolkata','delhi','goa']}
df = pd.DataFrame(dict1) #DataFrame is written in camel casing
print(df)

#step2
print(df.describe())

