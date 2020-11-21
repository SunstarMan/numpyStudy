# NumPy 从数值范围创建数组
import numpy

if __name__ == '__main__':
    # 1、numpy.arange;numpy包中的使用arange函数创建数值范围并返回ndarray对象，函数格式如下：
    # numpy.arange(start, stop, step, dtype)
    # start起始值，默认为0
    # stop终止值（不包含）
    # step步长，默认为1

    # 生成0到5的数组:
    x = numpy.arange(0, 6, 2, float)
    print(x)

    # 2、numpy.linspace函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    # num要生成的等步长的样本数量，默认为50
    # endpoint该值为true时，数列中包含stop值，反之不包含，默认是True。
    # retstep如果为True时，生成的数组中会显示间距，反之不显示
    y = numpy.linspace(0, 6, 12, False, True, float)
    print(y)
    z = numpy.linspace(0, 6, 6).reshape([2, 3])
    print(z)

    # 3、numpy.logspace 函数用于创建一个于等比数列。格式如下：
    # np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    # base对数log的底数。
    a = numpy.logspace(0, 64, 10, True, 2, float)
    print(a)
