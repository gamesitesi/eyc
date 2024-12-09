class EYCDil:
    def __init__(self):
        self.degiskenler = {}  # Değişkenleri saklamak için bir sözlük

    def calistir(self, kod):
        satirlar = kod.split("\n")
        satirlar = [satir.strip() for satir in satirlar if satir.strip()]  # Boş satırları atla
        i = 0

        while i < len(satirlar):
            satir = satirlar[i]

            # Yazdırma komutu
            if satir.startswith("yaz"):
                ifade = satir[4:]  # yaz komutundan sonraki kısmı al
                if ifade.startswith('"') and ifade.endswith('"'):
                    print(ifade[1:-1])  # Tırnak içeriğini yazdır
                elif ifade in self.degiskenler:
                    print(self.degiskenler[ifade])  # Değişken değeri yazdır
                else:
                    print("Hata: Tanımsız değişken veya ifade:", ifade)

            # Değişken tanımlama
            elif "=" in satir:
                degisken, deger = satir.split("=")
                degisken = degisken.strip()
                deger = deger.strip()
                if deger.isdigit():  # Sayı mı?
                    self.degiskenler[degisken] = int(deger)
                elif deger.startswith('"') and deger.endswith('"'):  # Metin mi?
                    self.degiskenler[degisken] = deger[1:-1]
                else:
                    print("Hata: Geçersiz değer:", deger)

            i += 1
