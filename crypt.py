#
#cryptorn - Tamamen hobi amaçlı eğlencesine denenmiştir.
#
import hashlib

password = "Bismillah :)"
myhash = hashlib.sha256(password.encode("utf-8")).hexdigest()

def changeChar(achar,key):
    ch = ord(achar)^ord(key)
    return chr(ch)

#Test-OK!
#print(changeChar("Ş","c"))
#print(changeChar(changeChar("Ş","c"),"c"))


def cryptStr(_msg, _hash):
    keyArray = []
    cryptMsgTmp = []
    cryptMsg = ''

    # for ch in myhash:
    #     keyArray.append(chr(ch.encode("utf-8")))
    
    #Test-OK!
    # print(changeChar("Ş", _hash[3]))
    # print(changeChar(changeChar("Ş", _hash[3]), _hash[3]))
    # print(_hash[3])

    i=0
    for cha in _msg:
        cryptMsgTmp.append(changeChar(cha,_hash[(i*i)%len(_hash)]));i = i+1 
    cryptMsg = ''.join(cryptMsgTmp)

    return cryptMsg
#print(changeChar(45,34))
#print(changeChar(changeChar(45,34),34))

print(cryptStr("Selamünaleyküm hacı osman nabin nası gidii?(Giresun Ağzı)",myhash))
print(cryptStr(cryptStr("Selamünaleyküm hacı osman nabin nası gidii?(Giresun Ağzı)",myhash),myhash))
