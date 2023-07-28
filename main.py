age = int(input("Type in your age: "))

if (age >= 0 and age <= 11):
    print("You are a child")
elif (age >= 12 and age <= 17):
    print("You are a teen")
elif (age > 18):
    print("You are an adult")