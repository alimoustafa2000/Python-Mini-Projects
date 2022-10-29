# username
u_name = input("What is your name? ").strip().capitalize()


# user id
u_id = int(input("Enter your ID: ").strip())


# import SQLite module
import sqlite3


# connect database
db = sqlite3.connect("Skills app.db")


# setup the cursor
cr = db.cursor()


# create IDs table
cr.execute("create table if not exists IDs (user_id integer unique)")


# insert data
try:

    IDs_list = [1, 2, 3, 4, 5]

    for Id in IDs_list:

        cr.execute(F"insert into IDs (user_id) values ('{Id}')")

except:

    pass


# commit changes
db.commit()


# Fetch Data
cr.execute(f"select user_id from IDs where user_id = '{u_id}'")

IDs = cr.fetchone()


# database password
password = ['skills_database@12345']

tries = 5


# APP CODE
def start_the_app():

    # input message
    input_message = """
    What do you want to do?

    - "s" => Show all skills.
    - "a" => Add new skill.
    - "d" => Delete skill.
    - "u"=> Update skill progress.
    - "q" => Quit the app.

    => Choose an option: 
    """


    # user input
    user_input = input(input_message).strip().lower()


    # create skills table and fields
    cr.execute("create table if not exists skills (user_id integer, skill_name text, skill_progress integer)")


    # Commit and close database
    def commit_and_close():

        db.commit()
        db.close()


    # ------------------
    # commands functions
    # ------------------

    def show_all_skills():

        # show skills 
        cr.execute(f"select * from skills where user_id = '{u_id}'")

        results = cr.fetchall()

        print(f"You have '{len(results)}' skills")

        for row in results:

            print(f"- Skill name => '{row[1]}', Skill progress => '{row[2]}'%")


    def add_new_skill():

        # insert data
        skill = input("Write Skill Name: ").strip().capitalize()

        cr.execute(f"select skill_name from skills where skill_name = '{skill}' and user_id = '{u_id}'")

        results = cr.fetchone()

        if results == None:

            progress = input("Write Skill Progress: ").strip()

            cr.execute(f"insert into skills (user_id, skill_name, skill_progress) values ('{u_id}', '{skill}', '{progress}')")

            print(f"'{skill}' is added")

        else:

            print(f"This skill '{skill}' is already exists")

            U_input = input("Do you want to update its progress? Yes or No ").strip().lower()

            if U_input == "yes":

                new_progress = input("Write the new Skill Progress: ").strip()

                cr.execute(f"update skills set skill_progress = '{new_progress}' where skill_name = '{skill}' and user_id = '{u_id}'")

                print(f"'{skill}' progress is updated")

            else:

                commit_and_close()


    def delete_skill():

        # delete data
        skill = input("Write Skill Name: ").strip().capitalize()

        cr.execute(f"delete from skills where skill_name = '{skill}' and user_id = '{u_id}'")

        print(f"'{skill}' is deleted")


    def update_skill_progress():

        # update data
        skill = input("Write the Skill Name that you want to update its progress: ").strip().capitalize()

        new_progress = input("Write the new Skill Progress: ").strip()

        cr.execute(f"update skills set skill_progress = '{new_progress}' where skill_name = '{skill}' and user_id = '{u_id}'")

        print(f"'{skill}' progress is updated")


    # check if the command is present
    commands_list = ["s", "a", "d", "u", "q"]

    if user_input in commands_list:

        if user_input == "s":

            show_all_skills()
            commit_and_close()

        elif user_input == "a":

            add_new_skill()
            commit_and_close()

        elif user_input == "d":

            delete_skill()
            commit_and_close()

        elif user_input == "u":

            update_skill_progress()
            commit_and_close()

        else:

            commit_and_close()
            print("App is closed")


    else:

        print(f"Sorry, Your command '{user_input}' not found")


# check if the u_id is present
if IDs != None:

    print(f"Welcome {u_name}!")

    start_the_app()

else:

    print(f"Sorry, You have no access to this database")


    # check if the user want to have access or no
    ques = input("Do you want to have access to this database? Yes or No ").strip().lower()

    if ques == 'yes':

        user_password = input("Please enter your password. ").strip()

        # check password
        # if password is right
        if user_password in password:

            cr.execute(f"insert into IDs (user_id) values ('{u_id}')")

            print(f"Welcome {u_name}!")

            print("Now you have access to this database")

            start_the_app()

        # if password is wrong
        else:

            while user_password not in password:

                tries -= 1

                if tries == 0:

                    print('Wrong password, Last chance left')

                elif tries == 1:

                    print('Wrong password, 1 chance left')

                else:

                    print(f'Wrong password, {tries} chances left')

                user_password = input("Enter your password. ")

                if tries == 0 and user_password not in password:

                    print('All chances are finished!')

                    print("You have no access to this database.")

                    break

            else:

                cr.execute(f"insert into IDs (user_id) values ('{u_id}')")

                print(f"Welcome {u_name}!")

                print("Now you have access to this database")

                start_the_app()

    if ques == 'no':

        print("You Are Not Added.")
