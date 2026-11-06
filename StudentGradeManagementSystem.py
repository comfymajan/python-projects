dic={}
people = int(input("Enter the number of people:"))
for i in range(people):
    name = input("Enter the name:")
    grade = int(input("Enter the grade:"))
    dic[name] = grade
total = 0
for grade in dic.values():
    total+=grade
average = total/people
max_num=max(dic.values())
min_num=min(dic.values())
print(("Total: ",total))
print(("Average: ",average))
print(("Max: ",max_num))
print(("Min: ",min_num))
while True:
    choice = input("Enter a name or a grade(or exit): ")
    if choice.lower() in dic:
        print("Grade: ",dic[choice])
    elif choice == "Exit":
        break
    else:
          found = False
          for name,grade in dic.items():
              if str(choice)==choice:
                  print("Student: ",name)
                  found = True
          if not found:
              print("Not found")
