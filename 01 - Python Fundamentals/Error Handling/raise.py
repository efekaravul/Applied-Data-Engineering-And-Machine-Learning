def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Password must be at least 8 characters long")
    elif not re.search("[a-z]", psw):
        raise Exception("Şifre küçük harf içermeli")
    elif not re.search("[A-Z]", psw):
        raise Exception("Şifre büyük harf içermeli")
    elif not re.search("[0-9]", psw):
        raise Exception("Şifre rakam içermeli")
    elif not re.search("[_@$]", psw):
        raise Exception("Şifre özel karakter içermeli")
    elif re.search(" ", psw):
        raise Exception("Şifre boşluk içermemeli")

password = "123456Aa_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Şifre oluşturuldu.")