#coding=gbk
#2-1
message = '�Ұ���̣��Ұ�python��'
print(message)

#2-2
message = 'python������ϲ���ı�����ԣ�������ѧ������ǿ��'
print(message)

#2.3�ַ���

#2.3.1ʹ�÷����޸��ַ�����Сд
#������ĸ��Ϊ��д
name = 'ada lovelace'
print(name.title())
#����ĸȫ����Ϊ��д
name = 'Ada Lovelace'
print(name.upper())
#������ĸ��ΪСд
print(name.lower())

#2.3.2�ϲ�(ƴ��)�ַ���
first_name = 'amos'
last_name = 'niu'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello,' + full_name.title() + '!')

message = 'Hello,' + full_name.title() + '!'
print(message)

#2.3.3ʹ���Ʊ�����з�����ӿհ�
#�Ʊ��\t
print('Python')
print('\tPython')
#���з�\n
print('��ϲ����̣����ʹ�ҿ��֣�������Python')
print('��ϲ����̣�\n���ʹ�ҿ��֣�\n������Python')
print('��ϲ����̣�\n\t���ʹ�ҿ��֣�\n\t������Python')

#2.3.4ɾ���հ�
country = '�й� '
print(country)
print(country.rstrip())
country = ' �й�'
print(country.lstrip())
country = ' �й� '
print(country.strip())

#2.3.5ʹ���ַ���ʱ�����﷨����
#��ȷʹ�õ����ź�˫����
message = "I'am Amos Niu."
print(message)
#message = 'I'am Amos Niu.'����д���ᱨ�﷨����
#˫�����м��е����ţ��������������м��ַ����е����Żᱨ��

#2.3.6Python2�е�print���
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
print('�����˵����䡷��˵����' + '\n\t���Ǳ�Ҫ���ȱ𿪿ڡ�')

#2-6
famous_person = 'Amos Niu'
message = 'Hello' + ' ' + famous_person + ',' + 'would you like to learn some Python today?'
print(message)

#2-7
user_name = ' Amos Niu '
print(user_name.strip())
print('\n\t' + user_name.strip())

#2.4����

#2.4.1����
print(1 + 2)
print(3 - 2)
print(2 * 3)
print(3 / 2)
#�����˺Ŵ���˷�
print(3 ** 2)
print(10 ** 6)
print((2+3) * 4)

#2.4.2������
print(0.1 + 0.1)
#���������С��λ���ǲ�ȷ���ģ����£�
print(0.2 + 0.1)
print(3 * 0.1)

#2.4.3ʹ�ú���str()�������ʹ���
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)

#2.4.4 Python2�е�����
#��Python2�У�������������ĵ��Ľ�����в�ͬ���磺3 / 2 = 1 
#���ֻ�����������֣�С�����ֻᱻֱ��ɾ����������������
#��Python2����Ҫ�����������������Ҫȷ��������һ��������Ϊ������������3.0 / 2 = 1.5
#��3 / 2.0 = 1.5

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
message = '����ϲ���������ǣ�' + str(favorite_number)
print(message)

#2.5ע��

#2.5.1��α�дע��
#"#"��������ݻᱻPython����������

#2.5.2�ñ�дʲô����ע��
