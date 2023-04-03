import win32com.client
import pandas as pd
import helper
import ctypes

if __name__ == '__main__':
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")
    inbox = mapi.GetDefaultFolder(6).Folders['Tagging']

    messages = inbox.Items

    df_all = pd.DataFrame(columns=['Group, Invoice Number, Tag, Date, Action'])

    all_dfs = []

    for mail in messages:
        email_date = mail.ReceivedTime.strftime('%m %d %Y')
        body = mail.Body
        body = body.replace(helper.HEADER, '').strip()
        body = body.replace(helper.PHISH, '').strip()
        table = body.splitlines()
        info = helper.splitter(table)
        df = pd.DataFrame(info)
        all_dfs.append(df)

    final = pd.concat(all_dfs)
    final.to_csv('M:\CPP-Data\CBO Westbury Managers\
    LEADERSHIP\Bot Folder\Dashboards\data\Tag Reports\Tagging Export.csv', index=False)
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(0, "Completed", "Main.py", 0)



