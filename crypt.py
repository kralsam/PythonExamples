#
#cryptorn
#
import hashlib

myhash = hashlib.sha256('1234'.encode("utf-8")).hexdigest()

def changeChar(achar,key):
    ch = ord(achar)^ord(key)
    return chr(ch)

def cryptStr(msg,hash):
    keyArray = []
    cryptMsgTmp = []
    cryptMsg = ''

    for ch in myhash:
        keyArray.append(ch.encode("utf-8"))
    
    i=0
    for cha in msg:
        cryptMsgTmp.append(changeChar(cha.encode("utf-8"),keyArray[i%512]));i = i+1 
    
    cryptMsg = ''.join(cryptMsgTmp)

    return cryptMsg
#print(changeChar(45,34))
#print(changeChar(changeChar(45,34),34))

print(cryptStr("Selamunaleykum",myhash))
print(cryptStr(cryptStr("Selamunaleykum",myhash),myhash))
