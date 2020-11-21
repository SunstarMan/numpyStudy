import numpy

if __name__ == '__main__':
    # 了解NumPy数组的一些基本属性。
    # NumPy数组的维数称为秩（rank），秩就是轴的数量，即数组的维度:
    # 一维数组的秩为1，
    # 二维数组的秩为2，以此类推。
    # 在NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说:
    # 二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是NumPy中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。
    # 很多时候可以声明axis:
    # axis = 0，表示沿着第0轴进行操作，即对每一列进行操作；
    # axis = 1，表示沿着第1轴进行操作，即对每一行进行操作。

    # 1、ndarray.ndim用于返回数组的维数，等于秩。
    a = numpy.arange(24)  # a 现只有一个维度,arange(24)表示数组的size为24
    print(a.ndim)
    # 现在调整其大小
    b = a.reshape(2, 3, 4)  # 2*3*4=24，即为a的size
    print(b.ndim)

    # 2、ndarray.shape表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即ndim属性(秩)。比如：
    # 一个二维数组，其维度表示"行数"和"列数"。
    # ndarray.shape也可以用于调整数组大小;对于矩阵，n 行 m 列
    c = numpy.array([1, 2, 3, 4, 5, 6])
    print(c)
    print(c.shape)
    c.shape = (3, 2)
    print(c)
    c.shape = (1, 6)
    print(c)
    d = c.reshape(2, 3)
    print(d)

    # 3、ndarray.itemsize以字节的形式返回数组中每一个元素的大小。
    # 例如，一个元素类型为float64的数组itemsize属性值为8(float64占用64个bits，每个字节长度为8bits，所以64/8，占用8个字节）
    # 又如，一个元素类型为complex32的数组itemsize属性为4（32 / 8）。
    x = numpy.array([1, 2, 3, 4, 5, 6], dtype=numpy.int32)
    x2 = numpy.array([1 + 2j, 2, 3], dtype=complex)
    print(x.size)  # 数组元素的总个数，相当于 .shape 中 n*m 的值
    print(x[1])
    print(x[1].itemsize)
    print(x.itemsize)
    print(x2)
    print(x2.itemsize)
    print(x2.real)  # ndarray元素的实部
    print(x2.imag)  # ndarray元素的虚部

    # 4、ndarray.flags返回ndarray对象的内存信息，包含以下属性：
    # C_CONTIGUOUS(C)数据是在一个单一的C风格的连续段中
    # F_CONTIGUOUS(F)数据是在一个单一的Fortran风格的连续段中
    # OWNDATA(O)数组拥有它所使用的内存或从另一个对象中借用它
    # WRITEABLE(W)数据区域可以被写入，将该值设置为False，则数据为只读
    # ALIGNED(A)数据和所有元素都适当地对齐到硬件上
    # UPDATEIFCOPY(U)这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
    print(x.flags)
