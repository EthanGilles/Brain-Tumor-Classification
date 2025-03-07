# Brain Tumor Classification using MRI Images

![Dataset Example](https://raw.githubusercontent.com/EthanGilles/Brain-Tumor-Classification/05a1843939f030e4ff7b6da9a0037f5d0245de77/images/dataset_example1.png)

![Dataset Example](https://raw.githubusercontent.com/EthanGilles/Brain-Tumor-Classification/05a1843939f030e4ff7b6da9a0037f5d0245de77/images/dataset_example2.png)

## Notebooks

[AlexNet-KNN Hybrid](https://github.com/EthanGilles/Brain-Tumor-Classification/blob/main/AlexNet-KNN.ipynb)

[Xception with no pretrained weights](https://github.com/EthanGilles/Brain-Tumor-Classification/blob/main/Xception-Not-Pretrained.ipynb)

[Xception-KNN Hybrid](https://github.com/EthanGilles/Brain-Tumor-Classification/blob/main/Xception-KNN.ipynb)

## Description

This repository contains the code and resources for a machine learning research 
project conducted at the University of Southern Maine (USM). The goal is to 
classify brain tumors in MRI images into one of four 
classes: **gliomas**, **meningiomas**, **pituitary tumors**, and **no tumor**. 

## Dataset Overview
The dataset consists of MRI scans categorized into the following classes:

| Class Name       | Description                                                                                     | Prevalence in Dataset* |
|------------------|-------------------------------------------------------------------------------------------------|------------------------|
| **Gliomas**      | Tumors originating from glial cells, often aggressive and common in the brain.                 | ~30%                   |
| **Meningiomas**  | Typically benign tumors arising from the meninges (membranes surrounding the brain/spinal cord).| ~25%                   |
| **Pituitary**    | Tumors in the pituitary gland, usually benign but may disrupt hormonal balance.                | ~25%                   |
| **No Tumor**     | Healthy MRI scans with no signs of tumors.                                                     | ~20%                   |

### Motivation
- Prior work ([Paper 1](#)) demonstrated the potential of AlexNet-KNN for brain tumor classification, but its robustness under varied conditions remains understudied.
- Transfer learning with Xception ([Paper 2](#)) achieved high accuracy but at the cost of computational complexity. This project aims to leverage the Xception model.
- Correct classification of tumors in MRI scans is crucial for accurate diagnosis and treatment planning.


## References

[Refined Automatic Brain Tumor Classification Using Hybrid Convolutional Neural Networks for MRI Scans](https://www.mdpi.com/2075-4418/13/5/864) - AlexNet-KNN Hybrid for Brain Tumor Classification.

[Advanced Brain Tumor Classification in MR Images Using Transfer Learning and Pre-Trained Deep CNN Models](https://www.mdpi.com/2072-6694/17/1/121#B23-cancers-17-00121) - Transfer Learning with Xception for MRI-Based Diagnosis.


## Previous Results

In previous papers we have the following results, along with mine:
| Model            | Accuracy | Precision | Recall | F1-Score | 
|------------------|----------|-----------|--------|----------|
| AlexNet-KNN (Paper 1)     | 96%    | 96%      | 100%   | 97%     |
| Xception (Paper 2) | 95.2%   | 95%      | 94%   | 95%     |
| Xception-KNN Hybrid (My approach) | 98.4%   | 98%      | 98%   | 98%     |


## Acknowledgments

- This work is supported by the University of Southern Maine (USM) as part of a 
research initiative in medical imaging classification.

- [Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/)
