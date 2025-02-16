# Classes:

# 1 - Program
Classe principal do programa, guarda o usuario logado nas informações.
## Métodos
### create_user()
Dá os prompts para o usuario criar uma conta, e a salva em user_data (variavel global)
### user_login()
Dá os promps para o usuario logar, se ele conseguir o user fica salvo em logged_user.
### user_management()
Uma pagina de configurações da conta do usuario, usa métodos de User_Account para mudar as informações da conta.

# 2 -  User:
Cria a conta principal do usuario, armazenando senha, email, plano de pagamento e as informações de perfis que serão adicionadas depois
## Métodos:
### profile_choice()
Imprime todos os perfis associados com a conta do usuario e dá o prompt para a escolha, usando o parâmetro ele ou usa o perfil ou o deleta.
### choose_user_profile()
Usa a print_user_profile para mostrar os perfis ao usuario e o permitir escolher qual ele quer usar, o escolhido ficara em profile_choosen.
### delete_user_profile()
Usa o print_user_profile para mostrar os perfis ao usuario e o permitir escolher qual ele quer deletar.
### create_user_profile()
Dá os prompts para o usuario criar um perfil com a classe Profile, que ficará salvo na profile_list
### change_email()
Dá o prompt para a troca do email nas informações
### change_password()
Dá o prompt para a troca da senha nas informações
### change_payment_plan()
Dá o prompt para a troca da senha nas informações.

# 3 - Profile
Cria um perfil para uma conta do usuario, armazenando informações como nome, idade, preferencias e etc.
## Métodos:
### bandwidth_settings
Faz a troca da qualidade da banda larga do usuário
### bookmarks_or_watch_history_page (nome a ser mudado)
Tem como parametro 'options' para mostrar ou os itens salvos ou o histórico

# 4 - Catalog
Usado para criar um catalogo de filmes e de séries, usando os dicionarios de new_data.
## Métodos:
### show_catalog()
Imprime o catálogo seguindo o argumento genre para o(s) gênero(s) escolhido.

# 5 - Item
Cria um objeto a partir de um dicionario, as chaves serão o nome da informação (self.key = dictionary[key]). É usado na criação de objetos para o catálogo.

# 6 - Watchable
Cria um objeto para algo "assistivel" usando a herança da classe Item.
## Métodos:
### watch()
Permite o usuario "assistir" o item. Se ele não tiver uma escolha de qualidade, ele poderá escolher também.
### bookmark()
Salva o item no perfil escolhido.
### print_reviews()
Imprime as reviews salvas no item e mostra a média de notas dadas.
### review_page()
Permite o usuario escrever uma review para o item e dar uma nota. Cria um dicionario com as duas informações (usando o nome do perfil como chave) e salva no item.
### show_details()
Imprime o titulo, descrição, ano de lançamento e classificação indicativa do item e dá a escolha para o usuario assistir, salvar, configurar a qualidade e ver se quer olhar ou escrever uma review.

# 7 - Ad
Classe de propaganda usando herança da classe Item
## Métodos
### show_random_ad()
Escolhe uma propaganda aleatória (somente dos banners) e imprime entre as categorias do catalogo.

# 8 - Funções soltas
## choice_catalog()
Chama o show_catalog() do(s) catalogo(s) especificado(s) por category.
## recommendations_page()
Puxa as informações do perfil de categoria e gênero escolhido para mandar para show_catalog().
## category_page()
Pede para o usuario a categoria para show_catalog()
## genre_page()
Pede para o usuario o gênero para show_catalog()
## login_menu()
Menu de criação e login de usuario.
## initial_menu()
Menu de criação, configuração e uso de perfil.
## main_menu()
Menu para o usuario escolher qual catálogo.

# TO DO:
- Polir e debugar.
