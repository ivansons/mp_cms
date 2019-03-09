from __future__ import unicode_literals
import datetime
import io

from django.utils.timezone import now

from mezzanine.conf import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_trade_in_value(serial_number):
    if not (settings.GOOGLE_OAUTH2_CLIENT_EMAIL and
            settings.GOOGLE_OAUTH2_PRIVATE_KEY and
            settings.GOOGLE_SPREADSHEET_ID):
        return

    try:
        buffer = io.StringIO(
            settings.GOOGLE_OAUTH2_PRIVATE_KEY.replace('\\n', '\n'))
        credentials = ServiceAccountCredentials.from_p12_keyfile_buffer(
            service_account_email=settings.GOOGLE_OAUTH2_CLIENT_EMAIL,
            file_buffer=buffer,
            scopes=['https://spreadsheets.google.com/feeds'])
        gc = gspread.authorize(credentials)
        ws = gc.open_by_key(settings.GOOGLE_SPREADSHEET_ID).sheet1
        camera = ws.find(serial_number)
        cell_start = ws.find('Serial Number')
        dates = ws.row_values(cell_start.row)
        today = now().date()
        x = None
        for col in range(ws.col_count, 0, -1):
            try:
                if today <= datetime.datetime.strptime(dates[col - 1],
                                                       '%m/%d/%Y').date():
                    x = col
            except:
                pass
        return ws.cell(camera.row, x).value or None
    except:
        return
