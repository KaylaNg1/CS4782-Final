#  CS4782-Final -- Implementing Image2StyleGAN++: How to Edit the Embedded Images?
## Introduction 
The goal of this project is to reimplement the main contributions of the paper Image2StyleGAN++: How to Edit the Embedded Images.   
This paper focuses on improving upon the existing Image2StyleGAN framework—an image editing framework. The improved version, Image2StyleGAN++, introduces three main contributions:  
1. Optimize noise separately from optimizing the latent space.  
2. Use the global latent space (W⁺) to make local edits with masks on images.  
3. Combine W⁺ embedding with activation tensors.

We implement these three contributions along with applications highlighted in the paper. 

## Chosen Result 
Each of three contributions in the paper had different results which we aimed to recreate. 

Contribution 1:   
In contribution 1, the paper prosed optimizing the moise seperatly from the latent space. With this, they aimed to get a higher PSNR value than the original Image2StyleGan framework. They were able to achieve a result of 45 db for the psnr. 

Contribution 2: 


## GitHub Contents 
Data -- These are the images that are passed as input to the model 
Results -- These are the different results developed by our framework 
Poster -- This is a poster describing our presentation of the paper for our CS4782 clss 
Report -- This is a report describing our implementation details 
Code -- This is where our main executable is. 

In our main executable, we have all three of the reimplmented contributions. There is markdown text seperating when each new contribution starts. The code must be run together as later contributions depend on functions implemented in previous contributions. 


## Re-implementation Details 
## Reproduction Steps 
To use this repo to reproduce the results, you must run the full Image2Style_Implementation.ipynb. To pass in the correct images, you must change the path for the input images in the framework. Images are imported many times throughout the 3 contributions, so it's important to look for all places we are importing. Additionally, any new images you want to run this framework on must be dropped in the data folder. Seperate contributions are seperated through markdown in the file. 

The GPU requirements for this code require T4 to run. Additionally, each contribution can take up to 40 minutes to 1 hour to run.   
## Results/Insights 
We were able to reimplment all three main contributions described in the paper. However, our results are not exactly like the paper. We attribute these differences to a couple different factors: 
1. There were no implmentation details for how the paper implemented style loss
2. The quality of our images were lower
3. The paper was vague in terms of tuning some parameters 

## Conclusion 
Overall, we believe we had a sucessful reimplmentation of Image2StyleGAN++.

## References 

13.12. Neural Style Transfer — Dive into Deep Learning 0.15.0 documentation. (n.d.). D2l.ai. https://d2l.ai/chapter_computer-vision/neural-style.html.  
Abdal, R., Qin, Y., & Wonka, P. (2020). Image2StyleGAN++: How to Edit the Embedded Images? CVPR, 8296-8305.   
https://openaccess.thecvf.com/content_CVPR_2020/papers/Abdal_Image2StyleGAN_How_to_Edit_the_Embedded_Images_CVPR_2020_paper.pdf.   
Abdal, R., Qin, Y., & Wonka, P. (2020). Image2StyleGAN++: How to Edit the Embedded Images? -Supplementary Material-. CVPR.
https://openaccess.thecvf.com/content_CVPR_2020/supplemental/Abdal_Image2StyleGAN_How_to_CVPR_2020_supplemental.pdf   
Bhat, Z. (2021). Image2StyleGAN [Pretrained Model]. https://github.com/zaidbhat1234/Image2StyleGAN.    
Mohd, A. (2021, February 8). Neural style transfer using PyTorch. DEV Community.  https://dev.to/aquibpy/neural-style-transfer-using-pytorch-3d5l.   

## Acknowledgements 
We would like to acknowledge the original authors of the Image2StyleGAN++ paper (Rameen Abdal, Yipeng Qin, and Peter Wonka). Additionally, we completed this reimplementation as part of a class at Cornell University, CS 4782(Deep Learning). We would like to acknowledge the professors and course staff who provided guidance and asistance. 


