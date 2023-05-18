Ara_Kat_Katsayisi = 2       #Katsayisi 1
Ust_Kat_Katsayisi = 1.6     #Katsayisi 2
Zemin_Kat_Katsayisi = 0.9   #Katsayisi 3

def hesapla_daire_alani(Dikey,Yatay):
    return Dikey * Yatay    

def hesapla_fiyat(kat_katsayisi, daire_alani):
    return kat_katsayisi * daire_alani * 5000