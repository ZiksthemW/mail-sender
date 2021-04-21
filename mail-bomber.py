import smtplib
cizgi = "-" * 15
servis_girildi = False
mail_gonderildi = 0

while not servis_girildi:
    mail_servisi = int(input(f"""{cizgi}
    Services: (1) GMail / (2) Yahoo / (3) Outlook / (4) Yandex Mail
        Choose the service that you want to use <> """))

    if mail_servisi <= 0 or mail_servisi >= 5:
        print(f"{cizgi}\nIncorrect entry. Please choose between (1) and (4).")
    else:
        servis_girildi = True

mail_gonderilecek = int(input(f"{cizgi}\nHow much times do you want to spam? <> "))
mail_kadi = str(input(f"{cizgi}\nYour Mail Address <> "))
mail_pass = str(input(f"{cizgi}\nYour Mail Password <> "))
mail_alici = str(input(f"{cizgi}\nMail Receiver <> "))
mail_baslik = str(input(f"{cizgi}\nMail Subject <> "))
mail_icerik = str(input(f"{cizgi}\nWITHOUT FILE EXTENSION.\nInput the .txt file that has the mail content <> "))
print(cizgi)

if not mail_gonderilecek or mail_kadi or mail_pass or mail_alici or mail_baslik or mail_icerik == None: # Will change there soon.
    with open(mail_icerik + ".txt", "r", encoding="utf-8") as mail_icerik:
        mail_icerik_veri = mail_icerik.read()
        mail_icerik_veri = f"""SUBJECT: {mail_baslik}\n{mail_icerik_veri}"""

    while mail_gonderilecek > mail_gonderildi:
        if mail_servisi == 1:
            mail = smtplib.SMTP("smtp.gmail.com",587)
        elif mail_servisi == 2:
            mail = smtplib.SMTP("smtp.mail.yahoo.com",587)
        elif mail_servisi == 3:
            mail = smtplib.SMTP("smtp-mail.outlook.com",587)
        elif mail_servisi == 4:
            mail = smtplib.SMTP("smtp.yandex.ru",587)
            
        mail.ehlo()
        mail.starttls()
        mail.login(mail_kadi, mail_pass)
        mail.sendmail(mail_baslik, mail_alici, mail_icerik_veri)
        print(f"Successfully sent the mail. {mail_gonderilecek - mail_gonderildi} Mails left to send")
        mail_gonderildi += 1

    print(f"{cizgi}\nSuccessfully sent {mail_gonderildi} mails.")

else:
    print(f"{cizgi}\nMissing information provided.")
