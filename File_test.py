import os

def getFileData(fname):
    with open(fname) as f:
        content = f.readlines() 
    a, b = zip(*(s.strip('\n').split(",") for s in content))
    #Typecasts touples to lists for return
    return [list(a), list(b)]

def datasetBuilder(fstart, fstop, label, dataset=[]):
    baseName = "Data/output_#.txt"
    i = fstart
    while os.path.isfile(baseName.replace("#", str(i))):
        print(i)
        data = getFileData(baseName.replace("#", str(i)))
        dataset = getSlices(data,label,dataset)
        if i == fstop:
            i = "End"
        else:
            i += 1


    
d = datasetBuilder(1, 10, [1,0])
print(d)
