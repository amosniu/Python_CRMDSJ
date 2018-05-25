#coding=gbk
#第三章 列表简介

#3.1列表是什么
#在Python中用[]表示列表，并用,分隔其中的元素
countrys = ['中国','美国','俄罗斯','日本','英国']
print(countrys)
#直接打印会将[]一并打印出来，这不是要让用户看到的输入，所以：

#3.1.1访问列表元素
print(countrys[0])
names = ['amos','marry','jack','mark','petter','robort']
#还可以调用字符串方法
print(names[0].title())

#3.1.2索引从0而不是从1
#索引指定为-1，即访问列表最后一个元素
print(countrys[-1])
#索引指定为-3，即返回列表倒数第三个元素
print(countrys[-3])

#3.1.3使用列表中的各个值
#使用拼接创建消息
message = countrys[0] + '是一个热爱和平的国家'
print(message)

#3-1姓名
print(names[0] + '\n' +
	  names[1] + '\n' +
	  names[2] + '\n' +
	  names[3] + '\n' +
	  names[4] + '\n' +
	  names[5])
	  
#3-2问候语
print('新年快乐哈！' + names[0])
print('新年快乐哈！' + names[1])
print('新年快乐哈！' + names[2])
print('新年快乐哈！' + names[3])
print('新年快乐哈！' + names[4])
print('新年快乐哈！' + names[5])

#3-3自己的列表
colors = ['red','blue','white','black','yellow','green']
print('我最喜欢的颜色是：' + colors[0])

#3.2修改，添加和删除元素
