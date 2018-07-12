import os
import cv2
from lxml import etree
import xml.etree.ElementTree as ET


def get_xml(folder, img, labels, top_left_list, bottom_right_list, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = img.name
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for label, top_left, bottom_right in zip(labels, top_left_list, bottom_right_list):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = label
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(top_left[0])
        ET.SubElement(bbox, 'ymin').text = str(top_left[1])
        ET.SubElement(bbox, 'xmax').text = str(bottom_right[0])
        ET.SubElement(bbox, 'ymax').text = str(bottom_right[1])


    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    save_path = os.path.join(savedir, img.name.replace('jpg', 'xml'))
    print (save_path)
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)