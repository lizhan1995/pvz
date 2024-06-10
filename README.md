# 植物大战僵尸

## 功能描述

使用【python】实现植物大战僵尸的自娱自乐版本。


截至2024-06-10，代码行数在550行左右


作者新手入门时的学习视频：
https://www.bilibili.com/video/BV1be411x7u9/?spm_id_from=333.999.0.0&vd_source=209569c05267fb94b8fedbb608f3272c




## 设计思路

### 自娱自乐

采用【python】的【pygame】库，搞了一个半成品，目的当然是让自己能快速理解python开发游戏的思路，大量采用了百度+kimi的问答方式进行思路扩展。 
![image](https://github.com/lizhan1995/pvz/assets/28769051/6c67461f-e197-44b6-abec-4632783ca0eb)

自定义的类体现封装、继承、多态的`OOP`思想，现在只做了三个部分：

1. 植物基类Plant，只实现了向日葵`SunFlower`、豌豆射手`Peashooter`、坚果`WallNut`。
2. 僵尸基类Zombie，只实现了普通僵尸`Zombie`。
3. 其他基类Other，只实现了区域`Zone`、阳光`sun`、卡槽`card_slot`。



## 操作运行

操作方式跟原版游戏一致：

* 种植，拖动植物到地块
* 攻击，僵尸大吃特吃、豌豆射个不停
* 随机事件，随机产生僵尸、随机产生阳光


### 效果图

![image](https://github.com/lizhan1995/pvz/assets/28769051/c2d04da1-17f8-49a2-8ba1-49bfcbc60283)


## 问题和解决方案

1. 有关pygame库的中文资料稀缺且泛泛而谈，如何学习？

   百度是你学习的第一位老师，ai是你学会如何找资料的第二位老师！

   
   
2. 该项目存在的意义？

   自娱自乐！
