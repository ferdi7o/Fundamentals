import re

metin = "Benim e-posta adresim: ornek@example.com"
desen = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # E-posta deseni

eslesme = re.search(desen, metin)
if eslesme:
    print("E-posta bulundu:", eslesme.group())
else:
    print("E-posta bulunamadı.")
