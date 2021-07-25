#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PIL
PIL.__version__


# In[ ]:


help(PIL)


# In[ ]:


dir(PIL)


# In[ ]:


from PIL import Image
help(Image)


# In[2]:


from PIL import Image
file='C:/Users/Niktab/Pictures/Picture1.jpg'
image=Image.open(file)
print(image)


# In[9]:


import inspect
print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))


# In[10]:


image.show()


# In[11]:


from IPython.display import display
display(image)


# # Common functions in Python Library

# In[12]:


from PIL import Image
from IPython.display import display
file='C:/Users/Niktab/Pictures/Picture1.jpg'
image=Image.open(file)
display(image)


# In[13]:


help(image.copy)


# In[14]:


help(image.save)


# In[23]:


file='C:/Users/Niktab/Pictures/dog.png'
image.save(file)
image=Image.open(file)
import inspect
inspect.getmro(type(image))


# In[ ]:


from PIL import ImageFilter
help(ImageFilter)


# In[29]:


import PIL
from PIL import ImageFilter
image=image.convert('RGB') # this stands for red, green blue mode
blurred_image=image.filter(PIL.ImageFilter.BLUR)
display(blurred_image)
print('{}*{}'.format(image.width,image.height))


# In[35]:


display(image.crop((10,0,190,500)))


# In[38]:



from PIL import ImageDraw
drawing_object=ImageDraw.Draw(image)
drawing_object.rectangle((50,40,190,150), fill ='blue', outline ='blue')
display(image)


# # Additional PILLOW functions

# In[39]:


import PIL
from PIL import Image
from IPython.display import display
file='C:/Users/Niktab/Pictures/dog.png'
image=Image.open(file).convert('RGB')
display(image)


# In[40]:


from PIL import ImageEnhance
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0,10):
    images.append(enhancer.enhance(i/10))
    
print(images)   
                  


# In[ ]:


help(PIL.Image.new)


# In[44]:


from PIL import ImageEnhance
from PIL import Image
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0,10):
    images.append(enhancer.enhance(i/10))
    
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode,(first_image.width,10*first_image.height))

current_location = 0
for img in images:
    contact_sheet.paste(img, (0,current_location))
    current_location=current_location+1125
contact_sheet = contact_sheet.resize((160,900) )

display(contact_sheet)   


# In[45]:


from PIL import ImageEnhance
from PIL import Image
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0,10):
    images.append(enhancer.enhance(i/10))
    
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
current_location = 0
# for img in images:
#     contact_sheet.paste(img, (0,current_location))
#     current_location=current_location+1125
# contact_sheet = contact_sheet.resize((160,900) )

# display(contact_sheet)   

x=0
y=0
for img in images[1:]:
    contact_sheet.paste(img, (x, y) )
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

display(contact_sheet)


# In[ ]:




