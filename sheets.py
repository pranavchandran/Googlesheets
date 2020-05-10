# googlesheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("testsheet").sheet1

data = sheet.get_all_records()

row = sheet.row_values(5)
# col = sheet.col_values(3)
cell = sheet.cell(1,2).value

# insertRow = ["Neethu","Pranav","Teacher"]
sheet.delete_rows(6,100)
# sheet.insert_rows(row,6)

# sheet.update_cell(3,2,"Nextlevel")
# print(row)

# numRows = sheet.row_count
# print(numRows)
# print(len(data))
# pprint(data)
# for x,y,z in data:
#     print(x,y,z)
# pprint(cell)


