import numpy

if __name__ == '__main__':
    # object：数组或嵌套的数列
    # dtype：数组元素的数据类型，可选
    # copy：对象是否需要复制，可选
    # order：创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
    # subok：默认返回一个与基类类型一致的数组
    # ndmin：指定生成数组的最小维度
    example_array = numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)

    # *******实例*************
    # 维度为1
    a = numpy.array([1, 2, 3])
    # print(a)

    # 维度为2
    b = numpy.array([[1, 2], [3, 4]])
    # print(b)

    # 限定最小维度为3
    c = numpy.array([1, 2, 3, 4], ndmin=3)
    # print(c)

    # 限定数据类型
    d = numpy.array([1, 2, 3, 4], dtype=complex)
    d1 = numpy.array([1, 2, 3, 4], dtype=float)
    print(d)
    print(d1)
