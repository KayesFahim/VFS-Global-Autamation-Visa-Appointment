import imaplib
import email
import html2text
import re
import json
import email


host = 'flyfarint.org'
username = 'a1@flyfarint.org'
password = '@Kayes321'

imap = imaplib.IMAP4_SSL(host)
imap.login(username, password)
imap.select("inbox")
_, search_data = imap.search(None, 'ALL', '(SUBJECT "WELCOME")')
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