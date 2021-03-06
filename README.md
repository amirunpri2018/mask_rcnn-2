# mask-rcnn


This is a Pytorch 1.0 implementation of [Mask R-CNN](https://arxiv.org/abs/1703.06870) that is based on Matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN)\[1\] and [this](https://github.com/multimodallearning/pytorch-mask-rcnn)\[2\]. Matterport's repository is an implementation on Keras and TensorFlow.

The main improvements from \[2\] are:
- Pytorch 1.0
- most numpy computations were ported to pytorch (for GPU speed)
- supports batchsize > 1
- some bugs were fixed in the translation process
- code refactor
- NMS speed-up

Currently, it works with Kaggle's 2018 Data Science Bowl dataset (the result on 1st phase testset is 0.27).

to train the network use:
python samples/nuclei.py train --dataset=path_to_dataset --model=coco

to detect use:
python samples/nuclei.py submit --dataset=path_to_dataset --model=path_to_trained_model

to check Kaggle's 2018 Databowl metric on a dataset use:
python samples/nuclei.py metric --dataset=path_to_dataset --model=path_to_trained_model

for installation instructions, just export mrcnn directory to PYTHONPATH and run:
python setup.py install
