userName = input("What is your name? ").strip().capitalize()
userCountry = input("Where are you from? ").strip().lower()
student = input("Are you a student? ").strip().lower()
courseName = "Python Course"
coursePrice = 100
countries_1 = ["egypt", "turkey", "syria", "palastine", "tunis", "libya"]
countries_2 = ["ksa", "qatar", "kuwait", "Bahrain", "saudi arabia"]
countries_3 = ["usa", "italy", "barazil", "england", "germany"]


print(f"Hi {userName}!")

if userCountry in countries_1:

    if student == "yes":
        print(f'The course "{courseName}" price is: ${coursePrice - 90}')

    else:
        print(f'The course "{courseName}" price is: ${coursePrice - 80}')


elif userCountry in countries_2:

    if student == "yes":
        print(f'The course "{courseName}" price is: ${coursePrice - 70}')

    else:
        print(f'The course "{courseName}" price is: ${coursePrice - 60}')


elif userCountry in countries_3:

    print(f'The course "{courseName}" price is: ${coursePrice - 0}')


else:

    if student == "yes":
        print(f'The course "{courseName}" price is: ${coursePrice - 40}')

    else:
        print(f'The course "{courseName}" price is: ${coursePrice - 30}')
