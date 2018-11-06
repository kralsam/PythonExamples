msg = "   Hello Array!      "
print(msg[0:5])
print(msg.strip()) # bastaki ve sonraki bosluklari siliyormus!
print(msg.strip()[0:5]) # bastaki ve sonraki bosluklari siliyormus!

print(len(msg))
print(len(msg.strip()))
print(len(msg.strip()[0:5]))

#

print(msg.lower()) #karakterleri kucuk harf yazar
print(msg.upper()) #karakterleri buyuk harf yazar

#
print(msg.lower().replace("a","ae",1)) # Editorlerdeki replace işlemine girilen sayı kadar yapar
print(msg.lower().replace("a","ae",2))
print(msg.lower().replace("a","ae"))

#
print(msg.strip().split(" ")) # parantez içindeki ifadeye göre ayırır.

print("ığüşiöç")
