mylist = ["ali", "veli", "ahmet", "mehmet"]
print(mylist)
#
print(len(mylist))
#

for i in mylist:
    print(i)

#

if "ali" in mylist:
    print("Ali bizim listede var.")
else:
    print("Ali bizim listede yok")

#
mylist.append("mahmut") # yeni item ekle
print(mylist)

#
myListCsize = []
for i in mylist:
    myListCsize.append(len(i))
print(myListCsize)

deneme = [[1, 2], [2], [3], [4]]
insanlar = {'isimler': ['soner', 'orhan'], 'soyisimler': ['bayram', 'yılmaz'], 'yaslar': [24, 29]}

print(insanlar['isimler']+insanlar['soyisimler'])