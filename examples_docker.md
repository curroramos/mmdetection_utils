# Build container
```
docker build -t mmdetection:latest .
```
# Run docker container using volume in folder "shared" 
```
t=mmdetection  && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/shared/:/usr/src/shared $t \ 
```
# First configuration: move data in volume to a new data folder and also the configs into the configs folder 
```
mkdir data && cp -r ../usr/src/shared/dataset/coco_data/ data/  && cp -r ../usr/src/shared/configs/ .
```
# Train a model
```
python tools/train.py {CONFIG} --gpu-id 0 --cfg-options runner.max_epochs={EPOCHS}   data.samples_per_gpu={BATCH_SIZE}  work_dir='{WORK_DIR}' load_from='{WEIGHTS_LINK}'
```
# Resume train and change epochs and workdir
```
python3 {CONFIG} --gpu-id 0 --cfg-options runner.max_epochs={EPOCHS}   data.samples_per_gpu={BATCH_SIZE}  work_dir='{WORK_DIR}' --resume-from {WEIGHTS} 
```
# Evaluate a model
```
python3 tools/test.py {CONFIG} {WEIGHTS} --eval bbox 
```
# Show inferences
```
python3 tools/test.py {CONFIG} {WEIGHTS} --eval show
```
# Robot2020v3 examples
```
python tools/train.py configs/dyhead/atss_r50_fpn_dyhead_1x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50   data.samples_per_gpu=2  work_dir='../usr/src/shared/checkpoints/robot_2020v3/atss_r50_fpn_dyhead_1x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/dyhead/atss_r50_fpn_dyhead_4x4_1x_coco/atss_r50_fpn_dyhead_4x4_1x_coco_20211219_023314-eaa620c6.pth'

python3 tools/train.py configs/swin/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50 data.samples_per_gpu=2 work_dir='../usr/src/shared/checkpoints/robot_2020v3/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/swin/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco/mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco_20210906_131725-bacf6f7b.pth'

python3 tools/train.py configs/swin/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_CATEC.py --gpu-id 0 --cfg-options runner.max_epochs=50   data.samples_per_gpu=2 work_dir='../usr/src/shared/checkpoints/robot_2020v3/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_CATEC' load_from='https://download.openmmlab.com/mmdetection/v2.0/swin/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco/mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco_20210903_104808-b92c91f1.pth'
```
