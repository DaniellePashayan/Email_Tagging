PHISH = "External Email.  Do not click links or open attachments unless you trust the sender and content.  Report suspicious emails using Report Phishing button or forward email to phish@northwell.edu"

HEADER = "Group    Invoice Number      Vendor              Tag Date    Action"

def splitter(table):
    """
    :param table: the table you want to split
    :return: each line as an array
    """
    data = []
    for line in table:
       info = "|".join(line.split())
       info = info.split('|')
       data.append(info)
    return data