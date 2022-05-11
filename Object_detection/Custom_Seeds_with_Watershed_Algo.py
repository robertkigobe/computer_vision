#!/usr/bin/env python
# coding: utf-8

# # Custom Seeds with the WaterShed Algorithm
# 
# Previously we did a lot of work for OpenCV to set Markers to provide seeds to the Watershed Algorithm. But what if we just provide seeds ourselves? Let's try it out!

# ## Imports

# In[2]:


import cv2
import numpy as np


# In[3]:


import matplotlib.pyplot as plt
#%matplotlib inline


# ### Read in the Image and Make a Copy

# In[4]:


road = cv2.imread('/Users/robertkigobe/Documents/My_Research/My_Python/Computer_vision/images/road_image.jpg')
road_copy = np.copy(road)


# In[5]:


#plt.imshow(road)


# #### Create an empty space for the results to be drawn

# In[6]:


road.shape


# In[7]:


road.shape[:2]


# In[8]:


marker_image = np.zeros(road.shape[:2],dtype=np.int32)


# In[9]:


segments = np.zeros(road.shape,dtype=np.uint8)


# In[10]:


segments.shape


# ### Create colors for Markers
# 

# In[11]:


from matplotlib import cm


# Returns (R,G,B,Alpha) we only need RGB values

# In[12]:


cm.tab10(0)


# In[13]:


cm.tab10(1)


# In[14]:


np.array(cm.tab10(0))


# In[15]:


np.array(cm.tab10(0))[:3]


# In[16]:


np.array(cm.tab10(0))[:3]*255


# In[17]:


x = np.array(cm.tab10(0))[:3]*255


# In[18]:


x.astype(int)


# In[19]:


tuple(x.astype(int))


# Let's make a function for all those steps

# In[20]:


def create_rgb(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)


# In[21]:


colors = []


# In[22]:


# One color for each single digit
for i in range(10):
    colors.append(create_rgb(i))


# In[23]:


colors


# ### Setting Up Callback Function

# In[24]:


colors


# In[25]:


# Numbers 0-9
n_markers = 10


# In[26]:


# Default settings
current_marker = 1
marks_updated = False


# In[27]:


def mouse_callback(event, x, y, flags, param):
    global marks_updated 

    if event == cv2.EVENT_LBUTTONDOWN:
        
        # TRACKING FOR MARKERS
        cv2.circle(marker_image, (x, y), 10, (current_marker), -1)
        
        # DISPLAY ON USER IMAGE
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)
        marks_updated = True


# In[ ]:


cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    
    # SHow the 2 windows
    cv2.imshow('WaterShed Segments', segments)
    cv2.imshow('Road Image', road_copy)
        
        
    # Close everything if Esc is pressed
    k = cv2.waitKey(1)

    if k == 27:
        break
        
    # Clear all colors and start over if 'c' is pressed
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[0:2], dtype=np.int32)
        segments = np.zeros(road.shape,dtype=np.uint8)
        
    # If a number 0-9 is chosen index the color
    elif k > 0 and chr(k).isdigit():
        # chr converts to printable digit
        
        current_marker  = int(chr(k))
        
        # CODE TO CHECK INCASE USER IS CARELESS
#         n = int(chr(k))
#         if 1 <= n <= n_markers:
#             current_marker = n
    
    # If we clicked somewhere, call the watershed algorithm on our chosen markers
    if marks_updated:
        
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)
        
        segments = np.zeros(road.shape,dtype=np.uint8)
        
        for color_ind in range(n_markers):
            segments[marker_image_copy == (color_ind)] = colors[color_ind]
        
        marks_updated = False
        
cv2.destroyAllWindows()


# In[ ]:




