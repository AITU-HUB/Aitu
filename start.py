# # a = [3,7,2,9,4,7,1]
# # #это сумма
# # b=0
# # for x in a:
# #     b=b+x
# # print(b)

# # #это максимум 
# # m=a[0]

# # for x in a:
# #     if x>m:
# #         m=x
# # print(m)
# # b=0

# # for x in a:
# #     if x==7:
# #         b=b+1
# # print(b)
# # z=[]

# # for x in a:
# #     if x>5:
# #         z.append(x)
# # print(z)

# #нахождение fizzbuzz
# # # try:
    
# #     a=int(input("a:"))

# #     if a%5==0 and a%3==0:
# #         print("fizzbuzz")
# #     elif a%3==0:
# #         print("fizz")
# #     elif a%5==0:
# #         print("buzz")
# # except ValueError:
# #     print("not number")


# #избавление от дубликатов
# nums = [1, 4, 6, 2, 9, 3, 6, 1]

# new_list = []

# for x in nums:
#     if x not in new_list:
#         new_list.append(x)

# print(new_list)


# # a = [5, 1, 4, 2]

# #сартировка 
# # sorted_list = []

# # while len(a) > 0:
# #     min_value = a[0]
# #     for x in a:
# #         if x < min_value:
# #             min_value = x

# #     sorted_list.append(min_value)
# #     a.remove(min_value)

# # print(sorted_list)


# # n=int(input("n:"))

# # i = 1
# # t = 0

# # while i <= n:
# #     t += i
# #     i += 1
# # print(t)

# # a=input("a:")

# # r={}
# # for w in a:
# #     if w in r:
# #         r[w]+=1
# #     else:
# #         r[w]=1
# # print(r)

# # scores = {
# #     "math": 90,
# #     "physics": 85,
# #     "cs": 98,
# #     "history": 70
# # }
# # max_subject = None
# # max_score = -1

# # for subject in scores:
# #     if scores[subject] > max_score:
# #         max_score = scores[subject]
# #         max_subject = subject

# # print(max_subject, max_score)

# # a=float(input("a:"))
# # b=float(input("b:"))
# # if b==0:
# #     print("на 0 делить нельза")
# # print(a/b)
# # a = [1.5, 2.5, 3.0, 4.0]
# # z=float(0)
# # b=float(0)
# # for x in a:
# #     b=b+x
# #     z+=1
# # print(b/z)

# def word_count(text):
#     words = text.split()
#     r={}
#     for w in words:
#         if w in r:
#             r[w]+=1
#         else:
#             r[w]=1
    
#     return r
# # text = "python is good and python is fast"
# # print(word_count(text))

# # print( "результат :",abs(-52564))

# # t = (10, 20, 30, 40)
# # x=0
# # for i in t:
# #     x+=i
# # print(x)
# # m=t[0]
# # for x in t:
# #     if x>m:
# #         m=x
# # print(m)
# # можно проста поменять скопки из кватратных в фигурные 
# # nums ={1, 2, 2, 3, 4, 4, 5}

# # print(nums)
# #попробавал этот способ  получилось 
# # nums = [1, 2, 2, 3, 4, 4, 5]
# # data=set()


# # for x in nums:
# #     if x not in data:
# #         data.add(x)

# # print(data)
# # data={1, 2, 2, 3, 4, 4, 5}
# # #проверка элеманта по наличию
# # for  item in data:
# #     if item == 3:
# #         print("да есть:", item)
# # # добавление новых элементов 
# # data.add(10)
# # #удалить число
# # data.remove(2)

# # print(data)

# # def stats(nums):
# #     total=0
# #     count=0

# #     for x in nums:
# #         total+=x
# #         count+=1
# #     avg=total/count
# #     return(total,count,avg)

# # data=[1,2,3,4]
# # print(stats(data))


# # nums = [1, 2, 3, 4, 5]
# # res = list(map(lambda x: x ** 2, nums))
# # print(res)

# # a = [1, 2, 3, 4, 5, 6]
# # b = list(filter(lambda x: x % 2 == 0, a))
# # print(b)


# # a=int(input("a:"))

# # for i in range(1,a):
# #     if i % 2 == 0:
# #         print(i)
# # x=0
# # for i in range(1,a+1):
# #     x+=i
# # print(x)
# # for i in range(0,a,3):
# #     print(i)


# # a=[ 2 , 4 , 6]
# # s=0
# # for i in a:
# #     s+=i
    
# # print(s)

# # a=[5, 12, 3, 9]
# # m=a[0]

# # for x in a:
# #     if x>m:
# #         m=x
# # print(m)

# # a="python"
# # for i in a:
# #     print(i)
# # s=50
# # while s>=1:
# #     print(s)
# #     s-=1

# # s=0
# # a=int(input("a:"))
# # while a != 0:
# #     s+=1
# #     a=int(input("a:2"))
# # print(s)

# # s=0
# # a=int(input("a:"))
# # while a != 0:
# #     s=s+a
# #     a=int(input("a:"))
   
# # print(s)


# # a=int(input("a:"))
# # s=0

# # while a != 0:
# #     s+=1
# #     a//=10
# # print(s)

# # text = "hello world"
# # r={}

# # for c in text:
# #     if c in r:
# #         r[c] += 1
# #     else:
# #         r[c] = 1
# # print(r)



# # def word_count(text):
# #     words = text.split()
# #     r={}
# #     for w in words:
# #         if w in r:
# #             r[w]+=1
# #         else:
# #             r[w]=1
    
# #     return r
# # text = "one two two three three three"

# # print(word_count(text))

# for i in range(1):
#     ...

# def analyze(data):
#     """
#     Функция принимает строку с данными пользователей
#     и возвращает словарь с аналитикой.
   
#     """

#     # Множество для хранения уникальных имён
#     # set автоматически убирает дубликаты
#     names = set()

#     # Словарь для хранения возрастов
#     # ключ   -> имя
#     # значение -> (минимальный возраст, максимальный возраст)
#     ages = {}

#     # Переменные для подсчёта среднего возраста
#     total_age = 0   # сумма всех возрастов
#     count = 0       # количество записей

#     # Разбиваем исходную строку на отдельные записи
#     # Разделитель между записями — ;
#     records = data.split(";")

#     # Обрабатываем каждую запись по очереди
#     for record in records:

#         # Убираем лишние пробелы в начале и в конце строки
#         record = record.strip()

#         # Разделяем запись на имя и возраст
#         # Пример: "Alice,18" -> ["Alice", "18"]
#         name, age = record.split(",")

#         # Возраст из строки превращаем в число
#         age = int(age)

#         # Добавляем имя в множество уникальных пользователей
#         names.add(name)

#         # Если пользователь уже встречался
#         if name in ages:
#             # Достаём текущие минимальный и максимальный возраст
#             min_age, max_age = ages[name]

#             # Проверяем, не меньше ли текущий возраст
#             if age < min_age:
#                 min_age = age

#             # Проверяем, не больше ли текущий возраст
#             if age > max_age:
#                 max_age = age

#             # Обновляем данные в словаре
#             ages[name] = (min_age, max_age)

#         else:
#             # Если пользователь встретился впервые,
#             # минимальный и максимальный возраст одинаковые
#             ages[name] = (age, age)

#         # Добавляем возраст к общей сумме
#         total_age += age

#         # Увеличиваем количество записей
#         count += 1

#     # Формируем итоговый результат
#     result = {
#         # frozenset — неизменяемое множество уникальных имён
#         "unique_users": frozenset(names),

#         # словарь с возрастной статистикой
#         "ages": ages,

#         # средний возраст (float)
#         "average_age": total_age / count
#     }

#     # Возвращаем результат работы функции
#     return result

# data = "Alice,12; Bob,20; Alice,18; Charlie,22; Bob,20; Bob,21"

# result = analyze(data)
# print(result)

# text = "aabccc"


# r={}
# for i in text :
#     if i in r:
#         r[i]+=1
#     else:
#         r[i]=1
# print(r)

# nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# a=[]

# for i in nums:
#     if i not in a:
#         a.append(i)

# z=[]
# while len(a)>0:
#     m=a[0]
#     for i in a:
#         if i < m:
#             m=i
#     z.append(m)
#     a.remove(m)
   
# print(z)


# def is_even(n):
#     return n%2==0
# print(is_even(7))

# a = [1, 2, 3, 4, 5, 6]

# b = list(filter(lambda x: x % 2 == 0, a))

# b = list(map(lambda x: x ** 2, b))

# print(b)


# text = "cat dog cat bird dog cat"
# word = text.split()
# r={}

# for w in word:
#     if w in r:
#         r[w]+=1
#     else:
#         r[w]=1
# print(r)

# def unique_words(text):
#     word=text.split()
#     result=set()
#     for i in word:
#         result.add(i)
#     return result
# text = "cat dog cat bird dog cat"

# print(unique_words(text))


# def most_common_word(text):
#     word=text.split()
#     r={}
#     for w in word:
#         if w in r:
#             r[w]+=1
#         else:
#             r[w]=1
#     mw = None
#     mc = 0

#     for w in r:
#         if r[w] > mc:
#             mc = r[w]
#             mw = w


#     return mw
# text = "cat dog cat bird dog cat"
# print(most_common_word(text))

# a=int(input('a:'))
# b=int(input('b:'))
# print(a+b)

# a,b=map(int,input ().split())
# print(a+b)


