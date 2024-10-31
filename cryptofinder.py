def cryptFinder():
    ips = str(input('What word would you like to check? '))
    key = wordSorter(ips)
    print(key)
    fout = open('dictionary.txt', 'r')
    words = fout.read()
    wlist = words.split('/n')
    n = len(wlist)
    for i in range(len(wlist)):
        if len(ips) != wlist[((n-i)-1)]:
            del wlist[((n-i)-1)]


def wordSorter(ku):
    kl = []
    for i in range(len(ku)):
        if ord(ku[i]) > 96 and ord(ku[i]) < 123:
            kl = kl + [[ku[i],i]]
    return kl


#def wordConverter(u,k):


#def pCheck(kl, pw):
    
    
