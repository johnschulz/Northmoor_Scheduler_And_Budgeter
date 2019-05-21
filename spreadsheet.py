from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

service = build('sheets', 'v4', http=creds.authorize(Http()))
sheet = client.open('June 30 - July 6').sheet1
SPREADSHEET_ID = '1m_jHiNcwl3EJsO9NSdFORGekUwJGSoaKN0Ie7useQec'
RANGE_NAME = 'Sheet1!A3:N'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
for row in range(0, 20):
    for col in range(1, 6):
        schedule_name = values[row][col]
        if schedule_name:
            schedule_hour = values[21][col]
            print(schedule_name, schedule_hour)
            for name_depth in range(0,16):
                name = values[name_depth][8]
                if name == schedule_name:
                    sheet.update_cell(name_depth+3, 11, str(float(sheet.cell(name_depth+3, 11).value) + float(schedule_hour)))
