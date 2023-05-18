import arsa
import daire

while True: #dongu baslatma
    Secenek = int(input("Lutfen Fiyatini Ogrenmek Istediginizi Seciniz[Arsa icin 1, Daire icin 2, Cikis icin 0]:"))
    if Secenek == 0:
        break
    if Secenek not in [1,2]:
        print("Secenek 1 ve 2 Olmalidir. Tekrar Deneyiniz.")
        Tekrar = "e"
        continue
    print("")

    if Secenek == 1:

        while True:
            Hangi_Bolge = int(input("Arsa Bolgesini Giriniz[1 Deniz Kenari, 2 Sehir Merkezi, 3 Kirsal]:"))  # Bolge Secimi
            print("")
            if Hangi_Bolge == 1:
                Bolge = arsa.Deniz_Kenari
                break
            elif Hangi_Bolge == 2:
                Bolge = arsa.Sehir_Merkezi
                break
            elif Hangi_Bolge == 3:
                Bolge = arsa.Kirsal
                break
            else:
                print("Sayi 1,2 veya 3 olmalidir.")
                print("")
        while True:
            ArsaSekli = int(input("Arsa Seklini Seciniz[Cember Arsa icin 1, Dikdortgen Arsa icin 2]:"))
            print("")
            if ArsaSekli == 1: #Cember Olan Arsa

                Yaricap = int(input("Yaricap Ne Kadar Olmali:"))
                Cevre = arsa.ArsaCemberCevre(Yaricap)
                print("Bolge Katsayisi:", Bolge)
                print("Cevre:", Cevre)
                print("Arsa Fiyati:", (arsa.CemberFiyat(Cevre, Bolge)))
                break
            elif ArsaSekli == 2: #Dikdortgen Olan Arsa

                Dikey = int(input("Dikey Boyut:"))
                Yatay = int(input("Yatay Boyut:"))
                Cevre = arsa.ArsaDikdortgenCevre(Dikey,Yatay)
                print("Bolge Katsayisi:", Bolge)
                print("Cevre:",Cevre)
                print("Arsa Fiyat:", (arsa.DikdorgenFiyat(Cevre,Bolge)))
                break
            else:
                print("Arsa Sekli 1 veya 2 olmalidir.")
                print("")

    elif Secenek == 2: #Daire Secenegi


        while True:
            Hangi_Kat = int(input("Kati Giriniz[1 Ara Kat icin,2 Ust Kat, 3 Zemin Kat]:"))
            print("")
            if Hangi_Kat == 1:
                Kat = daire.Ara_Kat_Katsayisi
                break
            elif Hangi_Kat == 2:
                Kat = daire.Ust_Kat_Katsayisi
                break
            elif Hangi_Kat == 3:
                Kat = daire.Zemin_Kat_Katsayisi
                break
            else:
                print("Kat Sayiniz 1,2 veya 3 Olmalidir")
                print("")

        Dikey = int(input("Dikey Boyut:"))
        Yatay = int(input("Yatay Boyut:"))
        Alan= daire.hesapla_daire_alani(Dikey,Yatay)
        print("Daire Metrekaresi:",Alan)
        print("Daire Fiyati:", daire.hesapla_fiyat(Kat,Alan))


    


