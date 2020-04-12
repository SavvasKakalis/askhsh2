import sys
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image


img = np.array(Image.open(sys.argv[1])) #diavazw thn eikona

a1 = float(sys.argv[3]) #pairnw ta orismata apth grammh entolwn
a2 = float(sys.argv[4]) 
a3 = float(sys.argv[5]) 
a4 = float(sys.argv[6]) 
a5 = float(sys.argv[7]) 
a6 = float(sys.argv[8]) 

rows = img.shape[0]
columns = img.shape[1]

new_img = np.zeros((rows,columns))
for i in range(0,rows):
    for j in range(0,columns):
        #methodologia gia ton metasxhmatismo eikonas kata shmeio 
        #1.metafora tou shmeiou (i,j) kata (-rows/2,-columns/2)
        x= 1*i + 0*j - (rows/2)*1
        y= 0*i + 1*j - (columns/2)*1
        #2.epithymhtos metasxhmatismos
        x= a1*x + a2*y + a3*1  
        y= a4*x + a5*y + a6*1 
        #3.metafora tou (xnew,ynew) kata (rows/2,columns/2)
        x= 1*x + 0*y + (rows/2)*1 
        y= 0*x + 1*y + (columns/2)*1
        #krithrio paremvolhs gia x y 
        x=round(x) 
        y=round(y) 
        #ama einai eksw apta oria mou de mpainei sthn eikona
        if(x>=0 and x<rows and y>=0 and y<columns):
            new_img[i][j]=img[x][y]
#emfanish eikonas

plt.imshow(new_img,"gray")                
plt.show()
Image.fromarray(new_img.astype(np.uint8)).save(sys.argv[2])

