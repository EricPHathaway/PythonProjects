def anagramTest():#this is the function that tests for anagrams
    ips = str(input('What phrase would you like to check for anagrams? '))#takes an input
    key = wordConverter(ips,ips)#converts the input to a key that will be checked against

    fout = open('dictionary.txt', 'r')#opens a list of 58000 english words
    words = fout.read()
    wlist = words.split('\n')#seperates each word into its own item in a list called wlist

    for i in range(len(wlist)):#this for loop converts each word into something that can be compared with the input
        wlist[i] = wordConverter(wlist[i],wlist[i])

    n = len(wlist)
    
    for i in range(len(wlist)):#this for loop gets rid of all of the words that could not possibly be an anagram with the imput. doing this saves a lot of time.
        if pCheck(wlist[((n-i)-1)],key) == False:
            del wlist[((n-i)-1)]

    print(key[27])

    for i in range(len(wlist)):#this for loop checks for single words that could be an anagram
        if tCheck(wlist[i],key) == True:
            print(wlist[i][26])

    for a in range(len(wlist)):#this for loop checks for two words that could be an anagram
        for b in range(a,len(wlist)):
            if tCheck(letterAdder(wlist[a],wlist[b]),key) == True:
                print(str(wlist[a][26])+' '+str(wlist[b][26]))

    for a in range(len(wlist)):#this for loop checks fo three words
        for b in range(a,len(wlist)):
            if (pCheck(letterAdder(wlist[a],wlist[b]), key) == True) and (wlist[a][27] + wlist[b][27] < key[27]):
                for c in range(b,len(wlist)):
                    if int(wlist[a][27]) + int(wlist[b][27]) + int(wlist[c][27]) == int(key[27]):
                        if tCheck(letterAdder(wlist[a],letterAdder(wlist[b], wlist[c])),key) == True:
                            print(str(wlist[a][26])+' '+str(wlist[b][26])+' '+str(wlist[c][26]))
    for a in range(len(wlist)):#this for loop checks for four words.
        for b in range(a,len(wlist)):
            if (pCheck(letterAdder(wlist[a],wlist[b]), key) == True) and (wlist[a][27] + wlist[b][27] < key[27]):
                for c in range(b,len(wlist)):
                    if pCheck(letterAdder(wlist[a],wlist[c]), key) == True and pCheck(letterAdder(wlist[b],wlist[c]), key) == True and pCheck(letterAdder(letterAdder(wlist[b],wlist[c]),wlist[a]), key) == True and (wlist[a][27] + wlist[b][27] + wlist[c][27] < key[27]):
                        for d in range(c,len(wlist)):
                            if tCheck(letterAdder(letterAdder(wlist[a],wlist[d]),letterAdder(wlist[b], wlist[c])),key) == True:
                                print(str(wlist[a][26])+' '+str(wlist[b][26])+' '+str(wlist[c][26])+' '+str(wlist[d][26]))
        
    

def wordConverter(ps,p):#this function saves each word input as a list of how many of each character are in a word as well as the original word.
    letterCount = 0
    olt = []
    for i in range(26):
        ltc = 0
        for x in(ps):
            if x == chr(97+i):
                ltc = ltc + 1
                letterCount = letterCount + 1
        olt = olt + [ltc]
        
    olt = olt + [p]
    olt = olt + [letterCount]
    return olt

def letterAdder(c1,c2):#this function adds togerther two lists that represent words that have been put in the wordConverter function
    co = []
    for i in range(26):
        co = co + [c1[i]+c2[i]]
    return co

def pCheck(c,key):#this function checks to see if it is possible for a word to be part of an anagram for the original phrase
    for i in range(26):
        if c[i] > key[i]:
            return False
    else:
        return True

def tCheck(c,key):#this function checks if the original phrase is an anagram for another word or phrase
    for i in range(26):
        if c[i] != key[i]:
            return False
    else:
        return True

def spellingBeeTest(phs, key):
    letterCount = 0
    for i in range(26):
        letterCount += phs[i]
        if ((key[i] == 0) and phs[i] != 0):
            return False
    if (phs[ord(key[26][0])-97] == 0):
        return False
    if letterCount < 4:
        return False
    else:
        return True

def search():
    sw = input('What word would you like to search for? ')
    fout = open('dictionary.txt', 'r')#opens a list of 58000 english words
    words = fout.read()
    wlist = words.split('\n')
    if sw in wlist:
        print('That word is in the list!'+'\n')
    else:
        print('That word in not in the list.'+'\n')



def spellingBee():
    ips = str(input('What phrase would you like to check for Spelling Bee? '))
    key = wordConverter(ips,ips)

    fout = open('dictionary.txt', 'r')#opens a list of 58000 english words
    words = fout.read()
    wlist = words.split('\n')#seperates each word into its own item in a list called wlist

    for i in range(len(wlist)):#this for loop converts each word into something that can be compared with the input
        wlist[i] = wordConverter(wlist[i],wlist[i])

    n = len(wlist)

    for i in range(len(wlist)):
        if spellingBeeTest(wlist[i],key) == True:
            print(wlist[i][26])

def letterBoxedKey(key, ips):
    box = []
    for i in range(0,3):
        key[ord(ips[i])-97] = 'a'
    for i in range(3,6):
        key[ord(ips[i])-97] = 'b'
    for i in range(6,9):
        key[ord(ips[i])-97] = 'c'
    for i in range(9,12):
        key[ord(ips[i])-97] = 'd'
    return key

def letterBoxedCheck(phs, key, box):
    letterCount = 0
    for i in range(26):
        letterCount += phs[i]
        if ((key[i] == 0) and phs[i] != 0):
            return False
    if letterCount < 3:
        return False
    for i in range(len(phs[26])-1):
        if(box[ord(phs[26][i])-97] == box[ord(phs[26][i+1])-97]):
            return False
    else:
        return True

def uniCheck(aps,bps):
    lc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    uniCount = 0
    for i in range(len(aps)):
        lc[ord(aps[i])-97] += 1
    for i in range(len(bps)):
        lc[ord(bps[i])-97] += 1
    for i in range(26):
        if (lc[i] >= 1):
            uniCount = uniCount + 1
    if(aps[0] != bps[-1] and bps[0] != aps[-1]):
        return False
    if (uniCount == 12):
        return True
    else:
        return False

    
def dictionaryCheck(dictionary, box):
    solved = False
    for a in range(len(dictionary)):
        for b in range(a, len(dictionary)):
            if uniCheck(dictionary[a],dictionary[b]):
                solved = True
                print(str(dictionary[a]) + ' ' + str(dictionary[b]))
    if solved == False:
        for a in range(len(dictionary)):
            for b in range(a, len(dictionary)):
                for c in range(b, len(dictionary)):
                    if uniCheck(letterAdder(dictionary[a], dictionary[b]), dictionary[c]):
                        print(str(dictionary[a]) + ' ' + str(dictionary[b]) + ' ' + str(dictionary[c]))
            


def letterBoxed():
    ips = str(input('What phrase would you like to check for Letter Boxed? '))
    key = wordConverter(ips,ips)

    fout = open('dictionary.txt', 'r')#opens a list of 58000 english words
    words = fout.read()
    wlist = words.split('\n')#seperates each word into its own item in a list called wlist

    for i in range(len(wlist)):#this for loop converts each word into something that can be compared with the input
        wlist[i] = wordConverter(wlist[i],wlist[i])

    n = len(wlist)

    box = letterBoxedKey(key, ips)

    dictionary = []
    
    for i in range(len(wlist)):
        if letterBoxedCheck(wlist[i], key, box) == True:
            dictionary = dictionary + [wlist[i][26]]
    dictionaryCheck(dictionary, box)
    
        

            
while True:
    tsk = input(str('If you would like to find an anagram, press "a", then "enter". To search to see if a word is in the dictionary, press "s", then "enter". To cheat at the NYT spelling Bee, press "b". To cheat at the NYT Letter Boxed, press"l"  '))
    if tsk == 'a':
        anagramTest()
    if tsk == 's':
        search()
    if tsk == 'b':
        spellingBee()
    if tsk == 'l':
        letterBoxed()








    

