from glob import glob
import os
import pandas as pd
import argparse

CATEGORIES_15 = ('background', 'small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
               'crane', 'bridge', 'oil tank', 'dam', 'athletic field', 'helipad', 'roundabout')
CATEGORIES_16 = ('background', 'small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
                  'crane', 'bridge', 'oil tank', 'dam', 'indoor playground', 'outdoor playground', 'helipad', 'roundabout')
CATEGORIES_20 = ('background', 'small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
                  'crane', 'bridge', 'oil tank', 'dam', 'indoor playground', 'outdoor playground', 'helipad', 'roundabout',
                  'helicopter', 'individual container', 'grouped container', 'swimming pool')
category_map = {
        15 : CATEGORIES_15,
        16 : CATEGORIES_16,
        20 : CATEGORIESS_20}

def main(srcpath, dstpath, classes=16):
    categories = category_map[classes]
    
    text_files = glob(os.path.join(srcpath, '*.txt'))
    header_names = ['file_name', 'confidence',
                    'point1_x', 'point1_y',
                    'point2_x', 'point2_y', 
                    'point3_x', 'point3_y', 
                    'point4_x', 'point4_y']

    dfs = []
    for txt in text_files:
        df = pd.read_csv(txt, delim_whitespace=True,
                    names=header_names)
        df['class_id'] = categories.index(txt.split('/')[-1][:-4])
        df['file_name'] = df['file_name'] + '.png'
        
        dfs.append(df)

    full_df = pd.concat(dfs)
    full_df = full_df[['file_name', 'class_id', 'confidence',
                        'point1_x', 'point1_y',
                        'point2_x', 'point2_y', 
                        'point3_x', 'point3_y', 
                        'point4_x', 'point4_y']]

    full_df.to_csv(dstpath, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='merge dota class results to csv file')
    parser.add_argument('--srcpath', )
    parser.add_argument('--classes', default=16)
    parser.add_argument('--dstpath', default='result.csv')

    args = parser.parse_args()

    main(args.srcpath, args.dstpath, args.classes)
