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