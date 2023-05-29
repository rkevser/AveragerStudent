

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This is the official repo of the Tiny Papers @ ICLR 2023 paper **Averager Student: Distillation from Undistillable Teacher**.

### Authors
Reyhan Kevser Keser (keserr@itu.edu.tr) and Behçet Uğur Töreyin (toreyin@itu.edu.tr)

### Abstract
Today, some companies release their black-box model as a service for users, where users can see the model’s output corresponding to their input. However, these models can be stolen via knowledge distillation by malicious users. Recently, undistillable teacher (Ma et al., 2021) is introduced in order to prevent the knowledge leakage. In this study, with the aim of contributing to solutions for model intellectual property (IP) protection, we propose a novel method which improves the distillation from an undistillable teacher whose goal is make the distillation difficult for students, with the purpose of model protection.




### Usage

1. Fetch the pretrained teacher models:
    ```
      https://github.com/ksouvik52/Skeptical2021 
    ```


OR train a nasty teacher model by: 
```
    python train_nasty.py --save_path='experiments/CIFAR10/kd_nasty_resnet18/'
```

2. Train an averager student: 
    ```
      python train_averager_stu.py --save_path='experiments/CIFAR100/averager_nasty_RN50_RN50/' --seed=101
    ```



### Cite this work
If you find this project useful to you, please cite our work:

      @article{keseraverager,
        title={Averager Student: Distillation from Undistillable Teacher},
        author={Keser, Reyhan Kevser and Toreyin, Behcet Ugur}
      }



### Acknowledgments
[Skeptical student repo](https://github.com/ksouvik52/Skeptical2021)

