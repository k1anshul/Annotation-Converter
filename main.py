#Import Library

import os
import shutil
import argparse
import yaml
from tqdm import tqdm
from pylabel import importer

from pyfiglet import Figlet
from termcolor import colored
print(Figlet(font='big',width=200).renderText('Annotation Converter'))

#Importing config file data
parser = argparse.ArgumentParser()
parser.add_argument('--hyp', type=str, default=r"config/hyp.yaml",help="config file path")
opt = parser.parse_args()
hyp = yaml.load(open(opt.hyp), Loader=yaml.FullLoader)

image_path = hyp['image_path']
annot_path = hyp['annot_path']
output_path = hyp['output_path']
class_names=hyp['class_names']
image_ext=hyp['image_ext']
cvt_list=hyp['converter'].split('2')

#Display Important Inputs
print(colored(f'* Conversion Type: {cvt_list[0]} TO {cvt_list[1]}', color='yellow'))
print(colored(f'* Image Path: {image_path}', color='yellow'))
print(colored(f'* Annotation Path: {annot_path}', color='yellow'))
print(colored(f'* Output Path: {output_path}', color='yellow'))
print(colored(f'* Class Names: {str(class_names)}\n', color='yellow'))

os.makedirs(output_path, exist_ok=True)

if cvt_list[0]=='YOLO':
	dataset = importer.ImportYoloV5(path=annot_path, path_to_images=image_path, cat_names=class_names,img_ext=image_ext)
elif cvt_list[0]=='COCO':
	dataset = importer.ImportCoco(path=annot_path, path_to_images=image_path)
elif cvt_list[0]=='VOC':
	dataset = importer.ImportVOC(path=annot_path, path_to_images=image_path)
else:
	print('Please select proper converter')

if cvt_list[1]=='YOLO':
	dataset.export.ExportToYoloV5(output_path=output_path,yaml_file=os.path.join(output_path,'dataset.yaml'),cat_id_index=0)[0]
elif cvt_list[1]=='COCO':
	json_path=os.path.join(output_path,'dataset_annot.json')
	with open(json_path, "w") as f:
		f.close()
	dataset.export.ExportToCoco(output_path=json_path,cat_id_index=1)
elif cvt_list[1]=='VOC':
	dataset.export.ExportToVoc(output_path=output_path, segmented_=True, path_=True, database_=True, folder_=True, occluded_=True)[0]

count=0
for img in tqdm(os.listdir(image_path)):
	if img.endswith(tuple(image_ext.split(','))):
		count+=1
		shutil.copy2(os.path.join(image_path,img),os.path.join(output_path,img))

print(colored(f'\n* Successfully Converted {count} Image Annotations', color='yellow'))