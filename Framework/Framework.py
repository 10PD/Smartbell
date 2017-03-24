#Smartbell Framework
#A practice framework for talking to the web server

#Imported libraries
import json
import datetime, time

#Descriptor object handling JSON data
class jsonDesc(object):

    defaultString = '[{"dumbbell_id":"serialID","user_id":"TBI","date":1490320045000,"workout":"TBI","reps":404,"form":404}]'

    #Takes initialising string and optional error message
    #Returns self.data as JSON
    def setJson(self, string,errorMsg="Unable to parse JSON. Initialised as default."):
        try:
            string = str(string).strip("'<>() ").replace('\'', '\"')
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
            self.data = self.setJson(args[0])
        #2+ args, tries to join and parse into JSON
        else:
            self.data = setJson(','.join(x for x in args),"Unable to parse multiple args. Initialised as default.")
                
    #Sets data to input data, equals overload
    def __set__(self, instance, data):
        setJson(self, data)
    #Gets data from class
    def __get__(self, instance, owner):
        return self.data

#Object containing JSON to be sent to server
#Data is formatted to be natively parsed in JavaScript
class jsonOutput(object):
    
    #Returns current time in JS format
    def getDate():
        d = datetime.datetime.utcnow()
        #Remember! JS takes miliseconds, Python gives seconds.
        return int(time.mktime(d.timetuple())) * 1000 #Sec*1000 = MilSec

    #Gets unique ID of RaspPi from its CPU ID
    #WARNING: Attempts file handling. If jsonOutput object is heavily used, REFACTOR THIS.
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

    #Horrible concatenation of the JSON object
    #TBI will be updated with features when possible
    formattedData = '[{"dumbbell_id":"' + getSerial() + '","user_id":"' + 'TBI' + '",\"date\":' + str(getDate()) + ',\"workout\":\"' + 'TBI' + '\",\"reps\":' + '404' + ',\"form\":' + '404' + '}]'
    data = jsonDesc()
    data.setJson(formattedData)

#Creates output object for server    
z = jsonOutput()

