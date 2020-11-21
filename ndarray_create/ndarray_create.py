import numpy

if __name__ == '__main__':
    # 1、numpy.empty方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组(数组元素为随机值，因为它们未初始化)
    # numpy.empty(shape, dtype = float, order = 'C')
    # order:有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
    arr1 = numpy.empty((2, 3), float, 'C')
    print(arr1)

    # 2、numpy.zeros创建指定大小的数组，数组元素以0来填充：
    # numpy.zeros(shape,dtype=float,order='C')
    # 1)默认为浮点数
    arr2 = numpy.zeros((3, 2))
    print(arr2)
    # 2)设置类型为整数
    arr3 = numpy.zeros((3, 2), dtype=numpy.int32)
    print(arr3)
    # 3)自定义类型
    arr4 = numpy.zeros((2, 3), dtype=[('name', 'S20'), ('age', 'i4')])
    print(arr4)

    # 3、numpy.ones创建指定形状的数组，数组元素以1来填充：
    # numpy.ones(shape, dtype=None, order='C')
    # 1)默认为浮点数
    x = numpy.ones(5)
    print(x)
    # 2)自定义类型
    x = numpy.ones([2, 2], dtype=int)
    print(x)
