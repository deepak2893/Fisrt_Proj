#!/bin/sh

import time
import re
import apiai
import json

class genesis:
    def start(self):
        answer = raw_input("You:")
        flag1 = self.apiai(answer.lower())
        if(flag1):
            self.start()
        else:
            flag = self.reply(answer.lower())
            if(flag):
                self.start()
            
            else:
                res=raw_input("I don't understand your input.\nShall I add it to my response list?\n")
                if(res.lower() == 'yes'):
                    resp = raw_input("How should I respond?\nPlease enter only the response\n")
                    finp = answer.lower() + ' =' + resp + '\n'
                    fi = open("C:\Users\deepak.sundaraiah\Desktop\data.txt", 'a')
                    fi.write(finp)
                    fi.close()
                    del fi
                    print("Response added. We can continue\n")
                    self.start()
                else:
                    print("We can continue\n")
                    self.start()
            
    def apiai(self, answer):        
        self.exit(answer)
        response = self.response(answer)
        result = response['result']
        pri = result['fulfillment']['speech']
        if (pri):
        #sent = answer + ' '
            print (pri)
            return True
        else: 
            return False           
            
            
    def reply(self, answer):
        fo = open("C:\Users\deepak.sundaraiah\Desktop\data.txt")
        self.exit(answer)
        for line in fo:
            matchObj = re.match( r'(.*)' + re.escape(answer) + r'(.*?) .*', line)
            if(matchObj):#print matchObj.string
            #if sent in line:
                ans1,ans2 = matchObj.string.split('=')
                print ans2
                del line, ans1, ans2#, sent
                fo.close()
                return True
        fo.close()
        del fo
    
    def response(self, answer):
        CLIENT_ACCESS_TOKEN = '21bf7b6e6f474b87be8d16178ee9fef5'
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        #self.assertTrue(False)
        text_requset = self.ai.text_request()
        text_requset.query = answer
        text_requset.resetContexts = False

        text_requset.entities = None

        response = text_requset.getresponse()
        return json.loads(response.read().decode())
    
    def exit(self, answer):
        if(answer.lower() == 'exit'):
            print("Goodbye. Take Care...\nSee you soon.")
            time.sleep(2)
            exit(1)
                                   
devstr = genesis()     
devstr.start()
