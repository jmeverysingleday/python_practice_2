import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.naver.com"
SMTP_PORT = 465

sender_email = "nurang99@naver.com"
receiver_email = "ksjoon28@naver.com"

def sendEmail(addr):
	reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"

	# bool 함수 -> 내용이 있다면(X none) TRUE, 없다면(none) FALSE
	if bool(re.match(reg,addr)):
			smtp.send_message(message)
			print("정상적으로 메일이 발송되었습니다.")
	else:
			print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("김정민 practice4 이메일입니다.")

message["Subject"] = "김정민 practice4"
message["From"] = sender_email
message["To"] = receiver_email

with open("image.png", "rb") as image:
	image_file = image.read()

image_type = imghdr.what("image", image_file)
message.add_attachment(image_file, maintype = 'image', subtype = image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login(sender_email, "SKKYVR6RNT4G")
sendEmail(receiver_email)
smtp.quit()