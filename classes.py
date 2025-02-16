import os
import platform
import random
from data import *

user_data = {}

class Program:
    """
    Classe principal do programa. Cuida do usuario logado.

    :var :class:`User` logged_user: Usuario logado no momento.
    :var str system: Sistema do usuario.
    :var str clear_type: Qual comando deve ser usado para limpar a tela.
    """
    def __init__(self):
        self.logged_user = None
        self.system = platform.system()
        self.clear_type = None

        if self.system == "Windows":
            self.clear_type = "cls"
        else:
            self.clear_type = "clear"

    def create_user(self):
        """
        Cria um usuario (objeto) a partir do email, senha e plano de pagamento escolhido.
        """

        email = str(input("Enter your email: "))
        while email in user_data:
            email = str(input("This email has already been registered.\nEnter another email: "))
        
        while True:
            password = str(input("Enter your password: "))
            rpt_password = str(input("Enter your password again: "))
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
        """
        Pagina de login do usuario. Define o :obj:`User` que ficará em :var:`logged_user`.
        """
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        success = False

        if email in user_data:
            user = user_data[email]

            if password == user.password:
                self.logged_user = user
                success = True

        if success:
            input("Login succesful. Press enter to continue.")
            return True
        else:
            input("Wrong email or password. Press enter to continue.")
            return False

    def user_management(self):
        """
        Página de configurações da conta do usuario. Pode mudar o email, senha, plano de pagamento e até deletar a conta.
        """
        failsafe = 1

        while True:
            self.clear_screen()
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
        
    def clear_screen(self):
        """
        Limpa a tela usando o comando :var:`clear_type`.
        """
        os.system(self.clear_type)

class User_Account:
    """
    Classe da conta do usuário. Lida com o perfil escolhido e troca das informações como email e senha.

    :var str email: Email salvo do usuário
    :var str password: Senha salva do usuário
    :var int payment_plan: Plano de pagamento salvo.
    :var list profile_list: Lista de perfis criados.
    :var `Profile` choosen_profile: Perfil escolhido.
    """
    def __init__(self,email:str,password:str,payment_plan:int):
        self.email = email
        self.password = password
        self.payment_plan = payment_plan

        self.profile_list = []
        self.profile_choosen = None

    def profile_choice(self, option:str):
        """
        Printa os perfis criados, os enumera para a escolha e retorna a escolha do usuário.
        """
        for i in range(len(self.profile_list)):
            print(f"{i} - {self.profile_list[i].first_name} {self.profile_list[i].last_name}")

        while True:
            user_choice = int(input(f"Enter which profile you would like to {option}: "))
            if user_choice in range(0, (len(self.profile_list))):
                break  
        return user_choice

    def choose_user_profile(self):
        """
        Página de escolha de perfil. Determina o :var:`profile_choosen`.
        """
        user_choice = self.profile_choice("use") 
        self.profile_choosen = self.profile_list[user_choice]

    def delete_user_profile(self):
        """
        Página para apagar um perfil.
        """
        user_choice = self.profile_choice("delete")
        assurance = str(input("Are you sure? Y/N\n").lower())
        if assurance == "y":
            self.profile_list.pop(user_choice)
    
    def create_user_profile(self):
        """
        Página de criação de um perfil.

        :var str first_name: Primeiro nome.
        :var str last_name: Sobrenome.
        :var int age: Idade.
        :var boolean parental_controls: Vê se o controle parental esta ligado ou desligado
        :var str category_preference: Categoria(s) preferida(s).
        :var list genre_preference: Lista de de :type:`str` gêneros preferidos.

        """
        main.clear_screen()
        print("Create a profile!")
        first_name = str(input("First name: "))
        last_name = str(input("Last name: "))
        age = int(input("Your age: "))
        parental_controls = False

        #Prompt do controle parental
        if age < 15:
            while True:
                opt = str(input("Would you like to enable parental controls on this profile? Y/N\n").lower())
                if opt == "y":
                    print("Parental Controls are now enabled.")
                    parental_controls = True
                    break
                elif opt == "n":
                    break
        
        #Prompt da preferência de categorias.
        while True:
            category_preference = str(input("Do you prefer: movies, shows or both? ").lower())

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
                print(f"{genre.title()} | ", end='')
            opt = str(input("\n").lower())

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
        """
        Efetua o prompt e a troca de emails.
        """
        while True:
            new_email = str(input("Enter your new e-mail or type 'out' to cancel"))

            if new_email in user_data:
                input("This email has already been registered. Press enter to try again")
            elif new_email == "out":
                break
            else:
                assurance = str(input(f"Are you sure you want to change {self.email} to {new_email}? Y/N\n").lower())
                if assurance == "y":
                    user_data[new_email] = user_data.pop(self.email)
                    self.email = new_email
                    input("New email successfully registered. Press enter to exit")
                    break
    
    def change_password(self):
        """
        Efetua o prompt e a troca da senha.
        """
        while True:
            password = str(input("Enter your new password or type 'out' to cancel: "))

            if password == "out":
                break
            rpt_password = str(input("Enter your new password again: "))
            if password != rpt_password:
                input("The two passwords are not the same, press enter to try again")
            else:
                self.password = password
                input("Password changed successfully. Press enter to exit")
                break

    def change_payment_plan(self):
        """
        Efetua o prompt e a troca do plano de pagamento
        """
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
    """
    Classe de perfil. Segura informações como prefrências e histórico.

    :var str first_name: Primeiro nome.
    :var str last_name: Sobrenome.
    :var int age: Idade.
    :var str category_preference: Categoria(s) preferida(s).
    :var str list genre_preference: Lista de genêro(s) preferido(s).
    :var bool parental_controls: Vê se os controles parentais estão ligados ou não.
    :var str bandwidth: Qualidade escolhida de banda larga.
    :var :obj:`Watchable` list bookmarks: Itens salvos.
    :var :obj:`Watchable` list watch_history: Itens assistidos.
    """
    def __init__(self, first_name:str, last_name:str, age:int, cat_preference:str, gen_preference:list, parental_controls:bool):
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
        """
        Página de configuração da banda larga.
        """
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
                input(f"Your preferred quality is now {self.bandwidth}. Press enter to continue")
                break
    
    def bookmarks_or_watch_history_page(self, option:str):
        """
        Lista os itens dos itens salvos ou histórico, dependendo de :param:`option`

        :param str option: A página escolhida para ser mostrada, "bookmarks" ou "watch_history". (Provavelmente deveria deixar de usar strings pra isso)
        """
        main.clear_screen()
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

            while True:
                opt = int(input("Enter wich item you want to watch (enter 0 to exit): "))
                if opt in range(0, i):
                    if opt != 0:
                        bm_list[opt - 1].show_details()
                    break

class Catalog:
    """
    Classe de catálogo, armazena os itens de maneira similar a como eles estão em data.py.

    :var str catalog_name: Nome do catálogo (show ou movie)
    :var dict catalog_dict: Dicionário onde será armazenados os itens. Serão armazenados na chave do genêro e suas informações na chave do seu nome.
    """
    def __init__(self, catalog_name:str, item_dict:dict):
        self.catalog_name = catalog_name
        self.catalog_dict = {}

        for genre in genres_list: #Percorre a lista de genêro criando chaves para cada um.
            self.catalog_dict[genre] = {}
        
        for key in item_dict: #Percorre o catálogo em data.py para criar um objeto para cada um e armazenalos em catalog_dict usando o genero como primeira chave e o nome como segunda.
            item = Watchable(key, item_dict[key])
            self.catalog_dict[item.genre][key] = item

    def show_catalog(self, genres, i:int, items:list):
        """
        Imprime o catálogo usando o(s) genêro(s) como parâmetro.

        :param genres: Lista ou string (rever isso daí) de genêros escolhidos.
        :param int i: Iterador para a escolha do item.
        :param int list items: Lista de :obj:`Watchable` a serem salvos para a escolha.
        
        :return: Retorna o iterador :var:`i`
        """
        profile = main.logged_user.profile_choosen
        if isinstance(genres, str): #se 'genre' for uma string, transforma ela em uma lista
            genres = [genres]
        
        print(f"\n\t\t\t{self.catalog_name.title()}")

        for genre_key in genres:

            print(f"\n{genre_key.title()}")

            for item in self.catalog_dict[genre_key]:
                #Filtro do controle parental
                if profile.parental_controls is False or self.catalog_dict[genre_key][item].rating <= profile.age:
                    print(f"{i} - {item} | ", end ='')
                    i += 1
                    items.append(self.catalog_dict[genre_key][item])
            print()
        return i

class Item:
    """
    Usa data.py para criar um item. Feito para ser herdado.
    """
    def __init__(self, name, dictionary):
        self.name = name
        for key in dictionary: 
            setattr(self, key, dictionary[key]) #Como se fosse self.key = dictionary[key]

class Watchable(Item):
    """
    Classe de itens "assistiveis", usa :class:`Item` em herança para escanear os catálogos em data.py.

    A seguir são os itens que **devem** estar no objeto.

    :var str name: Nome do filme/show.
    :var str category: Categoria do item (filme ou show).
    :var str genre: Genêro do item.
    :var str description: Descrição ou sinopse.
    :var str year: Ano de lançamento do item (será que eu devia mudar para int?)
    :var int rating: Classificação indicativa.
    :var dict reviews: Dicionário com dicionários de informações das reviews.
    """
    def watch(self):
        """
        "Assiste" o item e o salva no perfil do usuário.
        """
        profile = main.logged_user.profile_choosen
        if profile.bandwidth == "":
            while True:
                b_w = input("In what quality do you want to watch, 'Low', 'Medium' or 'High'? (We recommend 'High' for your bandwidth)\n").lower()

                if b_w in quality_list:
                    profile.bandwidth = b_w
                    break
                else:
                    input("Error. Press enter to try again")
        
        profile.watch_history.append(self)

        print("\n")
        ads.show_random_ad()
        input(f"You've just watched {self.name} in {profile.bandwidth} quality. Press enter to continue")
    
    def bookmark(self):
        """
        Salva o item em :var:`bookmarks` no perfil.
        """
        main.logged_user.profile_choosen.bookmarks.append(self)
        input(f"{self.name} has just been added to your bookmarks. Press enter to continue.")

    def print_reviews(self):
        """
        Imprime as reviews salvas no dicionário do item e a nota média.
        """
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
        """
        Página para o usuário escrever sua review. Salva ela no dicionário :var:`reviews` do item.
        """
        reviews_dict = self.reviews

        score = int(input(f"What would you rate {self.name} out of 10?\n"))
        review = str(input("Write your review: "))

        reviews_dict[main.logged_user.profile_choosen.first_name] = {
            "score": score,
            "review": review
        }

        input("Your review has been saved. Press enter to continue.")

    def show_details(self):
        """
        Mostra as opções do item, como assistir ou salva-lo.
        """
        while True:
            main.clear_screen()
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
                while True: #Escolha se o usuário vai ver ou fazer uma review.
                    user_choice = int(input("Would you like to:\n1 - Leave a review 2 - See the current score and reviews 3 - Exit\n"))
                    if user_choice == 1:
                        self.review_page()
                    elif user_choice == 2:
                        self.print_reviews()
            else:
                break

class Ad(Item):
    """
    Classe de propagandas, usa :class:`Item` como herança.

    Os dados das propagandas ainda são um W.I.P, porém *no momento* eles **devem** ser assim:

    :var str name: Nome do catálogo (no caso, ad)
    :var dict banner: Dicionário com as informações das propagandas em banner.
    :var dict placement: Dicionário com as informações das propagandas de "lugar" (no catálogo ou comercial no filme/show).
    """
    def show_random_ad(self):
        """
        Pega um banner aleatório para imprimi-lo.
        """
        random_ad_key = random.choice(list(self.banner.keys()))
        print(f"\nProduct placement: {random_ad_key}: {self.banner[random_ad_key]}")


main = Program()
movie_catalog = Catalog("movie", movie_catalog)
shows_catalog = Catalog("show", show_catalog)
ads = Ad("ad", ad)
