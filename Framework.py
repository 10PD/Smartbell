#Smartbell Framework
#Provides a discreet datatype, 'jsonDesc(*args)',   
#takes string and parses to JSON, else declares as default.

#*Contains 'jsonOutput' object,
#will be used to build the packets sent to the server.


#Imported libraries
import json
import datetime, time
import requests

#Descriptor object handling JSON data
class jsonDesc(object):

    defaultString = '[{"dumbbell_id":"serialID","user_id":"TBI","date":0,"workout":"TBI","reps":404,"form":404}]'
    #Takes initialising string and optional error message
    #Returns self.data as JSON
    def setJson(self, string,errorMsg="Unable to parse JSON. Initialised as default."):
        try:
            self.data = json.loads(string)
        except json.decoder.JSONDecodeError:
            print(errorMsg)
            self.data = json.loads(self.defaultString)
            
    #Descriptor Definitions:
    def __init__(self, *args):
        #No args, default init
        if (len(args) == 0):
            self.data = json.loads(self.defaultString)
        #1 arg, takes string to parse to JSON
        elif (len(args) == 1):
            self.setJson(args[0])
        #2+ args, tries to join and parse into JSON
        else:
            tmp = ','.join(x for x in args)
            self.setJson(tmp,"Unable to parse multiple args. Initialised as default.")
                
    #Sets data to input data, equals overload
    def __set__(self, instance, data):
        setJson(self, data)
    #Gets data from class
    def __get__(self, instance, owner):
        #print(self.data)
        return self.data

#Object containing JSON to be sent to server
#Data is formatted to be natively parsed in JavaScript
class jsonOutput(object):
    
    #Returns current time in JS format
    def getDate():
        d = datetime.datetime.utcnow()
        #Remember! JS takes miliseconds, Python gives seconds.
        return int(time.mktime(d.timetuple())) * 1000 #Sec*1000 = MilSec

    #Horrible concatenation of the JSON object
    #TBI will be updated with features when possible
    formattedData = '[{"dumbbell_id":"01","user_id":"' + 'TBI' + '",\"date\":' + str(getDate()) + ',\"workout\":\"' + 'TBI' + '\",\"reps\":' + '404' + ',\"form\":' + '404' + '}]'
    data = jsonDesc(formattedData)

#Creates output object for server    
z = jsonOutput()

