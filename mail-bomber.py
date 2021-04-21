import smtplib
cizgi = "-" * 15
servis_girildi = False
mail_gonderildi = 0

while not servis_girildi:
    mail_servisi = int(input(f"""{cizgi}
    Mevcut servisler: (1) GMail / (2) Yahoo / (3) Outlook / (4) Yandex Mail
        Kullanmak istediğiniz servisi <> """))

    if mail_servisi <= 0 or mail_servisi >= 5:
        print(f"{cizgi}\nHatalı giriş. Lütfen sadece (1) ila (4) arası giriş yapınız.")
    else:
        servis_girildi = True

mail_gonderilecek = int(input(f"{cizgi}\nKaç kere spam atmak istiyorsunuz? <> "))
mail_kadi = str(input(f"{cizgi}\nMail Adresiniz <> "))
mail_pass = str(input(f"{cizgi}\nMail Parolanız <> "))
mail_alici = str(input(f"{cizgi}\nMail Alıcısı <> "))
mail_baslik = str(input(f"{cizgi}\nMailiniz için konu başlığı giriniz <> "))
mail_icerik = str(input(f"{cizgi}\nSADECE DOSYA ADI GİRİLMELİ.\nMail içeriğinin bulunduğu .txt dosyasını belirtiniz <> "))
print(cizgi)

if not mail_gonderilecek or mail_kadi or mail_pass or mail_alici or mail_baslik or mail_icerik == None: # Burası bayağı uzun oldu, yakında daha kısası ile çözerim.
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
        print(f"Başarıyla yollandı. Kalan gönderim: {mail_gonderilecek - mail_gonderildi}")
        mail_gonderildi += 1

    print(f"{cizgi}\nMailler başarı ile {mail_gonderildi} kez gönderildi.")

else:
    print(f"{cizgi}\nEksik bilgi girildi.")
