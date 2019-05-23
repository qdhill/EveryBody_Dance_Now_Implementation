
<h1 align="center">
  <br>
  
  <br>
  Damini K Rijhwani
  <br>
</h1>

<h4 align="center"> Implementation of <a href="https://arxiv.org/pdf/1808.07371.pdf">Everybody Dance Now  by Chan, et al</a>.</h4>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"
         alt="Gitter">
  </a>
  <a href="https://github.com/daminiR/">
  <img src="https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg"></a>
  <a href="https://GitHub.com/Naereen/StrapDown.js/graphs/contributors/">
      <img src="https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg">
  </a>
  <a href="https://pypi.python.org/pypi/ansicolortags/">
    <img src="https://img.shields.io/pypi/l/ansicolortags.svg">
  </a>
</p>

<p align="center">
  <a href="#intro">Intro</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#related">Related</a> •
    <a href="#Requirements">Requirements</a> •
</p>

<div id=”mainDiv”, align="center">

![](loop-correct.gif)

## Intro 

This is an implementation of a research paper, Everybody Dance Now. The main objective of the project is to allow frames of poses to be synthesized. This in turn can be used for showcasing dance moves or any movement.
The paper utilizes pix2pixHD generative adversarial model to synthesize an image from semantic pose heat maps. The poses are obtain from openPose framework. Heat maps and part affinity maps are used to perform pose estimation.
The pix2pixHD GAN introduces, several separate inputs to the generator and the deliminator, while having multiple decriminators that advance the photo realistic depiction of the synthesized image.Further details about the 
pix2pixHD GAN can read on NVIDIA's <a href="https://github.com/NVIDIA/pix2pixHD">github</a>  or in my <a href="https://thedisruptculture.com/2019/04/20/high-resolution-image-synthesis-and-semantic-manipulation-with-conditional-gans-explained/">blog</a>.   

## Key Features

Create gifs or videos of synthesized dance moves<br/>
Make people you know dance!<br/>
Simple use of GANs and CNNs<br/>

## How To Use
Clone or download the repo<br/>
Obtain target dataset - the person you want to perform the generated poses on.<br/>
Obtain the test dataset to source the pose estimation from<br/>
Train the GAN model on the target dataset<br/>
Transfer the models learnt outcome to output synthesise images, using generator and the semantic label heat map of the poses.<br/>
Create video from moving frames.<br/>
## Download 
Clone the github repo including source. 


---
> LinkedIn [Damini K Rijhwani](https://www.linkedin.com/in/drijhwan)<br/>
> GitHub [@DaminiR](https://github.com/daminiR/) <br/>
> AI Blog  [Disrupt Culture](https://thedisruptculture.com/) <br/>




