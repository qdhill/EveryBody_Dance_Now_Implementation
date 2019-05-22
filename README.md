
<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.png" alt="Markdownify" width="200"></a>
  <br>
  Damini K Rijhwani
  <br>
</h1>

<h4 align="center"> Implementation of <a href="https://arxiv.org/pdf/1808.07371.pdf">Everybody Dance Now  by Chan, et al</a>.</h4>

<p align="center">
  <a href="https://www.python.org/">
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

![](new_gif_blog.gif)

<\div>
## Intro 

This is an implementation of a research paper, Everybody Dance Now. The main objective of the project is to allow frames of poses to be synthesized which in turn can be used for showcasing dance moves or any movement.
The paper utilizes pix2pixHD generative adversarial model to synthesize an image from a semantic pose heat maps. The poses are obtain from openPose framework. Heat maps and part affinity maps are used perform pose estimation.
The pix2pixHD GAN introduces, several separate inputs to the generator and the deliminator, while having multiple decriminators that advance the photo realistic depiction of the synthesized image.Further details about the 
pix2pixHD GAN can read on NVIDIA's documentation. The details of the GAN is also explain in my blog.   

## Key Features

* Create gifs or videos of synthesized dance moves
* Make people you know dance!
* Simple use of GANs and CNNs

## How To Use

- Clone or download the repo
- obtain target dataset - the person you want to perform the generated poses on.
- Obtain the test dataset to source the pose estimation from
- Train the GAN model on the target dataset 
- Transfer the models learnt outcome to output synthesise images, using generator and the semantic label heat map of the poses.
- Create video from moving frames.
## Download 
Clone the github repo including source. 


---
> GitHub [@amitmerchant1990](https://github.com/daminiR/) &nbsp;&middot;&nbsp;
> LinkedIn [Damini K Rijhwani](www.linkedin.com/in/drijhwan)






- [Introduction](#introduction)
- [Features](#features)
- [Build Process](#build-process)
- [License](#License)




