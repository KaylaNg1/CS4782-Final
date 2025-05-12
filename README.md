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

Contribution 1: In contribution 1, the paper proposed optimizing the noise seperatly from the latent space. By injecting and optimizing the noise, the recostruction is able to recover finer grained details (skin texture, facial hair, etc ), achieving a higher PSNR value than the original Image2StyleGan framework. They were able to achieve a result of 45 db for the psnr post noise optimization. 

Contribution 2: In contribution 2, they leveraged global latent space (W⁺) to make local edits with masks on image. We specifically chose to re-create two applications of this contribution: local edits via scribbles and style transfer.

Contribution 3: In contribution 3, the authors of the paper combined W+ embedding with activation tensors manipulation in order to perform both high quality local edits and global semantic edits.  

## GitHub Contents 
Data -- These are the images that are passed as input to the model   
Results -- These are the different results developed by our framework    
Poster -- This is a poster describing our presentation of the paper for our CS4782 class   
Report -- This is a report describing our implementation details    
Code -- This is where our main executable is.    

In our main executable, we have all three of the reimplmented contributions. There is markdown text seperating when each new contribution starts. The code must be run together as later contributions depend on functions implemented in previous contributions. 

## Re-implementation Details 

We based our implementation upon an existing pre-trained implementation of Image2StyleGAN. The original code for it can be found here: https://github.com/zaidbhat1234/Image2StyleGAN. We then extended it with the three contributions of described in the paper.

There were some hyper-parameters and function implementations unspecified in the paper (e.g style loss function, masking function, etc ). Therefore, we implemented our own custom versions that we attribute to our slightly differing results.

For the first contribution, adding noise map optimization, the evaluation metrics would be achieving as PSNR score of ~44/45 post noise optimization. The other contributions would be evaluated qualitatively as the paper does not specify any quantitative metrics.
- The methodology for contribution 1: applying w+ latent optimization ( already provided by Image2StyleGAN ) THEN applying noise map optimization which initialized each noise layer with a random tensor of noise, then a training loop was implemented which would generate the noise injected image and calculate the loss ( MSE + Perceptual ).

For the second contribution, we choose to reimplement 2 applications highlighted in the paper: Local Edits with Scribble and Style Transfer. 
- The methodology for local edits with scribble was as follows: extracting mask, applying mask to image, optimizing W+ with mask and noise optimization. This algorithm was highlighted in algorithm 5 of the paper. It produced comparable results. 
- The methodology for style transfer was as follows: extracting mask, applying mask to image, optimizing W+ with mask, optimizing W+ with style loss, and noise optimization. This algorithm was highlighted in algorithm 6 of the paper. It produced comparable results to the paper. We believe any differences present here were attributed to image quality, and lack of information on the specifics of thier style loss function.  

## Reproduction Steps 
To use this repo to reproduce the results, you must run the full Image2Style_Implementation.ipynb. All of the dependencies, libraries, and command-line arguments are already embedded into the cells. To pass in the correct images, you must change the path for the input images in the framework. Images are imported many times throughout the 3 contributions, so it's important to look for all places we are importing. Additionally, any new images you want to run this framework on must be dropped in the data folder. Seperate contributions are seperated through markdown in the file. 

The GPU requirements for this code require T4 to run. Additionally, each contribution can take up to 40 minutes to 1 hour to run.   

Moreover, please refer to the Image2StyleGAN repository README.md for information on how to access their pre-trained weights. Once received, you should create a folder called weight_files that should be located in your project directory.

## Results/Insights 
We were able to reimpelment all three main contributions similar to what was described in the paper. That is, we achieved a higher PSNR score post noise map optimization that was around ~36. Moreover, for contributions 2 and 3, we were able to visually see realistic embeddings and edits after training. However, our results are not exactly like the paper. We attribute these differences to a couple different factors: 
1. There were no implmentation details for how the paper implemented style loss and other functions
2. The quality of our images were lower
3. The paper was vague in terms of tuning some parameters 

## Conclusion 
Overall, we believe we had a sucessful reimplmentation of Image2StyleGAN++. Although we were not able to make perfect replicas of the result, we were able to sucessfully demonstrate the improvements this paper proposed. Our barriers were input image quality, and a vague description of specific implementations in the paper. Through this project, we learned the importance of time-management and communication which were critical to make this assignment a success!

## References 
13.12. Neural Style Transfer — Dive into Deep Learning 0.15.0 documentation. (n.d.). D2l.ai. https://d2l.ai/chapter_computer-vision/neural-style.html.  
Abdal, R., Qin, Y., & Wonka, P. (2020). Image2StyleGAN++: How to Edit the Embedded Images? CVPR, 8296-8305.   
https://openaccess.thecvf.com/content_CVPR_2020/papers/Abdal_Image2StyleGAN_How_to_Edit_the_Embedded_Images_CVPR_2020_paper.pdf.   
Abdal, R., Qin, Y., & Wonka, P. (2020). Image2StyleGAN++: How to Edit the Embedded Images? -Supplementary Material-. CVPR.
https://openaccess.thecvf.com/content_CVPR_2020/supplemental/Abdal_Image2StyleGAN_How_to_CVPR_2020_supplemental.pdf   
Bhat, Z. (2021). Image2StyleGAN [Pretrained Model]. https://github.com/zaidbhat1234/Image2StyleGAN.    
Mohd, A. (2021, February 8). Neural style transfer using PyTorch. DEV Community.  https://dev.to/aquibpy/neural-style-transfer-using-pytorch-3d5l.   

## Acknowledgements 
We would like to acknowledge the original authors of the Image2StyleGAN++ paper (Rameen Abdal, Yipeng Qin, and Peter Wonka). Additionally, we completed this reimplementation as part of a class at Cornell University, CS 4782 (Deep Learning). We would like to acknowledge the professors and course staff who provided guidance and asistance. 


