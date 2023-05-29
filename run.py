import os
import sys


# train vanilla model:
# To train a nasty teacher, a vanilla trained model (called as "adversarial") is required.
cmd1 = "python train_scratch.py --save_path='experiments/CIFAR10/baseline/mobilenetv2/'"
os.system(cmd1)


# train nasty teacher:
cmd1 = "python train_nasty.py --save_path='experiments/CIFAR10/kd_nasty_resnet18/'"
os.system(cmd1)


# KD for skeptical student:
cmd1 = "python train_skeptical.py --save_path='experiments/skeptical_mobilenetv2_nasty_resnet18/cifar100/'"
os.system(cmd1)


# train averager student:
cmd1 = "python train_averager_stu.py --save_path='experiments/CIFAR100/averager_nasty_RN50_RN50/' --seed=101"
os.system(cmd1)


# train averager student in a manner of training scheme of skeptical student / evaluation of ensembling:
cmd1 = "python train_averager_stu_ens.py --save_path='experiments/CIFAR100/averager_normal_RN50_RN50/' --seed=100"
os.system(cmd1)


