#coding=gbk
#2-1
message = '我爱编程，我爱python。'
print(message)

#2-2
message = 'python是我最喜欢的编程语言，它简单易学，功能强大。'
print(message)

#2.3字符串

#2.3.1使用方法修改字符串大小写
#将首字母变为大写
name = 'ada lovelace'
print(name.title())
#将字母全部变为大写
name = 'Ada Lovelace'
print(name.upper())
#将首字母变为小写
print(name.lower())

#2.3.2合并(拼接)字符串
first_name = 'amos'
last_name = 'niu'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello,' + full_name.title() + '!')

message = 'Hello,' + full_name.title() + '!'
print(message)

#2.3.3使用制表符或换行符来添加空白
#制表符\t
print('Python')
print('\tPython')
#换行符\n
print('我喜欢编程，编程使我快乐，尤其是Python')
print('我喜欢编程，\n编程使我快乐，\n尤其是Python')
print('我喜欢编程，\n\t编程使我快乐，\n\t尤其是Python')

#2.3.4删除空白
country = '中国 '
print(country)
print(country.rstrip())
country = ' 中国'
print(country.lstrip())
country = ' 中国 '
print(country.strip())

#2.3.5使用字符串时避免语法错误
#正确使用单引号和双引号
message = "I'am Amos Niu."
print(message)
#message = 'I'am Amos Niu.'这种写法会报语法错误
#双引号中间有单引号，不报错，单引号中间字符串有单引号会报错

#2.3.6Python2中的print语句
# print"Hello, Python World!"

#2-3
user_name = 'Amos Niu'
print('Hello' + ' ' + user_name + ',' + 'would you like to learn some Python today?')

#2-4
user_name = 'Amos Niu'
print(user_name.lower())
print(user_name.upper())
print(user_name.title())

#2-5
print('《巨人的陨落》中说到：' + '\n\t除非必要，先别开口。')

#2-6
famous_person = 'Amos Niu'
message = 'Hello' + ' ' + famous_person + ',' + 'would you like to learn some Python today?'
print(message)

#2-7
user_name = ' Amos Niu '
print(user_name.strip())
print('\n\t' + user_name.strip())

#2.4数字

#2.4.1整数
print(1 + 2)
print(3 - 2)
print(2 * 3)
print(3 / 2)
#两个乘号代表乘方
print(3 ** 2)
print(10 ** 6)
print((2+3) * 4)

#2.4.2浮点数
print(0.1 + 0.1)
#结果包含的小数位数是不确定的，如下：
print(0.2 + 0.1)
print(3 * 0.1)

#2.4.3使用函数str()避免类型错误
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)

#2.4.4 Python2中的整数
#在Python2中，两个整数相除的到的结果稍有不同，如：3 / 2 = 1 
#结果只包含整数部分，小数部分会被直接删除，而非四舍五入
#在Python2中若要避免这种情况，则需要确保至少有一个操作数为浮点数，即：3.0 / 2 = 1.5
#或：3 / 2.0 = 1.5

#2-8
a = 3 + 5
b = 11 - 3
c = 2 * 4
d = 16 / 2
print(a)
print(b)
print(c)
print(d)

#2-9
favorite_number = 188
message = '我最喜欢的数字是：' + str(favorite_number)
print(message)

#2.5注释

#2.5.1如何编写注释
#"#"后面的内容会被Python解释器忽略

#2.5.2该编写什么样的注释
