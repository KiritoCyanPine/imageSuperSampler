from PIL import Image
import time
import os
from cv2 import dnn_superres

# initialize super resolution object
sr = dnn_superres.DnnSuperResImpl_create()

# read the model
path = 'EDSR_x4.pb'
sr.readModel(path)

# set the model and scale
sr.setModel('edsr', 2)

# sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
print("initialized")

def ConvertImage(imagename) -> bool:
    try:
        # im = Image.open(imagename)
        
        # im = im.resize((im.size[0]*2,im.size[1]*2), resample=Image.BILINEAR)

        # rgb_im = im.convert('RGB')
        # # newName = imagename[:-4] + '.jpg'
        # newName = "colors" + '.jpg'

        # rgb_im.save(newName)

        image = cv2.imread(imagename)
        image = image.convert('RGB')
        image = sr.upsample(image)
        cv2.imwrite('zupscaled_test.png', image)

        return True
    except Exception:
        print("unable to convert image")
        return False

def RemoveImage(imagename):
    os.remove(imagename)


def getAllPNG():
    pngImages = []
    dirItems = os.listdir()
    for file in dirItems:
        if file[len(file)-4:] == ".png":
            pngImages.append(file)
    return pngImages
    
def convertIncomimgFilesToJpg():
    images = getAllPNG()
    for image in images:
        isConverted = ConvertImage(image)
        if not isConverted:
            print(image + "was not conerted to jpg")
        

def WatchExecute():
    while 1:
        convertIncomimgFilesToJpg()
        time.sleep(15)
        
    


print(ConvertImage("HS2_2023-01-18-11-31-27-070.png"))