# import pandas as pd

# # Create Excel file file with python and pnadas using xlsxwriter engine
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# writer.close()

# # Create Excel Sheet from python dictionary
# df =  pd.DataFrame({'Name':['A','B','C','D'], 'Age':[10,0,30,50]})
# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='sheet1', index=False)
# writer.close()

# Read Excel file with python pandas
# reader = pd.read_excel(r'demo.xlsx')
# print(reader)

# Add new data to excelsheet with python
# import pandas as pd
# from openpyxl import load_workbook

# df = pd.DataFrame({'Name':['E','F','G','H','I'], 'Age':[100,70,40,60,70]})
# writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')
# # open an existing workbook
# writer.book = load_workbook('demo.xlsx')
# # copy an existing sheets
# writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# # read existing file
# reader = pd.read_excel(r'demo.xlsx')
# # writer out the new sheet
# df.to_excel(writer, index=False, header=False, startnow=len(reader) + 1)
# writer.close()


# How to Create csv file with python/pandas
import pandas as pd
technology = {
    'python':['Django','Flask','Django-celery','Django-Htmx'],
    'fee' : [100, 200, 300, 400],
    'duration' : ['30days','20days','10days','5days'],
    'discount':[50,40,30,20],
}
df = pd.DataFrame(technology)
print(df)
df.to_csv('csvdemo.csv')