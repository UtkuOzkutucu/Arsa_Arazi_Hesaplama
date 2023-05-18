global Deniz_Kenari
global Sehir_Merkezi
global Kirsal
Deniz_Kenari = 1.6      #Bolge 1
Sehir_Merkezi = 1.2     #Bolge 2
Kirsal = 0.8            #Bolge 3

def ArsaCemberCevre(Yaricap):
    return 6 * Yaricap

def ArsaDikdortgenCevre(Dikey,Yatay):
    return 2 * (Dikey + Yatay)

def CemberFiyat(ArsaCemberCevre,Bolge_Katsayisi):
    return 1000* ArsaCemberCevre * Bolge_Katsayisi

def DikdorgenFiyat(ArsaDikdorgenCevre,Bolge_Katsayisi):
    return ArsaDikdorgenCevre * Bolge_Katsayisi * 1000