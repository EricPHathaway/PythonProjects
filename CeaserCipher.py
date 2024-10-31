def listConverter(oplist):
    optext = ""
    for i in range(len(oplist)):
        optext += oplist[i]
    return optext
def keyConverter(ipkey, iptextLength):
    opKey = ""
    for i in range(iptextLength):
        opKey += ipkey[i%len(ipkey)]
    return opKey

while True:
    cipherInput = str(input('What cipher are you using? "c" for ceaser, "v" for vigenere: '))
    if(cipherInput == "c"):
        purposeInput = str(input('type "e" for encryption or "d" for decryption '))
        if(purposeInput == "e"):
            iptext = str(input('What would you like to encrypt? ')).lower()
            ipkey = int(input('What is the key? '))
            oplist = []
            for i in range(len(iptext)):
                oplist += chr(ord(iptext[i])+ipkey)
            for i in range(len(oplist)):
                if(ord(oplist[i])<97):
                    oplist[i] = chr(ord(oplist[i])+26)
                if(ord(oplist[i])>122):
                    print(chr(ord(oplist[i])-26))
                    oplist[i] = chr(ord(oplist[i])-26)
            print(listConverter(oplist))
        if(purposeInput == "d"):
            iptext = str(input('What would you like to decrypt? ')).lower()
            ipkey = int(input('What is the key? '))
            oplist = []
            for i in range(len(iptext)):
                oplist += chr(ord(iptext[i])-ipkey)
            for i in range(len(oplist)):
                if(ord(oplist[i])<97):
                    oplist[i] = chr(ord(oplist[i])+26)
                if(ord(oplist[i])>122):
                    oplist[i] = chr(ord(oplist[i])-26)
            print(listConverter(oplist))
    if(cipherInput == "v"):
        purposeInput = str(input('type "e" for encryption or "d" for decryption '))
        if(purposeInput == "e"):
            iptext = str(input('What would you like to encrypt? ')).replace(" ","").lower()
            ipkey = str(input('What is the key? ')).lower()
            realKey = keyConverter(ipkey, len(iptext))
            oplist = []
            for i in range(len(iptext)):
                oplist += chr(ord(iptext[i])+(ord(realKey[i])-97))
            for i in range(len(oplist)):
                if(ord(oplist[i])<97):
                    oplist[i] = chr(ord(oplist[i])+26)
                if(ord(oplist[i])>122):
                    print(chr(ord(oplist[i])-26))
                    oplist[i] = chr(ord(oplist[i])-26)
            print(listConverter(oplist))
        if(purposeInput == "d"):
            iptext = str(input('What would you like to decrypt? ')).replace(" ","").lower()
            ipkey = str(input('What is the key? ')).lower()
            realKey = keyConverter(ipkey, len(iptext))
            oplist = []
            for i in range(len(iptext)):
                oplist += chr(ord(iptext[i])-(ord(realKey[i])-97))
            for i in range(len(oplist)):
                if(ord(oplist[i])<97):
                    oplist[i] = chr(ord(oplist[i])+26)
                if(ord(oplist[i])>122):
                    oplist[i] = chr(ord(oplist[i])-26)
            print(listConverter(oplist))





    
