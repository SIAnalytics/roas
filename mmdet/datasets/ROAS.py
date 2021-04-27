from .coco import CocoDataset
import numpy as np

class ROAS(CocoDataset):

    CLASSES= ('small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
            'crane', 'bridge', 'oil tank', 'dam', 'athletic field', 'helipad', 'roundabout')

class ROAS_16(CocoDataset):

    CLASSES= ('small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
            'crane', 'bridge', 'oil tank', 'dam', 'indoor playground', 'outdoor playground', 'helipad', 'roundabout')
    
class ROAS_20(CocoDataset):

    CLASSES= ('small ship', 'large ship', 'civilian aircraft', 'military aircraft', 'small car', 'bus', 'truck', 'train',
            'crane', 'bridge', 'oil tank', 'dam', 'indoor playground', 'outdoor playground', 'helipad', 'roundabout',
            'helicopter', 'individual container', 'grouped container', 'swimming pool')
