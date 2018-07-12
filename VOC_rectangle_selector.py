import os
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from VOC_generate_xml import get_xml


img = None
top_left_corList = [] #矩形坐上坐标List
bottom_right_corList = [] #矩形右下坐标List
label_list = [] #同一个图片多个标记框的标签List


image_folder = 'images' #图片目录
savedir = 'annotations' #XML存储地址
label = 'watermelon' #标签


def onSelect_func(click, release):
    global top_left_corList, bottom_right_corList, label_list    
    top_left_corList.append((int(click.xdata), int(click.ydata)))
    bottom_right_corList.append((int(release.xdata), int(release.ydata)))
    label_list.append(label)


def onkeypress(event):
    global label_list, top_left_corList, bottom_right_corList, img
    if event.key == 'q':
        print(label_list)
        get_xml(image_folder, img, label_list, top_left_corList, bottom_right_corList, savedir)
        top_left_corList = []
        bottom_right_corList = []
        label_list = []
        img = None


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1, figsize=(10.5, 8))
        image = cv2.imread(os.getcwd() + '\\' + image_file.path)
        print (os.getcwd() + '\\' + image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)
        
        toggle_selector.RS = RectangleSelector(
            ax, onSelect_func,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True,
        )
        plt.connect('key_press_event', toggle_selector)
        plt.connect('key_press_event', onkeypress)
        plt.tight_layout()
        plt.show()
        plt.close(fig)