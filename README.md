# EEG.DeepLearning-xi (Gitee Repo as Main Add.)

- 整理用Matlab、Octave、Python-MNE处理EEG信号数据的相关技术流程

## MNE-Python

MNE-Python出现于2014年，是Python在神经科学方面的三方库，用Python处理大量EEG数据时，代码式的操作方式会大大提高“数据流”处理效率。  
后面在学习深度学习框架的同时要兼顾该三方库的学习。  
`sudo pip install mne`即可安装该库，项目首页在：`https://mne.tools/stable/index.html`.  

另查到该三方库存在正在开发的GUI项目MNELAB，基于MNE-Python和Pyside2图形库，构建了初步可用的MNE界面。项目地址在：  
`https://github.com/cbrnr/mnelab`.  
该GUI项目暂时不作为重点学习的内容，因为GUI操作不利于与深度学习框架的融合和后期项目的扩展能力。  

这意味着MNE-Python这个EEG处理库与“深度学习”结合的紧密程度将会更高。  

## VScode中新建Jupyter-notebook文件
1. 安装VScode编辑器，官方方案太慢，推荐下载最新安装包自己手动安装（windows下推荐软件内升级）。  
2. 安装Python扩展。  
3. 创建新的Notebook笔记本，`Ctrl + Shift + p`打开命令栏，输入`jupyter`，选择`creat new blank jupyter notebook`创建笔记本。

## Octave Related(不考虑)
Octave是Matlab社区化的产物，官方介绍能兼容Matlab99%的代码，除了不具有Matlab优良的GUI界面以及商业化的三方库，基本的代码是完全可以跑通的，数据分析、处理、可视化方面完全可以替代Matlab。

未来也许会出现Octave的GUI项目，以及三方库的繁荣，届时该产品的商业和开源社区将会出现相辅相成、互相促进的局面。
