
import pandas as pd

excelFile = 'sample.xlsx'

df1 = pd.read_excel(excelFile, header=1)
# print(df1)
# print(df1.columns)

data = [3, 4]
df2 = pd.DataFrame(data, columns=['CategoryID'])
print(df2)

print(df1['CategoryID'].isin(df2['CategoryID']))

filtered_data = df1.loc[(df1['CategoryID'].isin(df2['CategoryID']))]

filtered_data.to_excel("result.xlsx")

# Pandas DataFrame.loc attribute access a group of rows and columns by label(s)
# or a boolean array in the given DataFrame.