## study caffe

### 安装

* 具体见[Installation/Caffe.md](https://github.com/alisure-ml/Installation/blob/master/Caffe.md)

* `caffe`编译完成后，会生成一个`build`目录，在该目录下有个`tools`，这里有个可执行文件`caffe`


### 一般步骤

1. 数据格式处理

2. 编写网络结构文件 `.prototxt`
    在`Data`层中引用数据文件

3. 网络求解文件 `solver.prototxt`
    用`net`配置网络结构文件

4. 训练网络
    ```
    ./build/tools/caffe train --solver=solver.prototxt
    ```
    

### 生成`prototxt`

* pycaffe


### 可视化工具

* draw_net.py

* [netscope](http://ethereon.github.io/netscope/quickstart.html)


### 模型

* [soeaver/caffe-model](https://github.com/soeaver/caffe-model)


### Reference

* [[Caffe]:关于caffe新手入门](http://blog.csdn.net/cham_3/article/details/72141753)

* [深度学习（六）caffe入门学习](http://blog.csdn.net/hjimce/article/details/48933813)
