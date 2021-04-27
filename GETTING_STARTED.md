# Getting Started

This page provides basic tutorials about the usage of mmdetection.
For installation instructions, please see [INSTALL.md](INSTALL.md).



## Prepare ROAS dataset.
It is recommended to symlink the dataset root to `roas/data`.

Here, we give an example for single scale data preparation of ROAS dataset.

First, make sure your initial data are in the following structure.
```
data/roas
├── train
│   ├── images
│   └── json
└── test 
    ├── images
    └── json
```
Split the original images and create COCO format json. 

```
python ROAS_devkit/prepare_roas.py --srcpath path_to_dota --dstpath path_to_split_data
```
Then you will get data in the following structure
```
roas16-split
├── test1024_2x
│   ├── coco.json
│   └── images
└── train768_2x
     ├── coco.json
     └── images
```

## Inference with pretrained models



### Test a dataset

- [x] single GPU testing
- [x] multiple GPU testing

You can use the following commands to test a dataset.

```shell
# single-gpu testing
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [--out ${RESULT_FILE}]

# multi-gpu testing
./tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} [--out ${RESULT_FILE}]
```

Optional arguments:
- `RESULT_FILE`: Filename of the output results in pickle format. If not specified, the results will not be saved to a file.

Examples:

Assume that you have already downloaded the checkpoints to `work_dirs/`.

1. Test Faster R-CNN with RoI Transformer. [Pretrained Weight: RoI Transformer with Resnet101](https://drive.google.com/file/d/1q99Lg9hw2AvLuS0NUXzWisQKEMjPR7DI/view?usp=sharing)

```shell
python tools/test.py configs/ROAS/faster_rcnn_RoITrans_r101_fpn_2x_roas16.py \
    work_dirs/faster_rcnn_RoITrans_r101_fpn_2x_roas16/epoch_12.pth
```

2. Test Faster R-CNN with RoI Ttransformer with 4 GPUs.

```shell
./tools/dist_test.sh configs/ROAS/faster_rcnn_RoITrans_r101_fpn_2x_roas16.py \
    work_dirs/faster_rcnn_RoITrans_r101_fpn_2x_roas16/epoch_12.pth  \
    4 
```

3. Parse the results.pkl to the format which is used in [DOTA evaluation](http://117.78.28.204:8001/)

For methods with only OBB Head, set the type OBB.
```
python tools/parse_results.py --config configs/ROAS/faster_rcnn_RoITrans_r101_fpn_2x_roas16.py --type OBB
```

4. Merge results as csv
```
python3 ROAS_devkit/merge_results_as_csv.py --srcpath ${PARSING PATH}$ --dstpath ${DST_PATH}
```

5. Evaluate performance
```
python3 ROAS_devkit/evaluate_roas.py --gt_csv_path ${GT_PATH}$ --pred_csv_path ${PRED_PATH}
```
You have to prepare csv file for ground-truth by **./ROAS_devkit/geojson2csv.py**.

### Demo of inference in a large size image.


```python
python demo_large_image.py
```


## Train a model

mmdetection implements distributed training and non-distributed training,
which uses `MMDistributedDataParallel` and `MMDataParallel` respectively.

All outputs (log files and checkpoints) will be saved to the working directory,
which is specified by `work_dir` in the config file.

**\*Important\***: The default learning rate in config files is for 8 GPUs.
If you use less or more than 8 GPUs, you need to set the learning rate proportional
to the GPU num, e.g., 0.01 for 4 GPUs and 0.04 for 16 GPUs.

### Train with a single GPU

```shell
python tools/train.py ${CONFIG_FILE}
```

If you want to specify the working directory in the command, you can add an argument `--work_dir ${YOUR_WORK_DIR}`.

### Train with multiple GPUs

```shell
./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} [optional arguments]
```

Optional arguments are:

- `--validate` (recommended): Perform evaluation at every k (default=1) epochs during the training.
- `--work_dir ${WORK_DIR}`: Override the working directory specified in the config file.
- `--resume_from ${CHECKPOINT_FILE}`: Resume from a previous checkpoint file.

### Train with multiple machines

If you run mmdetection on a cluster managed with [slurm](https://slurm.schedmd.com/), you can just use the script `slurm_train.sh`.

```shell
./tools/slurm_train.sh ${PARTITION} ${JOB_NAME} ${CONFIG_FILE} ${WORK_DIR} [${GPUS}]
```

Here is an example of using 16 GPUs to train Mask R-CNN on the dev partition.

```shell
./tools/slurm_train.sh dev mask_r50_1x configs/mask_rcnn_r50_fpn_1x.py /nfs/xxxx/mask_rcnn_r50_fpn_1x 16
```

You can check [slurm_train.sh](tools/slurm_train.sh) for full arguments and environment variables.

If you have just multiple machines connected with ethernet, you can refer to
pytorch [launch utility](https://pytorch.org/docs/stable/distributed_deprecated.html#launch-utility).
Usually it is slow if you do not have high speed networking like infiniband.



For more information on how it works, you can refer to [TECHNICAL_DETAILS.md](TECHNICAL_DETAILS.md) (TODO).
