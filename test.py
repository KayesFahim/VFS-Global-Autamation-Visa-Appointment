import imaplib
import email
import html2text
import re
import json


host = 'imap.gmail.com'
username = 'mrfawbd@gmail.com'
password = '@Kayes321'


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'ALL', '(SUBJECT "OTP Confirmation Email")')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
        my_message.append(email_data)
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    h = html2text.HTML2Text()
    h.ignore_links = True
    listToStr = ' '.join(map(str, my_inbox))
    PlainText = h.handle(listToStr)
    result = json.dumps(PlainText)
    getOTP = re.findall('\d+', result)
    finalOTP = ' '.join(map(str, getOTP))
    print(int(finalOTP))

