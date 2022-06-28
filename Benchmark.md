
# Benchmark template table

# Test
| Model                     | bbox_mAP | bbox_mAP_50 | bbox_mAP_75 | bbox_mAP_s | bbox_mAP_m | bbox_mAP_l |
|---------------------------|----------|-------------|-------------|------------|------------|------------|
|mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x| 0.231 |0.474 |0.221| 0.000| 0.239| 0.265|
|mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x| 0.235| 0.516| 0.192| 0.000| 0.249| 0.282 |
|atss_r50_fpn_dyhead | 0.193 | 0.543 | 0.099 | 0.110 | 0.151 | 0.371 |
|retinanet_swin-t-p4-w7_fpn_1x| 0.228| 0.570 |0.139 |0.124 |0.238 |0.288|
|dab_detr|0.273|0.717|0.167|0.157|0.266|0.330
|dab_deformable_detr|0.304|0.795|0.170|0.318|0.293|0.337|

# Val
| Model                     | bbox_mAP | bbox_mAP_50 | bbox_mAP_75 | bbox_mAP_s | bbox_mAP_m | bbox_mAP_l |
|---------------------------|----------|-------------|-------------|------------|------------|------------|
|mask_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x| 0.179| 0.402| 0.138| 0.007| 0.143| 0.451|
|mask_rcnn_swin-t-p4-w7_fpn_ms-crop-3x|0.164| 0.388| 0.123| 0.009| 0.122| 0.428|
|atss_r50_fpn_dyhead_1x|0.193| 0.543| 0.099| 0.110| 0.151| 0.371|
|retinanet_swin-t-p4-w7_fpn_1x|0.214| 0.595| 0.098| 0.174| 0.200| 0.420|
|dab_detr|0.167|0.444|0.104|0.107|0.099|0.459|
|dab_deformable_detr|0.226|0.536| 0.152|0.167| 0.181|0.384|