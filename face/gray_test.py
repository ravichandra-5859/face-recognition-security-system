from PIL import Image
import numpy as np
#load the image and convert it to graycode
image=Image.open("ravi.jpg").convert("L")
#image to numnpy
image_array=np.array(image)
#set numpy print options
np.set_printoptions(threshold=np.inf)
#print all pixels
print("\n pixel values: ")
print(image_array)
image.save("gray_image.jpg")
image.show()
