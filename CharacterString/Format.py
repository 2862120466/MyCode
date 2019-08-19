# 所有标准序列操作（索引、切片、乘法、成员资格检查、长度、小值和 大值）
# 都适用于字符串，但别忘了字符串是不可变的，因此所有的元素赋值和切片赋值都是非 法的。

# 使用字符串格式设 置运算符——百分号。这个运算符的行为类似于C语言中的经典函数printf：在%左边指定一个字符串（格式字符串），
# 并在右边指定要设置其格式的值。指定要设置其格式的值时，可使用单个 值（如字符串或数字），
# 可使用元组（如果要设置多个值的格式），还可使用字典（这将在下一章 讨论），其中常见的是元组。

print("Hello,%s.%s enough for ya" % ('world','Hot'))

print("{},{} and {}".format("first","second","third"))
print("{2},{0} and {1}".format("second","third","first"))

print( "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to") )

print("{name} is approximately {value:.2f}.".format(value=3.141592653,name='pai'))









