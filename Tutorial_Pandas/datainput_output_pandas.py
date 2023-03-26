'''
1. In order to work with CSV, Excel, HTML and SQL files in the Python we need to install BeautifulSoup4,lxml,html5lib,
sqlalchemy
2. The files should be stored where the python is installed.
3. To read a CSV file run command - pd.read_csv('name_of_CSV'). We can read various variety of files by the same command
just the file type will change in the command mentioned above. eg. pd.read_sql('file_name')
4. In order to write to a dataframe we can use command dataframe.to_filetype
5. If we want to write something to a CSV file, we can use the command datframe.to_CSV('new_dataframe',index = False).
We need to set the Index to False else there will be a duplicate index column which will be added to the resultant dataframe.
6. Excel - Python can only import the data from the excel and not formulas applied etc. In order to read an excel file we
can use pd.read_excel('file_name',sheet_name='Sheet_of the workbook')
7. Use this command in order to write to an excel sheet - df.to_excel('New_file_name', sheet_name = 'nameofthe_newsheet')
8. In order to read an html file we can run command - pd.read_html('link_of _the_htmlfile'). This command will return
all the tables present in the HTML file as a list. By indexing we can obtain the table that we need. Python will try to
read the best that it could, there might be some null values left. For writing the same syntax is followed as above
9. There are specific libraries in pandas that work with different types of SQL engines. For postgreSQL there is psycopg2
# note: did not understand the 9th point
'''
import pandas as pd

