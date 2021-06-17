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
import json


a = ''
for word in sys.argv[1:]:
    a += word + ' '
text = a

model_log = keras.models.load_model("vendor/quynhthu/detect-attacker/sqldata1")
def convert_to_ascii(sentence):
   sentence_ascii=[]
   for i in sentence:
      if(ord(i)<8222):# ” has ASCII of 8221
         if(ord(i)==8217): # ’  :  8217
            sentence_ascii.append(134)
         if(ord(i)==8221): # ”  :  8221
            sentence_ascii.append(129)
         if(ord(i)==8220): # “  :  8220
            sentence_ascii.append(130)
         if(ord(i)==8216): # ‘  :  8216
            sentence_ascii.append(131)
         if(ord(i)==8217): # ’  :  8217
            sentence_ascii.append(132)
         if(ord(i)==8211): # –  :  8211
            sentence_ascii.append(133)
         if(ord(i)==246): 
            sentence_ascii.append(135)    
         if(ord(i)==252): 
            sentence_ascii.append(136)  
         if(ord(i)==223): 
            sentence_ascii.append(137)
         if(ord(i)==252): 
            sentence_ascii.append(138)    
         if(ord(i)==228): 
            sentence_ascii.append(139)
         if(ord(i)==163): 
            sentence_ascii.append(140)
         if(ord(i)==226): 
            sentence_ascii.append(141)
         if(ord(i)==152): 
            sentence_ascii.append(142)
         if(ord(i)==195): 
            sentence_ascii.append(143)
         if(ord(i)==189): 
            sentence_ascii.append(145)
         if(ord(i)==253): 
            sentence_ascii.append(146)
         if(ord(i)==224): 
            sentence_ascii.append(147)                
         if (ord(i)<=128):
            sentence_ascii.append(ord(i))
         else:
            pass
   zer=np.zeros((10000))
   for i in range(len(sentence_ascii)):
      zer[i]=sentence_ascii[i]
   zer.shape=(100, 100)
   return zer
# clean data

def clean_sqli_data(data):    
   for i in data:
      i=i.replace('\n', '')
      i=i.replace('%20', ' ')
      i=i.replace('=', ' = ')
      i=i.replace('((', ' (( ')
      i=i.replace('))', ' )) ')
      i=i.replace('(', ' ( ')
      i=i.replace(')', ' ) ')  
   return data

result = []
#a=np.zeros(len(sys.argv))
#arr=np.zeros((len(sys.argv),100,100))
#a='<script>alert(document.cookie)</script>'
#for i in range(len(sys.argv)):
#   a= clean_sqli_data(a)
image=convert_to_ascii(a)
x=np.asarray(image,dtype='float')
image =  cv2.resize(x, dsize=(100,100), interpolation=cv2.INTER_CUBIC)
image/=128
a=image
a= a.reshape(1,100,100,1)
p = model_log.predict(a)#Nếu kết quả dự đoán lớn hơn 0.5 thì suy ra nó là tấn công
if p>0.5:
   p="SQL"
else: 
   p="Normal"

print('{"test":"'+text+'", "result":"'+p+'"}')
#   pred=np.argmax(p)cj ở
#   result.append(pred) 
#   result.append(p)  
"""
arr=np.zeros(len(array))
for i in range(len(array)):
   a= clean_sqli_data(array[i])
   image=convert_to_ascii(a)
   x=np.asarray(image,dtype='float')
   image =  cv2.resize(x, dsize=(100,100), interpolation=cv2.INTER_CUBIC)
   image/=128
   arr[i]=image
arr=arr.reshape(shape[0],100,100,1)
p=model_log.predict(arr)
pred=[]
for i in range(len(p))
   pred[i]=np.argmax(p[i])
print(pred)
"""


