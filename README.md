
# ROAS Baseline
Object Detection Baseline for Rotated Objects in Arirang Satellite Image

## Introduction
This is baseline to detect rotated objects in Arirang(KOMPSAT) satellite image.
This codebase is on [AerialDetection](https://github.com/dingjiansw101/AerialDetection).

For simplicity, we will call our data as ROAS, which stands for *R*otated *O*bject Dataset in *A*rirang *S*atellite Image.


![detected_results](results.jpg)
   

## Installation

  Please refer to [INSTALL.md](INSTALL.md) for installation.
    
## Get Started

Please see [GETTING_STARTED.md](GETTING_STARTED.md) for the basic usage.

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Citing

If you use [ROAS](https://niasatellitedata.imweb.me/ai_object) dataset, codebase or models in your research, please consider cite .

```
@inproceedings{xia2018dota,
  title={DOTA: A large-scale dataset for object detection in aerial images},
  author={Xia, Gui-Song and Bai, Xiang and Ding, Jian and Zhu, Zhen and Belongie, Serge and Luo, Jiebo and Datcu, Mihai and Pelillo, Marcello and Zhang, Liangpei},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3974--3983},
  year={2018}
}

@article{chen2019mmdetection,
  title={MMDetection: Open mmlab detection toolbox and benchmark},
  author={Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and Liu, Ziwei and Xu, Jiarui and others},
  journal={arXiv preprint arXiv:1906.07155},
  year={2019}
}

@InProceedings{Ding_2019_CVPR,
author = {Ding, Jian and Xue, Nan and Long, Yang and Xia, Gui-Song and Lu, Qikai},
title = {Learning RoI Transformer for Oriented Object Detection in Aerial Images},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {June},
year = {2019}
}

```

## Thanks to the Third Party Libs

[Pytorch](https://pytorch.org/)

[mmdetection](https://github.com/open-mmlab/mmdetection)

[AerialDetection](https://github.com/dingjiansw101/AerialDetection)
