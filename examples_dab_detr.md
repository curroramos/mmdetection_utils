# Data
```
COCODIR/
  ├── train2017/
  ├── val2017/
  └── annotations/
  	├── instances_train2017.json
  	└── instances_val2017.json
```

# Train
```
python main.py -m dab_detr \
  --output_dir logs/DABDETR/R50 \
  --batch_size 2 \
  --epochs 50 \
  --lr_drop 40 \
  --coco_path /home/curro/dataset_catec/robot_2020_v2/dab_detr \
  --pretrain_model_path /home/curro/Downloads/checkpoint_dab_detr.pth

python main.py -m dab_deformable_detr \
  --output_dir logs/dabdeformabledetr/R50_v2/ \
  --batch_size 1 \
  --epochs 50 \
  --lr_drop 40 \
  --coco_path /home/curro/dataset_catec/robot_2020_v2/dab_detr \
  --pretrain_model_path /home/curro/Downloads/checkpoint_dab_deformable_r50v2.pth
```

# Val
MODEL = {dab_detr, dab_deformable_detr}

```
python main.py -m ${MODEL} \
  --output_dir logs/dabdeformabledetr/R50_v2 \
  --coco_path /home/curro/dataset_catec/robot_2020_v2/dab_detr \
  --resume ${WEIGHTS} \
  --eval 
```