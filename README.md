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

## Re-implementation Details 
## Reproduction Steps 
To use this repo to reproduce the results, you must run the full Image2Style_Implementation.ipynb. To pass in the correct images, you must change the path for the input images in the framework. Images are imported many times throughout the 3 contributions, so it's important to look for all places we are importing. Additionally, any new images you want to run this framework on must be dropped in the data folder. Seperate contributions are seperated through markdown in the file. 

The GPU requirements for this code require T4 to run. Additionally, each contribution can take up to 40 minutes to 1 hour to run.   
## Results/Insights 
## Conclusion 
## References 
## Acknowledgements 


