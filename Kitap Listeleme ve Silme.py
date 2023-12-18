kitap_listesi = ["Kuyucaklı Yusuf" , "İnce Memed" , "Balzac" , "Kürk Mantolu Madonna" , 
"İnce Memed" , "İki Şehrin Hikayesi" , "Türk Kültür Tarihi" , "İstanbul Hatırası" , "Dönüşüm" , 
"İnsan Ne İle Yaşar" , "Dönüşüm" , "İnsan Ne İle Yaşar", "Yer Altından Notlar" , "Karamazaof Kardeşler" , "İstanbul Hatırası"]
adet_bilgisi = {i:kitap_listesi.count(i) for i in set(kitap_listesi)}
kitaplar = set(kitap_listesi)
while True:
	print("""
	[1] Kitap adet Bilgilerini Göster
	[2] Bir Kitap Çıkar 
	[Q] Çıkış
	""")
	seçim = input("İşlemi Seçiniz: ")
	if seçim == "1":
		for i in adet_bilgisi.keys():
			print("Kitap: {:<30}Adet: {}".format(i , adet_bilgisi.get(i)))
	elif seçim == "2":
		kitap = input("Çıkarılacak Kitap: ")
		if kitap in kitaplar:
			if adet_bilgisi[kitap] > 1:
				adet_bilgisi[kitap] = adet_bilgisi[kitap] - 1
			else:
				kitaplar.discard(kitap)
				adet_bilgisi.pop(kitap)
		else:
			print("Kitap Mevcut Değil...")
	elif seçim == "q" or seçim == "Q":
		break
	else:
		print("Hatalı Giriş...")