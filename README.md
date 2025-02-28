# Brain Tumor Classification using MRI Images

![https://github.com/EthanGilles/Brain-Tumor-Classification/blob/dff8f14819e323666c1ccedc0b7a95a0ce02fee5/images/dataset_example1.png](Dataset Example)
![https://github.com/EthanGilles/Brain-Tumor-Classification/blob/dff8f14819e323666c1ccedc0b7a95a0ce02fee5/images/dataset_example2.png](Dataset Example)

## Description


This repository contains the code and resources for a machine learning research 
project conducted at the University of Southern Maine (USM). The goal is to 
classify brain tumors in MRI images into one of four 
classes: **gliomas**, **meningiomas**, **pituitary tumors**, and **no tumor**. 
The project focuses on evaluating the robustness of the AlexNet-KNN hybrid 
model proposed in prior work and developing a lightweight yet accurate 
alternative to heavyweight architectures like Xception.

## Key Features
- **Multi-class Classification**: Predicts tumor type from MRI images across four classes.
- **Model Efficiency**: Prioritizes lightweight architectures to ensure deployability in resource-constrained environments.
- **Reproducibility**: Detailed code and documentation to replicate experiments.
- **Comparative Analysis**: Benchmarks performance against the Xception-based transfer learning approach.

## Dataset Overview
The dataset consists of MRI scans categorized into the following classes:

| Class Name       | Description                                                                                     | Prevalence in Dataset* |
|------------------|-------------------------------------------------------------------------------------------------|------------------------|
| **Gliomas**      | Tumors originating from glial cells, often aggressive and common in the brain.                 | ~30%                   |
| **Meningiomas**  | Typically benign tumors arising from the meninges (membranes surrounding the brain/spinal cord).| ~25%                   |
| **Pituitary**    | Tumors in the pituitary gland, usually benign but may disrupt hormonal balance.                | ~25%                   |
| **No Tumor**     | Healthy MRI scans with no signs of tumors.                                                     | ~20%                   |

*Note: Prevalence statistics are approximate and dataset-dependent.*

## Methodology
### Model Architectures
1. **AlexNet-KNN Hybrid**: A hybrid approach combining AlexNet for feature extraction and K-Nearest Neighbors (KNN) for classification. This model is tested for robustness and computational efficiency.
2. **Xception, but not pretrained**: To test the transfer learning capabilities of Xception, there will be an Xception architecture but with random weights.
3. **Lightweight Custom Architectures**: Experiments with streamlined convolutional neural networks (CNNs) to balance accuracy and model size.

### Motivation
- Prior work ([Paper 1](#)) demonstrated the potential of AlexNet-KNN for brain tumor classification, but its robustness under varied conditions remains understudied.
- Transfer learning with Xception ([Paper 2](#)) achieved high accuracy but at the cost of computational complexity. This project aims to bridge the gap between performance and efficiency.
- Correct classification of tumors in MRI scans is crucial for accurate diagnosis and treatment planning.


## References
[Refined Automatic Brain Tumor Classification Using Hybrid Convolutional Neural Networks for MRI Scans](https://www.mdpi.com/2075-4418/13/5/864) - AlexNet-KNN Hybrid for Brain Tumor Classification.

[Advanced Brain Tumor Classification in MR Images Using Transfer Learning and Pre-Trained Deep CNN Models](https://www.mdpi.com/2072-6694/17/1/121#B23-cancers-17-00121) - Transfer Learning with Xception for MRI-Based Diagnosis.


## Previous Results

In previous papers we have the following results:
| Model            | Accuracy | Precision | Recall | F1-Score | 
|------------------|----------|-----------|--------|----------|
| AlexNet-KNN (Paper 1)     | 96%    | 96%      | 100%   | 97%     |
| Xception (Paper 2) | 95.2%   | 95%      | 94%   | 95%     |

These are great results however testing the robustness and efficientcy of these models is necessary.

## Results

I am currently working on conducting experiments for the results.

## Acknowledgments

- This work is supported by the University of Southern Maine (USM) as part of a 
research initiative in medical imaging classification.

- [Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/)
