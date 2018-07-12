import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

options = {
    'model' : 'cfg/yolov2-tiny-voc-8c.cfg',
    'load' : 21750,
    'threshold': 0.2,
    'gpu' : 0.8
}

tf = TFNet(options)
img_dir = 'check_img/'
img_name = 'strawberry0'
img_type = '.jpg'
img = cv2.imread(img_dir+img_name+img_type,cv2.IMREAD_COLOR)



result = tf.return_predict(img)

res_len = len(result)

for i in range(res_len):
	tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
	br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
	label = result[i]['label']

	img = cv2.rectangle(img, tl, br, (0, 255, 0), 4)
	img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

cv2.imwrite(img_dir+img_name+'_detected'+img_type,img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)


plt.show()