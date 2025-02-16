from classes import *

# ----

def choice_catalog(category, genres):
    main.clear_screen()
    i = 0
    items = []
    if category == "movies" or category == "all":
        i = movie_catalog.show_catalog(genres, 1, items)
    
    ads.show_random_ad()

    if category == "shows" or category == "all":
        i += shows_catalog.show_catalog(genres, i, items)

    ads.show_random_ad()
    
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
        main.clear_screen()
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
        main.clear_screen()
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
        main.clear_screen()
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
            main.clear_screen()
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
        main.clear_screen()
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


login_menu()
