import smtplib


EMAIL_HOST_USER = 'epicstone637@gmail.com'
EMAIL_HOST_PASSWORD = 'vbshwwzxhjdqyzid'

def send_email_to_student(fname,email,enrolmentID):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            body = f"subject:Successfull Enrolment in Dummy School \n\n\nDear {fname},\n\nYou got enroll in Dummy School your Enrollment ID is {enrolmentID} let's provide us the "+ \
            "hard copies for the future references.\n\n\nTeam\nDummy School"
            connection.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD )
            connection.sendmail(from_addr=EMAIL_HOST_USER, to_addrs=str(email),msg=body)
            connection.close()
            return True
    except Exception as e:
        print(e)

def send_email_to_admin(stdName,clsName,sectionId,enrolmentId,sessionId):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:

            body = f"subject:A New Student Enrolled \n\n\nDear Admin,\n\n\n You got new student {stdName } enrolledin class {clsName}," + \
                f"section {sectionId} with enrollment id {enrolmentId} this in {sessionId} session.\n\n\n Bot Msg."
            connection.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD )
            res = connection.sendmail(from_addr=EMAIL_HOST_USER, to_addrs='durganand.jha@habrie.com',msg=body)
            print("res",res)
            connection.close()
            return True


    except Exception as e:
        print(e)


# send_email_to_student('JA1CK','S2S113')
# send_email_to_admin("j2ack","X11","S2S11","ENT1211","SES11")

