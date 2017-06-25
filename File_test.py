def getFileData(fname):
    with open(fname) as f:
        content = f.readlines() 
    a, b = zip(*(s.strip('\n').split(",") for s in content))
    #Typecasts touples to lists for return
    return [list(a), list(b)]
    
    
filen = "Data/example.txt"
a = getFileData(filen)
print(a[0])
print(a[1])
