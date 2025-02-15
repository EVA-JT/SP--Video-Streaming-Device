import os
import random

from new_data import *

user_data = {}

class Program:
    def __init__(self):
        self.logged_user = None

    def create_user(self):
        email = input("Enter your email: ")
        while email in user_data:
            email = input("This email has already been registered, please try again.")
        
        while True:
            password = input("Enter your password: ")
            rpt_password = input ("Enter your password again: ")
            if password != rpt_password:
                print("The two passwords are not the same, try again.")
            else:
                break
        payment_plan = 0
        print("After your 7-day free trial, what type of payment plan would you like?\n1 - Monthly 2 - Quartely 3 - Annual")
        while payment_plan not in range(1,4):
            payment_plan = int(input())

        user = User_Account(email, password, payment_plan)
        user_data[email] = user

    def user_login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        success = 0

        if email in user_data:
            user = user_data[email]

            if password == user.password:
                self.logged_user = user
                success = 1

        if success:
            input("Login succesful. Press enter to continue.")
            return 1
        else:
            input("Wrong email or password. Press enter to continue.")
            return 0

    def user_management(self):
        failsafe = 1

        while True:
            os.system('cls')
            print(f"Hello user {self.logged_user.email} what would you like to change in your account?")
            opt = 0

            while opt not in range(1,6):
                opt = int(input("1 - Change email 2 - Change password 3 - Change payment plan 4 - Delete account 5 - Exit menu"))
            if opt == 1:
                self.logged_user.change_email()
            elif opt == 2:
                self.logged_user.change_password()
            elif opt == 3:
                self.logged_user.change_payment_plan()
            elif opt == 4:
                user_data.pop(self.logged_user.email)
                self.logged_user = None
                failsafe = 0

            return failsafe

class User_Account:
    def __init__(self,email,password,payment_plan):
        self.email = email
        self.password = password
        self.payment_plan = payment_plan

        self.profile_list = []
        self.profile_choosen = None

    def print_user_profile(self):
        for i in range(len(self.profile_list)):
            print(f"{i} - {self.profile_list[i].first_name} {self.profile_list[i].last_name}")

    def choose_user_profile(self):
        self.print_user_profile()
        #user_choice = 100
        #print(len(self.profile_list) - 1)
        #while user_choice not in range(0, len(self.profile_list) - 1): #REVER
        user_choice = int(input("Enter which profile you would like to use: "))
        self.profile_choosen = self.profile_list[user_choice]

    def delete_user_profile(self):
        self.print_user_profile()
        #user_choice = 100
        #while user_choice not in range(len(self.profile_list) - 1): #REVER
        user_choice = int(input("Enter which profile you would like to delete: "))
        assurance = str(input("Are you sure? Y/N\n").lower())
        if assurance == "y":
            self.profile_list.pop(user_choice)
    
    def create_user_profile(self):
        os.system('cls')
        print("Create a profile!")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        age = int(input("Your age: "))
        parental_controls = False

        if age < 15:
            while True:
                opt = input("Would you like to enable parental controls on this profile? Y/N\n").lower()
                if opt == "y":
                    print("Parental Controls were enabled.")
                    parental_controls = True
                    break
                elif opt == "n":
                    print("Parental Controls were not enabled.")
                    break
        
        while True:
            category_preference = input("Do you prefer: movies, shows or both? ").lower()

            if category_preference == "movies" or category_preference == "shows":
                category_preference = category_preference[:-1] # remove a ultima letra 's'
                break

            elif category_preference == "both":
                category_preference = "all"
                break

            else:
                input("Category not available. Press enter to try again")

        g_l = genres_list.copy() #copia a lista de generos para g_l
        genre_preference = []
        while (len(g_l) >= 1):
            print("Enter your favorite genres or 'cancel' to exit.")
            for genre in g_l:
                print(f"{genre.title()} | ", end='') #printa os generos disponiveis

            opt = input("\n").lower()

            if opt == "cancel":
                break

            elif opt in genres_list and opt not in genre_preference: #se o genero digitado estiver em genres_list e não estiver em genre_preference, ele é adicionado
                genre_preference.append(opt)
                g_l.remove(opt)

            else:
                input("This genre is not availabe. Press enter to try again.")

        if not genre_preference: #se a lista estiver vazia então os generos favoritos serão todos (genres_list)
            genre_preference = genres_list.copy()
        
        profile = Profile(first_name, last_name, age, category_preference, genre_preference, parental_controls)
        self.profile_list.append(profile)

    def change_email(self):
        while True:
            new_email = input("Enter your new e-mail or type 'out' to cancel")

            if new_email in user_data:
                input("This email has already been registered. Press enter to try again")
            elif new_email == "out":
                break
            else:
                assurance = input(f"Are you sure you want to change {self.email} to {new_email}? Y/N\n").lower()
                if assurance == "y":
                    user_data[new_email] = user_data.pop(self.email)
                    self.email = new_email
                    input("New email successfully registered. Press enter to exit")
                    break
    
    def change_password(self):
        while True:
            password = input("Enter your new password or type 'out' to cancel: ")

            if password == "out":
                break
            rpt_password = input("Enter your new password again: ")
            if password != rpt_password:
                input("The two passwords are not the same, press enter to try again")
            else:
                self.password = password
                input("Password changed successfully. Press enter to exit")
                break

    def change_payment_plan(self):
        print("There are still 7 days until the next billing.")
        opt = 0
        while opt not in range(1, 5):
            opt = int(input("What type of payment plan would you like?\n1 - Monthly 2 - Quartely 3 - Annual 4 - Cancel\n"))
        if opt == 4:
            return
        else:
            self.payment_plan = opt
            input("Payment plan changed successfully. Press enter to continue")
   
class Profile:
    def __init__(self, first_name, last_name, age, cat_preference, gen_preference, parental_controls):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.category_preference = cat_preference
        self.genre_preference = gen_preference
        self.parental_controls = parental_controls

        self.bandwidth = ""
        self.bookmarks = []
        self.watch_history = []

    def bandwidth_settings(self):
        if self.bandwidth == "":
            print("You haven't chosen your preferred quality.")
        else:
            print(f"Your current choosen quality is: {self.bandwidth}")
        
        while True:
            b_w = input("In what quality do you want to watch, 'Low', 'Medium' or 'High'? (We recommend 'High' for your bandwidth)\nType 'exit' to cancel.\n").lower()

            if b_w == "exit":
                break
            elif b_w in quality_list:
                self.bandwidth = b_w
                input(f"Your preferred quality is now {b_w}. Press enter to continue")
                break
    
    def bookmarks_or_watch_history_page(self, option):
        os.system('cls')
        choice = None

        if option == "bookmarks":
            choice = self.bookmarks
        else:
            choice = self.watch_history

        if len(choice) == 0:
            input(f"There are no items. Press enter to exit.")
        else:
            bm_list = []
            i = 1

            for item in choice:
                print(f"{i} - Title: {item.name}, Genre: {item.genre}")
                bm_list.append(item)
                i += 1

            opt = int(input("Enter wich item you want to watch (enter 0 to exit): "))
            if opt != 0:
                bm_list[opt - 1].show_details()


class Catalog:
    def __init__(self, catalog_name, item_dict):
        self.catalog_name = catalog_name
        self.catalog_dict = {}

        for genre in genres_list:
            self.catalog_dict[genre] = {}
        
        for key in item_dict:
            item = Watchable(key, item_dict[key])
            self.catalog_dict[item.genre][key] = item

    def show_catalog(self, genres, i, items):

        if isinstance(genres, str): #se 'genre' for uma string, transforma ela em uma lista
            genres = [genres]
        
        print(f"\n\t\t\t{self.catalog_name.title()}")

        for genre_key in genres:

            print(f"\n{genre_key.title()}")

            for item in self.catalog_dict[genre_key]:
                print(f"{i} - {item} | ", end ='')
                i += 1
                items.append(self.catalog_dict[genre_key][item])

            print()
        return i

class Item:
    def __init__(self, name, dictionary):
        self.name = name
        for key in dictionary: 
            setattr(self, key, dictionary[key])

class Watchable(Item):
    def watch(self):
        if main.logged_user.profile_choosen.bandwidth == "":
            while True:
                b_w = input("In what quality do you want to watch, 'Low', 'Medium' or 'High'? (We recommend 'High' for your bandwidth)\n").lower()

                if b_w in quality_list:
                    main.logged_user.profile_choosen.bandwidth = b_w
                    break
                else:
                    input("Error. Press enter to try again")
        
        main.logged_user.profile_choosen.watch_history.append(self)

        print("\n")
        #show_ad()
        input(f"You've just watched {self.name} in {main.logged_user.profile_choosen.bandwidth} quality. Press enter to continue")
    
    def bookmark(self):
        main.logged_user.profile_choosen.bookmarks.append(self)
        input(f"{self.name} has just been added to your bookmarks. Press enter to continue.")

    def print_reviews(self):
        reviews_dict = self.reviews
        reviews_total = 0
        scores_sum = 0
        scores_total = 0

        for reviwer in reviews_dict:
            if reviews_dict[reviwer]['review'] != "":
                print(f"{reviwer} : {reviews_dict[reviwer]['review']}")
                reviews_total += 1
            scores_sum += reviews_dict[reviwer]['score']
            scores_total += 1
        
        if scores_total != 0:
            print(f"The current score is: {scores_sum / scores_total}")
        else:
            print("There is no score at the moment.")
        
        if reviews_total == 0:
            print("There are no reviews at the moment")

    def review_page(self):
        reviews_dict = self.reviews

        score = int(input(f"What would you rate {self.name} out of 10?\n"))
        review = str(input("Write your review: "))

        reviews_dict[main.logged_user.profile_choosen.first_name] = {
            "score": score,
            "review": review
        }

        input("Your review has been saved. Press enter to continue.")

    def show_details(self):
        while True:
            os.system('cls')
            rating = rating_list[self.rating]

            print(f"Title: {self.name}\nSinopsis: {self.description}\nYear: {self.year}\nRating: {rating}\n")
            opt = int(input("1 - Watch 2 - Bookmark it 3 - Bandwidth settings 4 - Reviews 5 - Exit\n"))

            if opt == 1:
                self.watch()
            elif opt == 2:
                self.bookmark()
            elif opt == 3:
                main.logged_user.profile_choosen.bandwidth_settings()
            elif opt == 4:
                while True:
                    user_choice = int(input("Would you like to:\n1 - Leave a review 2 - See the current score and reviews 3 - Exit\n"))
                    if user_choice == 1:
                        self.review_page()
                    elif user_choice == 2:
                        self.print_reviews()
            else:
                break

class Ad(Item):
    pass

# ----

def choice_catalog(category, genres):
    os.system('cls')
    i = 0
    items = []
    if category == "movies" or category == "all":
        i = movie_catalog.show_catalog(genres, 1, items)
    if category == "shows" or category == "all":
        i += shows_catalog.show_catalog(genres, i, items)

    opt = int(input(f"\nEnter the number of wich item you want to watch (or enter '0' to exit).\n"))
    if opt == 0:
        return
    else:
        items[opt - 1].show_details()

def recommendations_page():
    profile = main.logged_user.profile_choosen

    genres = profile.genre_preference
    categories = profile.category_preference

    choice_catalog(categories, genres)

def category_page():
    while True:
        os.system('cls')
        print("Choose a category to browse on or type 'exit' to cancel.")

        opt = str(input("'Movies', 'Shows' or 'All'\n").lower())

        if opt == "exit":
            break

        elif opt in categories_list or opt == "all":
            choice_catalog(opt, genres_list)

        else:
            input("This category is not availabe, press enter to try again")

def genre_page():
    while True:
        os.system('cls')
        print("Enter the genre to browse on or type 'exit' to cancel.")

        for i in range(len(genres_list)):
            print(f"{genres_list[i].title()} | ", end='')

        opt = str(input("\n").lower())
        if opt == "exit":
            break
        elif opt in genres_list:
            choice_catalog("all", opt)
        else:
            input("This genre is not availabe, press enter to try again")
    
def login_menu():
    while True:
        os.system('cls')
        opt = 0
        while opt not in range(1, 4):
            opt = int(input("Welcome to [site name], would you like to:\n1 - Log in 2 - Create an account 3 - Log out\n"))

        if opt == 1:
            if main.user_login():
                initial_menu()
        elif opt == 2:
            main.create_user()
        elif opt == 3:
            break

def initial_menu():
    user = main.logged_user
    while True:
        if len(user.profile_list) == 0: #Inicio do programa, nenhum perfil criado
            user.create_user_profile()
        else:
            os.system('cls') #Limpa a tela
            print("Hello, would you like to access a profile or create a new one?")
            option = int(input("1 - Access a profile 2 - Create a new one 3 - Delete a profile 4 - Account settings 5 - Exit\n"))

            if option == 1:
                user.choose_user_profile()
                main_menu()
            elif option == 2:
                user.create_user_profile()
            elif option == 3:
                user.delete_user_profile()
            elif option == 4:
                res = main.user_management
                if res == 0:
                    return               
            elif option == 5:
                assurance = str(input("Are you sure you want to log out? Y/N\n").lower())
                if assurance == "y":
                    break

def main_menu():
    while True:
        profile = main.logged_user.profile_choosen
        os.system('cls')
        print(f"Hello, {profile.first_name}, what will you watch today?")
        opt = int(input("Browse by:\n1 - Recommendations based on your preferences 2 - Category 3 - Genre 4 - Bookmarks 5 - Watch History 6 - Exit\n"))

        if opt == 1:
            recommendations_page()
        elif opt == 2:
            category_page()
        elif opt == 3:
            genre_page()
        elif opt == 4:
            profile.bookmarks_or_watch_history_page("bookmarks")
        elif opt == 5:
            profile.bookmarks_or_watch_history_page("history")
        elif opt == 6:
            break

main = Program()
movie_catalog = Catalog("movie", movie_catalog)
shows_catalog = Catalog("show", show_catalog)
login_menu()
