import numpy as np
from numpy.core.records import array
from numpy.lib.function_base import append
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import keras
from keras.models import Sequential
import sys


a = ''
for word in sys.argv[1:]:
    a += word + ' '
text = a

model_log = keras.models.load_model("vendor/quynhthu/detect-attacker/model-version-one")
def convert_to_ascii(sentence):
   sentence_ascii=[]
   for i in sentence:
        if(ord(i)==8217): # �  :  8217
          sentence_ascii.append(133)
        if(ord(i)==8221): # �  :  8221
          sentence_ascii.append(129)      
        if(ord(i)==8220): # �  :  8220
          sentence_ascii.append(130)
        if(ord(i)==8216): # �  :  8216
          sentence_ascii.append(131) 
        if(ord(i)==8211): # �  :  8211
          sentence_ascii.append(132)  
          
        if(len(sentence)==1 and ord(i)>128):
          sentence_ascii.append(134)
             
        if (ord(i)<=128):
          sentence_ascii.append(ord(i))
        else:
          pass
   zer=np.zeros((10000))
   
   for i in range(len(sentence_ascii)):
      zer[i]=sentence_ascii[i]
   zer.shape=(100, 100)
   
   return zer
def clean_sqli_data(data):  
    d=''
    for i in data:
        
        i=i.replace('\n', '')
        i=i.replace('%20', ' ')
        d+=i
    return d

image=convert_to_ascii(a)
x=np.asarray(image,dtype='float')
image =  cv2.resize(x, dsize=(100,100), interpolation=cv2.INTER_CUBIC)
image/=128
a=image
a= a.reshape(1,100,100,1)
p = model_log.predict(a)
pred=np.argmax(p)


if pred==0:
   pred="Normal"
elif pred==1: 
   pred="XSS"
elif pred==2: 
   pred="SQL"

print('{"text":"'+text+'", "result":"'+pred+'"}')