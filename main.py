
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
import os
import cv2
import numpy as np
import time
IMAGE_WIDTH=1241
IMAGE_HEIGHT=376






rospy.init_node("listener", anonymous=True)
image_pubulish=rospy.Publisher('/camera/image_raw',Image,queue_size=1)
def publish_image(imgdata):
    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=IMAGE_HEIGHT
    image_temp.width=IMAGE_WIDTH
    image_temp.encoding='rgb8'
    image_temp.data=np.array(imgdata).tostring()
    #print(imgdata)
    #image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=1241*3
    image_pubulish.publish(image_temp)
file_list=os.listdir('/home/lucky/open/data/kitti/00/image_0')
file_list.sort()
for i in file_list:
    img=cv2.imread('/home/lucky/open/data/kitti/00/image_0/'+i)
    publish_image(img)
    #time.sleep(1)
    cv2.imshow('123',img)
    key=cv2.waitKey(1000)
    if key==ord('q'):
        break
    print("pubulish")