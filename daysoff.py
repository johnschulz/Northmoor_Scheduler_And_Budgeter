from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

service = build('sheets', 'v4', http=creds.authorize(Http()))
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1YACoZ05IEhpOvqXFudKqa20iApdJTv90t2fpG-aEytc/edit#gid=0').sheet1
SPREADSHEET_ID = '1YACoZ05IEhpOvqXFudKqa20iApdJTv90t2fpG-aEytc'
RANGE_NAME = 'Sheet1!A3:N'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
daysoff = {"Jack": ["Friday", "Saturday", "Sunday"], "Caroline":[], "Lily and Lindsay(closing only)":["Sunday", "Tuesday", "Thursday", "Saturday"],"Lily":["Monday", "Wednesday", "Friday", "Saturday", "Sunday", "June 23 2018", "July 10 2018", "July 12 2018", "July 20 2018", "August 2 2018", "August 3 2018", "August 4 2018", "August 5 2018"], "Jake":["All", "June 11 2018", "June 19 2018"],"Julia":["All"], "Jared":["All","June 9 2018","June 14 2018","June 15 2018","June 16 2018","June 17 2018","June 18 2018","June 19 2018","June 20 2018","June 21 2018","June 22 2018"], "John":[],"Amy":["All"], "Justin":["All"],"Tyler":["All","Friday", "Saturday", "Sunday", "June 12 2018","June 13 2018","June 21 2018"],"Sloane":["All"], "Colby":["June 11 2018","June 12 2018","June 13 2018","June 14 2018","June 15 2018","June 16 2018","June 22 2018","June 23 2018","June 24 2018", "July 7 2018", "July 8 2018", "July 12 2018", "July 13 2018", "July 14 2018", "July 20 2018", "July 21 2018", "July 22 2018","July 23 2018","July 24 2018","July 25 2018","July 26 2018","July 27 2018","July 28 2018","July 29 2018","August 4 2018","August 10 2018","August 11 2018","August 12 2018","August 13 2018","August 14 2018","August 15 2018","August 16 2018"], "Lindsay":["Monday", "Wednesday", "Friday", "June 9 2018","June 10 2018","June 15 2018","June 16 2018", "June 17 2018","June 28 2018","June 29 2018","June 30 2018","July 1 2018","August 3 2018","August 4 2018", "August 5 2018", "August 6 2018"], "Will": ["June 9 2018"],"Sam":["June 9 2018", "July 2 2018", "July 3 2018", "July 4 2018", "July 5 2018", "July 6 2018", "July 7 2018", "August 2 2018", "August 3 2018", "August 4 2018", "August 5 2018"], "Cody":["All"]}

specific = list(daysoff.values())
names = list(daysoff.keys())
week = []
for x in range(0, 20)[::3]:
    week.append(values[x][0])
print(week)
monthly = []
indices = [3, 6, 9, 12, 15, 18, 21]
for index in range(0, 6):
    additions = []
    print(week[index])
    for x in range(0, 16):
        if week[index] not in specific[x] not in specific[x] and "All" not in specific[x]:
            print(names[x])
            additions.append(names[x])
            print(sheet.cell(1, 7).value)
    sheet.update_cell(indices[index],7 ,str(additions))
