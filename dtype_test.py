import numpy

if __name__ == '__main__':
    # 数据类型对象（numpy.dtype类的实例）用来描述与数组对应的内存区域是如何使用，它描述了数据的以下几个方面：：
    # 1、数据的类型（整数，浮点数或者Python对象）
    # 2、数据的大小（例如， 整数使用多少个字节存储）
    # 3、数据的字节顺序（小端法或大端法）
    # 4、在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
    # 5、如果数据类型是子数组，那么它的形状和数据类型是什么。
    # 字节顺序是通过对数据类型预先设定 < 或 > 来决定的。 < 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。
    # > 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。

    # dtype对象是使用以下语法构造的：
    # dt = numpy.dtype(object, align, copy)

    # 使用标量类型
    dt1 = numpy.dtype(numpy.int32)
    print(dt1)

    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    dt2 = numpy.dtype('i8')
    print(dt2)

    # 字节顺序标注
    dt3 = numpy.dtype('<i4')
    print(dt3)

    # 1、下面实例展示结构化数据类型的使用，类型字段和对应的实际类型将被创建。
    # 首先创建结构化数据类型
    dt4 = numpy.dtype([('age', numpy.int8)])
    # print(dt4)
    # 将数据类型应用于 ndarray 对象
    arr1 = numpy.array([(18,), (24,), (30,)], dtype=dt4)
    print(arr1)
    # 类型字段名可以用于存取实际的 age 列
    print(arr1['age'])

    # 2、下面的示例定义一个结构化数据类型student，包含字符串字段name，整数字段age，及浮点字段marks，并将这个dtype应用到ndarray对象。
    student = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    print(student)
    arr2 = numpy.array([('cmm', 22, 98.3), ('yj', 21, 100.0)], dtype=student)
    print(arr2)
