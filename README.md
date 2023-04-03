# Email Tagging

A daily automated email is received and automatically moved to the "Tagging" folder within outlook. This email is auto generated and contains data in a tabular structure, but is not sent with an HTML table. This script is automatically run at the end of every month to extract that data from each email and concatenate into one csv file. It only extracts unread emails and after the data is extracted, marks the email as read so it does not pick it up in future runs.
