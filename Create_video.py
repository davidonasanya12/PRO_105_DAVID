import os 
import cv2

path = "C:/Users/thesl/Downloads/PRO-C105-Project-Images-main/PRO-C105-Project-Images-main/Images"

images=[]


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
print(len(images))
count = len(images)
frame=cv2.imread(images[0])
frame.shape("width","height","channels")
size = ("width","height")
print(size)
out=cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    cv2.imread(images[i])
    out.write()
    if (cv2.waitKey(25)==32):
        break 
cv2.destroyAllWindows()
