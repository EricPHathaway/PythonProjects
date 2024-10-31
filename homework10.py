tdl = []

def addItem(Item, pos):
    global tdl
    tdll = tdl
    if pos >= len(tdl):
        tdll = tdll + [Item]
        print(str(Item)+' added to postion '+str(len(tdl))+'.')
    else:
        tdll[pos] = Item
        print(str(Item)+' added to postion '+str(pos)+'.')
    tdl = tdll

def printList():
    print(tdl)

def removeItem(Item):
    global tdl
    for i in range(0, len(tdl)):
        if Item == tdl[i]:
            del tdl[i]
            print(str(Item)+' was deleted from the list.')
            break
    else:
        print(str(Item)+' was not found in the list.')
