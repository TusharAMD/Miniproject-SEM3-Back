import cv2
import numpy as np
import random

def get_filtered_image(image1,image2):
    img1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
    img1=cv2.resize(img1, (1000, 1000)) 
    img2=cv2.resize(img2, (1000, 1000)) 
    
    width = img1.shape[0] 
    height = img1.shape[1] 
      
    # img1 and img2 are two blank images 
      
    for i in range(img2.shape[0]): 
        for j in range(img2.shape[1]): 
            for l in range(3): 
                  
                # v1 and v2 are 8-bit pixel values 
                # of img1 and img2 respectively 
                v1 = format(img1[i][j][l], '08b') 
                v2 = format(img2[i][j][l], '08b') 
                  
                # Taking 4 MSBs of each image 
                v3 = v1[:4] + v2[:4]  
                  
                img1[i][j][l]= int(v3, 2) 


    filtered=img1

    return filtered