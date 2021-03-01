# visual-saliency-detection
 Fast and easy detection based on spectral residual approach

Saliency detection based on spectral residual/residual spectrum theory is actually a smooth curve subtracted from logarithmic spectrum in the frequency domain.
According to the similarity between the author's theory and the stage of human visual preprocessing, the distribution of logarithmic spectrum of a large number of natural images is found to be relatively consistent. Now, the distribution is given through some algorithm or prior information, and then the singularity obtained by subtracting the distribution from the log spectrum is the significant point.
The algorithm is simple, fast and effective, and can be used for data screening after adjustment.

based on [Saliency detection: A spectral residual approach](https://www.researchgate.net/profile/Liqing_Zhang3/publication/221364530_Saliency_Detection_A_Spectral_Residual_Approach/links/55b497f208ae092e9653c2bc.pdf)</br>

My result :  
![0](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/visual-saliency-detection/s1.jpg?token=AJZQ6R26P2WO6YM2BLZNK3K6Y64VW)![1](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/visual-saliency-detection/s1_2.png?token=AJZQ6R5T6THA3E7HJ4EG4ZC6Y64XG)</br>
![2](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/visual-saliency-detection/s2.png?token=AJZQ6R2EHZWIB2XAWI36VKS6Y64YW)![3](https://raw.githubusercontent.com/MirusUmbra/Display-data/master/visual-saliency-detection/s2_2.png?token=AJZQ6R7OH6NC7DDSNLPJOQS6Y64ZS)</br>

It is important to note that the size of the data will affect the results. Generally speaking, a small graph will get a larger area of the overall target in the graph, while a large graph will get the details of the target.

Size of image will influence the result
