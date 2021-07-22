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
from urllib.parse import unquote
import json


strInput = ''
for word in sys.argv[1:]:
    strInput += word + ' '
a = unquote(strInput).replace("+", " ")
text = a

model_log = keras.models.load_model("model")

##############################################################
def convert_to_ascii(sentence):
 sentence_ascii=[]
 for i in sentence:                 
  if(ord(i)==8221): # ”  :  8221
   sentence_ascii.append(129)  # ü    
  elif (ord(i)==8220): # “  :  8220
   sentence_ascii.append(130) # é
  elif(ord(i)==8216): # ‘  :  8216
   sentence_ascii.append(131) # â
  elif(ord(i)==8211): # –  :  8211  
   sentence_ascii.append(132) # ä 
  elif(ord(i)==8217): # ’  :  8217
   sentence_ascii.append(133) # à
             
  elif(len(sentence)==1):
   sentence_ascii.append(134) # å

  else:
   sentence_ascii.append(ord(i)) 
  #else:
  # pass
   
 zer=np.zeros((10000))

 for i in range(len(sentence_ascii)):
  zer[i]=sentence_ascii[i]

 zer.shape=(100, 100)
 return zer
################################################
def clean_sqli_data(data):  
 d=data   
 d= " ".join(d.split( )) 
 if (d==''):
  d=' '   
 return d
###############################################
a= clean_sqli_data(a)
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

# return json
xjson = {
  "text": text,
  "result": pred
}
yjson = json.dumps(xjson)
print(yjson) 