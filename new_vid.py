from classes import *

def login_menu():
    """
    Primeiro menu do programa. O usuário pode logar ou criar uma conta aqui.
    """
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
    """
    Segundo menu do programa. Aqui o usuário pode criar, escolher ou deletar um perfil e configurar sua conta.
    """
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
    """
    Terceiro menu do programa. Aqui pode ser escolhido como o usuário ira ver o(s) catálogo(s).
    """
    while True:
        profile = main.logged_user.profile_choosen

        main.clear_screen()
        print(f"Hello, {profile.first_name}, what will you watch today?")
        opt = int(input("Browse by:\n1 - Recommendations based on your preferences 2 - Category 3 - Genre 4 - Bookmarks 5 - Watch History 6 - Exit\n"))

        if opt == 1:
            main.recommendations_page()
        elif opt == 2:
            main.category_page()
        elif opt == 3:
            main.genre_page()
        elif opt == 4:
            profile.bookmarks_or_watch_history_page("bookmarks")
        elif opt == 5:
            profile.bookmarks_or_watch_history_page("history")
        elif opt == 6:
            break

login_menu()
