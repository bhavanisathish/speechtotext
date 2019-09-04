# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 01:34:43 2019

@author: bhavanisathish
"""

import speech_recognition as sr  
while True:
# get audio from the microphone                                                                       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")  
        try:                                                                              
            audio = r.listen(source)
            text = r.recognize_google(audio)
            if(text=="stop"):
                print("stoppped")
                break
            else:
                    print(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
