
import os
import json
from glob import glob

test_list = []
with open('test_list.txt') as f:
    test_list = f.readlines()
test_list = [i.strip().split('.')[0] for i in test_list]


json_files = []
for label_file in os.listdir('label'):
    if label_file.split('.')[0] not in test_list:
        continue
    json_files.append(label_file)


with open('labels.csv', 'w') as f:
    f.write('file_name,class_id,confidence,point1_x,point1_y,point2_x,point2_y,point3_x,point3_y,point4_x,point4_y\n')
    for json_file in json_files:
        file_name = json_file.split('.')[0]
        with open(os.path.join('label',json_file)) as json_f:
            features = json.load(json_f)['features']
        for feat in features:
            class_id = feat['properties']['type_id']
            if int(class_id) not in list(range(17)):
                continue
            points = feat['properties']['object_imcoords']
            f.write(f'{file_name},{class_id},1,{points}\n')

