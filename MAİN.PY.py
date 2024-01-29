print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI ")
boy = float(input("Boyunuzu girin : "))
kilo = float(input("Kilonuzu girin : "))
endex  = kilo/(boy*boy)

if endex <18:
    print("\n zayıf VKİ:{}".format(endex))
elif endex >= 18 and endex <25 :
    print("\n normal VKİ:{}".format(endex))
elif endex >= 25 and endex <30:
    print("\n kilolu VKİ:{}".format(endex))
elif endex >= 30 and endex <35:
    print("\n obez VKİ:{}".format(endex))
else:
    print("\n ciddi obez VKİ:{}".format(endex))