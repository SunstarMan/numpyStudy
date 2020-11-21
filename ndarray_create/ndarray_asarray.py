import numpy

if __name__ == '__main__':
    # 4、numpy.asarray从已有的数组创建数组
    # numpy.asarray类似numpy.array，但numpy.asarray参数只有三个，比numpy.array少两个。
    # numpy.asarray(a, dtype=None, order=None)

    # 1)将列表转换为ndarray:
    x1 = [1, 2, 3]
    print(x1)
    asarr = numpy.asarray(x1)
    print(asarr)
    # 2)将元组转换为 ndarray:
    x2 = (1, 2, 3)
    print(x2)
    asarr2 = numpy.asarray(x2)
    print(asarr2)
    # 3)将元组列表转换为ndarray:
    x3 = [(1, 2, 3), (4, 5)]
    print(x3)
    asarr3 = numpy.asarray(x3)
    print(asarr3)
    # 4)设置dtype参数：
    asarr4 = numpy.asarray(x1, dtype=float)
    print(asarr4)

    # 5、numpy.frombuffer用于实现动态数组。
    # numpy.frombuffer接受buffer输入参数，以流的形式读入转化成ndarray对象。
    # numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
    # buffer是字符串的时候，Python3默认str是Unicode类型，所以要转成bytestring在原str前加上b。
    # buffer可以是任意对象，会以流的形式读入。
    # count读取的数据数量，默认为 - 1，读取所有数据。
    # offset读取的起始位置，默认为0。
    s = b'hello,world!'
    arr = numpy.frombuffer(s, dtype='S1', count=2, offset=0)
    print(arr)

    # 6、numpy.fromiter方法从可迭代对象中建立ndarray对象，返回一维数组
    # numpy.fromiter(iterable, dtype, count=-1)
    # iterable可迭代对象
    # 使用 range 函数创建列表对象
    li = range(5)
    it = iter(li)
    # 使用迭代器创建 ndarray
    arr2 = numpy.fromiter(it, dtype=numpy.float, count=-1)
    print(arr2)
