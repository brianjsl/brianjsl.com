title: BallpitNDF: Few Shot Pouring with Local Neural Descriptor Fields
slug: projects/ballpitndf
lang: en
summary: BallpitNDF project summary.
status: hidden
template: projects 
save_as: projects/ballpitndf.html

<div style="text-align: center;">
<img src="../images/ballpitndf.png" style="width: 30%;"/>
</div>

Can a robot learn to pour from a basket without ever seeing how to grab one? In this project, we learn to pour things from a wide variety of containers (eg. cups, bottles, bowls) in a few-shot manner. This is my final project for MIT's course on robotic manipulation (6.4210) taught by Tomas Lozano-Perez. While systems have been built before
to pour from containers, almost all of them require a large amount of data to train on. In this project, we show that a robot can learn to pour from a basket with only a few examples on objects of *different classes*, using a few-shot imitation learning paradigm trained only on the surrogate task of object reconstruction. The idea is to use <a href="https://arxiv.org/abs/2302.03573"> Local Neural Descriptor Fields </a> as a form of *shape* level descriptors, which can then be used to learn grasps of the handle with an energy optimization scheme. This is combined with a perception module that uses the Grounded DINO and SAM modules along with outlier removal to generate a fully end-to-end robotic
pouring system. 

Please see the <a href="https://github.com/brianjsl/BallPitNDF">code</a> for more details. 

