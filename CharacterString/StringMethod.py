#方法center通过在两边添加填充字符（默认为空格）让字符串居中。
print( "The Middle by Jimmy Eat World".center(39) )
print( "The Middle by Jimmy Eat World".center(39, "*") )

#方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
#可指定搜索的起点和终点
print()
print( 'With a moo-moo here, and a moo-moo there'.find('moo') )
S='With a moo-moo here, and a moo-moo there'
print(S.find('moo'))
print(S.find('moot'))  #错误返回值-1
print(S.find('moo',8,16))  #指定搜索的起点和终点

#join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
#join不修改原来的变量
#所合并序列的元素必须都是字符串
print()
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

#方法lower返回字符串的小写版本。
print()
print( 'Trondheim Hammer Dance'.lower())

#方法replace将指定子串都替换为另一个字符串，并返回替换后的结果。
print()
print( 'This is a test,is a book'.replace('is', 'eez') )

#split是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
#如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符 等）处进行拆分。
print()
print('1+2+3+4+5'.split('+') )

#方法strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果
#与lower一样，需要将输入与存储的值进行比较时，strip很有用。回到前面介绍lower时使用 的用户名示例，并假定用户输入用户名时不小心在末尾加上了一个空格。
#你还可在一个字符串参数中指定要删除哪些字符。只删除开头或末尾的指定字符，
print()
print( '    internal whitespace is kept***    '.strip() )
print( '***internal *whitespace is kept***'.strip('*') )

#方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
#使用translate前必须创建一个转换表
#要创建转换表，可对字符串类型str调用方法maketrans，这个方法接受两个参数：两个长度相同的字符串第一个替换第二个
#还可提供可选的第三个参数，指定要将哪些字母删除
print()
table = str.maketrans('cs', 'kz','i')
print('this is an incredible test'.translate(table) )





