#Smartbell
#Program to handle JSON data
#Basically, a practice framework for talking to the web server
#Using example data from 'Databae'

#Imported libraries
import json
import datetime, time

#Descriptor object handling JSON data
#Currently only standard descriptors
#Will be updated to fit our ADT needs
class jsonDesc(object):
    #Descriptor Definitions:
    #Instantiated as list
    def __init__(self):
        self.values = []    
    #Sets data to input data
    def __set__(self, obj, setData):
        self.values = []
    #Gets data from class
    def __get__(self, instance, owner):
        return self.values
    #Deletes current data
    def __del__(self):
        del self.values
    #Called when printing data
    def __repr__(self):
        return self.values
    
#Main object, instantiates 'data' from jsonDesc
class jsonHolder(object):
    #Defined constructor
    #Takes 0 OR 1 args (More args ignored but no exception thrown)
    #Inits data as empty OR parses JSON
    def __init__(self, *args):
        #This may do nothing
        self.data = jsonDesc()
        if args:
            try:
                self.data = json.loads(args[0])
            except json.decoder.JSONDecodeError:
                print("Invalid JSON argument passed! Initialised as empty.")

    #Getters / Setters
    def setJson(self, setData):
        self.data = json.loads(setData)
    def getJson(self):
        return json.dumps(self.data)
    
    #print utility; printing:
    def printer(self, *args):
        #Prints all values of stored key
        if args:
            for x in self.data:
                try:
                    print(x[args[0]])
                except KeyError:
                    print("Key not found in this item")
        #Prints all items
        else:
            for x in self.data:
                print(x)

    #search utility; basic searching:
    #Returns list of results by key and/or query
    def search(self, key, value):
        resultList = []
        for x in self.data:
            if (x[key] == value):
                resultList.append(x)
        return resultList

    #filter utility; essentially layered basic searching:
    #Takes keyvalue pair and optional bool arg for OR / AND filter (Default OR)
    #Returns list of results
    def filter(self, layer=False, **qargs):
        resultList = []
        filterCheck = 0
        if qargs:
            for x in self.data:
                for key, value in qargs.items():
                    if layer:
                        if (x[str(key)] == value):
                            filterCheck += 1
                        if (filterCheck == len(qargs)):
                            resultList.append(x)
                    else:
                        if (x[str(key)] == value):
                            resultList.append(x)
        return resultList

#Object containing JSON to be sent to server
#Data is formatted to be natively parsed in JavaScript
class jsonOutput(object):
    
    #Returns current time in JS format
    def getDate():
        d = datetime.datetime.utcnow()
        #Remember! JS takes miliseconds, Python gives seconds.
        return int(time.mktime(d.timetuple())) * 1000 #Sec*1000 = MilSec

    #Gets unique ID of RaspPi from its CPU ID
    #WARNING: Attempts file handling. If this object is heavily used, REFACTOR THIS.
    def getSerial():
        #Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo','r')
            for line in f:
                if line[0:6]=='Serial':
                    cpuserial = line[10:26]
            f.close()
        except:
            cpuserial = "ERROR000000000"
        #return cpuserial
        return 'serialID' #Placeholder until I'm on a Pi
        
    #Disgusting lines to format into JSON
    #TBI = To Be Implimented
    formattedData = '[{"dumbbell_id":"' + getSerial() + '","user_id":"' + 'TBI' + '",\"date\":' + str(getDate()) + ',\"workout\":\"' + 'TBI' + '\",\"reps\":' + '404' + ',\"form\":' + '404' + '}]'
    formattedData = str(formattedData).strip("'<>() ").replace('\'', '\"')
    jsonData = json.loads(formattedData)

z = jsonOutput()
print(z.jsonData[0]["workout"])
