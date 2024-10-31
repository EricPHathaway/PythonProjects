print('To encode or decode, type "enCode()" or "deCode()"')
import random
def enCode():
    ps = str(input('What would you like to encode? '))
    key = random.randint(0,25)
    psa = ps.lower()
    rng = len(ps)
    psn = ''
    for x in range(rng):
        a = ord(ps[x])
        if a <= 96 or a >= 123:
            psn = psn + psa[x]
        else:
            a = (219-a)
            a = a + key
            if a >= 123:
                a = a-26
            psn = psn + chr(a)
    print('The encoded message is "'+psn+'" and the key is '+str(key)+'.')

def deCode():
    pse = str(input('What is the encoded phrase? '))
    key = int(input('What is the key? '))
    rng = len(pse)
    psd = ''
    for x in range(rng):
        a = ord(pse[x])
        if a <= 96 or a >= 123:
            psd = psd + pse[x]
        else:
            a = a - key
            if a <= 96:
                a = a +26
            a = (219-a)
            psd = psd + chr(a)
    print(psd)
