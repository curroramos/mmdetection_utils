_base_ = './mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_CATEC.py'


pretrained = 'https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_small_patch4_window7_224.pth'  # noqa



# you need to set mode='dynamic' if you are using pytorch<=1.5.0
fp16 = dict(loss_scale=dict(init_scale=512))


model = dict(
    backbone=dict(
        depths=[2, 2, 18, 2],
        init_cfg=dict(type='Pretrained', checkpoint=pretrained)))




#### Modify dataset related settings
dataset_type = 'COCODataset'
classes = ("airplane",)


data = dict(
    train=dict(
        img_prefix='data/coco_data/coco_train/', #'balloon/train/',
        classes=classes,
        ann_file= 'data/coco_data/train.json'), #'balloon/train/annotation_coco.json'),
    val=dict(
        img_prefix='data/coco_data/coco_val/', #'balloon/val/',
        classes=classes,
        ann_file= 'data/coco_data/validation.json'), #'balloon/val/annotation_coco.json'),
    test=dict(
        img_prefix='data/coco_data/coco_val/', #'balloon/val/',
        classes=classes,
        ann_file= 'data/coco_data/validation.json'))# val/annotation_coco.json')


####

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg=dict(
        custom_keys={
            'absolute_pos_embed': dict(decay_mult=0.),
            'relative_position_bias_table': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))
lr_config = dict(warmup_iters=1000, step=[27, 33])
runner = dict(max_epochs=36)
