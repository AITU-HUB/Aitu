# # beatles : list = []
# # beatles.append("John Lennon")
# # beatles.append("Paul McCartney")
# # beatles.append("George Harrison")
# # beatles.append("Stu Sutcliffe")
# # beatles.append("Pete Best")
# # while True:
# #      for i in range(len(beatles)):
# #           print(f"{i} -- {beatles[i]}")
# #      choice = int(input("Write index who you want to remove\nOr length of the list to break: "))
# #      if choice >= len(beatles):
# #           break
# #      del beatles[e]
# # beatles.insert(0, "Ringo Starr")
# # print(beatles)

# # students = [ ("Alice", 85, 90), ("Bob", 78, 82), ("Charlie", 92, 88) ]
# # avg_f = 0
# # avg_l = 0
# # S = []
# # for name, first_score, last_score in students:
# #      S.append(StudentsC(name, first_score, last_score))
# #      avg_f += first_score
# #      avg_l += last_score
# # print("Average first score ", (avg_f / len(students)))
# # print("Average last score ", (avg_l / len(students)))
# # print(StudentsC.name, S, sep=" ")

# A = {"Alice", "Bob", "Charlie", "David"}
# B = {"Bob", "Eve", "Frank", "Alice"}
# C = {"Charlie", "Alice", "George"}
# listok = [A, B, C]

# isAllThree = {}
# isOnlyOne = {}
# atLeastOne = {}

# for i in A:
#      if i in B and i in C:
#           isAllThree[i] = True
# for i in range(len(listok)):
#      for j in listok[i]:
#           if j not in listok[i-1] and j not in listok[(i+1) % len(listok)]:
#                isOnlyOne[j] = True
#           if j not in atLeastOne:
#                atLeastOne[j] = True

# print("answered all three question: ", isAllThree)
# print("answered only one question: ", isOnlyOne)
# print("Answered 1+ questions: ", atLeastOne)

# iteratedList = iter(atLeastOne)

# while True:
#      item = next(iteratedList, "end")
#      if item == "end":
#           break
#      print(item)

beatles : list = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
beatles.append("Stu Sutcliffe")
beatles.append("Pete Best")
while True:
 for i in range(len(beatles)):
   print(f"{i} -- {beatles[i]}")
 choice = int(input("Write index who you want to remove\nOr length of thelist to break: "))
 if choice >= len(beatles):
  break
 del beatles[e]
beatles.insert(0, "Ringo Starr")
print(beatles)