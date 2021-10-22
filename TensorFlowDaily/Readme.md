# README
## Tensorflow Daily

本目录用于日常所见TF代码的摘录

TensorFlow2 的 Eager 模式，去掉了 TF 定义的变量或张量需要借助 Session 来实现向 Python 变量的转换的过程，是对 Session 模式的去枷锁，不要从 Session 模式开始学习如何去掉 Session，直接`认为 TF 定义的变量或张量可以被直接调用`就好了，即在 TensorFlow2 中定义了变量或张量，像 Numpy 变量或数组一样直接调用就可以了。
