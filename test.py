import imaplib
import email
import html2text
import re
import json
from imapclient import IMAPClient
import email


host = 'imap.gmail.com'
username = 'mrfawbd@gmail.com'
password = '@Kayes321'

imap = imaplib.IMAP4_SSL(host)
imap.login(username, password)
imap.select("inbox")
_, search_data = imap.search(None, 'UNSEEN', '(SUBJECT "OTP Confirmation Email")')
my_message = []
for num in search_data[0].split():
    email_data = {}
    _, data = imap.fetch(num, '(RFC822)')
    # print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            email_data['body'] = body.decode()
    my_message.append(email_data)


h = html2text.HTML2Text()
h.ignore_links = True
listToStr = ' '.join(map(str, my_message))
PlainText = h.handle(listToStr)
result = json.dumps(PlainText)
getOTP = re.findall('\d+', result)
finalOTP = ' '.join(map(str, getOTP))
print(finalOTP)

#deeleted

status, message_id_list = imap.search(None, 'SUBJECT "OTP Confirmation Email"')
messages = message_id_list[0].split()

for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")
print("All selected mails have been deleted")

# delete all the selected messages 
imap.expunge()
# close the mailbox
imap.close()

# logout from the account
imap.logout()