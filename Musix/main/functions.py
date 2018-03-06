def uploadFile(file):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def generateMediaDirectoryName(username, folder):
    return "Musix/tracks/" + str(username) + "/" + str(folder)

def listToString(list):
    res = ""
    for i in range(len(list)):
        if i == len(list)-1:
            res = res + list[i]
        else:
            res = res + list[i] + ", "
    return res

def splitInstruments(string):
    res = ""
    del1 = string.split("[")
    del2 = del1[1].split("]")
    splt = del2[0].split("u'")

    for i in splt:
        if i is not splt[0]:
            if i is splt[len(splt)-1]:
                aux = i.split("'")
                res += aux[0]
            else:
                aux = i.split("'")
                res += aux[0] + ", "

    return res