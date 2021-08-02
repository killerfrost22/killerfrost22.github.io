from PIL import Image
import sys

# squre picture first   
def fill_image(image):
    width, height = image.size
    # Length and height first 
    new_image_length = width if width > height else height
    # Generate a white image background
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    #Given back the old image put the layer on teh new image 
    if width > height:#Vertical dimension first 
        new_image.paste(image, (0, int((new_image_length - height) / 2)))#(x,y) which representing each axis
    else:
        new_image.paste(image, (int((new_image_length - width) / 2),0))
    return new_image

#Cutting the picture into 9 equal pieces
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,3): # range could be 0-? which always be a squre 
        for j in range(0,3):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    
    image_list = [image.crop(box) for box in box_list]

    return image_list

#Save picture
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./result/python'+str(index) + '.png', 'PNG')
        index += 1
#Main function  
if __name__ == '__main__':
    file_path = "test.jpg"
    image = Image.open(file_path)
    image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)

    
