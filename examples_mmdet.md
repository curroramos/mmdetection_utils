# Mmdetection 

## 1. Docker
### 1.1 Build container
```
docker build -t mmdetection:latest .
```
### 1.2 Run docker container using volume in folder "shared" 
```
t=mmdetection  && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/shared/:/usr/src/shared $t \ 
```
### 1.3 First configuration: move data in volume to a new data folder and also the configs into the configs folder 
```
mkdir data && cp -r ../usr/src/shared/dataset/coco_data/ data/  && cp -r ../usr/src/shared/configs/ .
```

## 2. Train a model
```
python tools/train.py ${CONFIG} --gpu-id 0 --cfg-options runner.max_epochs=${EPOCHS}   data.samples_per_gpu=${BATCH_SIZE}  work_dir=${WORK_DIR} load_from=${WEIGHTS_LINK}
```
## 2.1 Resume train and change epochs and workdir
```
python3 tools/train.py ${CONFIG} --gpu-id 0 --cfg-options runner.max_epochs=${EPOCHS}   data.samples_per_gpu=${BATCH_SIZE}  work_dir='${WORK_DIR}' --resume-from ${WEIGHTS} 
```
## 3. Evaluate (test) a model
```
python3 tools/test.py ${CONFIG} ${WEIGHTS} --eval bbox 
```
## 3.1 Show inferences
```
python3 tools/test.py ${CONFIG} ${WEIGHTS} --eval show
```

## 4 FPS benchmark
python3 tools/analysis_tools/benchmark.py ${CONFIG} ${WEIGHTS}  NONONONONONONO
## 5. Some examples
```
python tools/train.py configs/dyhead/atss_r50_fpn_dyhead_1x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50   data.samples_per_gpu=2  work_dir='../usr/src/shared/checkpoints/robot_2020v3/atss_r50_fpn_dyhead_1x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/dyhead/atss_r50_fpn_dyhead_4x4_1x_coco/atss_r50_fpn_dyhead_4x4_1x_coco_20211219_023314-eaa620c6.pth'

python3 tools/train.py configs/swin/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50 data.samples_per_gpu=2 work_dir='../usr/src/shared/checkpoints/robot_2020v3/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/swin/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco_20210906_131725-bacf6f7b.pth' ;\
python3 tools/train.py configs/swin/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50   data.samples_per_gpu=2 work_dir='../usr/src/shared/checkpoints/robot_2020v3/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/swin/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco_20210903_104808-b92c91f1.pth'
```


# PERSONALIZE MODELS
Each config file starts from 4 different base modules:
- dataset
- default_runtime
- model
- schedule

You can modify different things in each base modules:
- dataset
    - data settings, data location, batch_size (samples per gpu) ...
- default_runtime
    - checkpoint
- model
    - model architecture, num_classes
- schedule
    - optimizer, learning rate, epochs

These configs options can be modified in config.py file or in the argument line 
adding:
```
--cfg-options key='value'
```

## Example: building new config file
0. Load the "parent" model using `_base_` option, e.g.
```
_base_ = [
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py',
    '../_base_/default_runtime.py'
]
```
1. Change model base head  `num_classes=n_classes`. First copy the model head into
 the new config file, then change this parameter. This will overwrite the base model.

2. Change dataset location, overwritting train, val and test directories.

3. Change number of epochs, batch size, workdir, checkpoint ... However, this is
 recommended to be done using `--cfg-options` line command argument.
