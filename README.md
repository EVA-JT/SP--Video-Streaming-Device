# 14. Video Streaming Service

### • Content Library Management: 
Implementada, mostrando o catalógo de filmes e séries com apenas 3 generos no momento.

### • User Subscription Management:
Implementada, é possivel criar, logar e excluir uma conta inscrita, podendo alterar as informações dela também. É possivel gerenciar o plano de pagamento porém de maneira simples e toda conta está no teste gratuito automaticamente.;

### • User Profile Management:
Implementada, é possivel criar, usar e excluir um perfil. As informações armazenadas são apenas o nome, sobrenome e idade.

### • Bookmarking and Watch History:
Implementada, ao "assistir" algo ou salva-lo o objeto do item fica salvo no perfil escolhido pelo usuario e pode ser visto em suas respectivas páginas no menu principal.

### • Personalized Recommendations:
Implementada, na criação de perfil o usuario pode escolher qual categoria e genero(s) são seus preferidos e no menu principal, ao escolher a página de recomendações, itens são impressos baseado nas escolhas feitas na criação. TO DO: Permitir certa modificação das opções, sendo baseadas no histórico ou sendo modificadas nas configurações.;

### • Bandwidth Optimization:
Implementada, ao assistir algo pela primeira vez em um perfil, o usuario pode escolher com que qualidade assistir-lo, podendo escolher entre low, medium e high. Essa escolha pode ser configurada na página de detalhes do item. O programa sempre recomendará high para o usuario.

### • Content Rating and Reviews:
Implementada, os usuarios podem ver e deixar uma review. Essas informações ficarão salvas nas informações do filme.

### • Ad Integration and Management:
Implementada, ads aparecem no catálogo e após assistir algum item.

### • Parental Control Settings:
Implementada, ao criar um perfil e digitar a idade o usuario pod escolher ligar o controle parental, se ligado o catálogo é filtrado a partir da idade do perfil.;

### • Multi-Device Streaming:
A ser implementada posteriormente, por não ser possivel de se fazer no terminal.;


# Classes:

# 1 - Program
Classe principal do programa. Cuida do usuario logado e de certas páginas relacionadas ao catálogo.

`logged_user`: Usuario (`User`) logado no momento.

`system`: Sistema do usuario.

`clear_type`: Qual comando deve ser usado para limpar a tela.

## Métodos
### create_user()
Cria um usuario (`User`) a partir do email, senha e plano de pagamento escolhido.
### user_login()
Pagina de login do usuario. Define o `User` que ficará salvo em `logged_user`.
### user_management()
Página de configurações da conta do usuario. Pode mudar o email, senha, plano de pagamento e até deletar a conta.
### clear_screen()
Limpa a tela usando o comando `clear_type` salvo no objeto.
### choice_catalog(category:str, genres)
Define qual e como um catálogo será imprimido. Ao final dá o prompt de escolha do item para o usuário e chama o `show_details()` do item escolhido.
### genre_page()
Dá um prompt para o usuário escolher um genêro para imprimir todos os catálogos seguindo ele.
### recommendations_page()
Usa as informações do perfil escolhido para imprimir o(s) catálogo(s) seguindo elas e usando `choice_catalog()`.
### category_page()
Dá um prompt para o usuário escolher uma categoria de catálogo para ser impresso.

# 2 -  User:
Classe da conta do usuário. Lida com o perfil escolhido e troca das informações como email e senha.

`email`: Email salvo do usuário

`password`: Senha salva do usuário

`payment_plan`: Plano de pagamento salvo.

`profile_list`: Lista de perfis criados.

`choosen_profile`: Perfil (`Profile`) escolhido.

## Métodos:
### profile_choice(option:str))
Printa os perfis criados, os enumera para a escolha e retorna a escolha do usuário.
### choose_user_profile()
Página de escolha de perfil. Determina o `profile_choosen`.
### delete_user_profile()
Página para apagar um perfil.
### create_user_profile()
Dá os prompts para o usuario criar um perfil com a classe Profile, que ficará salvo na profile_list
### change_email()
Efetua o prompt e a troca de emails.
### change_password()
Efetua o prompt e a troca da senha.
### change_payment_plan()
Efetua o prompt e a troca do plano de pagamento.

# 3 - Profile
Classe de perfil. Segura informações como prefrências e histórico.

`first_name`: Primeiro nome.

`last_name`: Sobrenome.

`age`: Idade.

`category_preference`: Categoria(s) preferida(s).

`genre_preference`: Lista de genêro(s) preferido(s).

`parental_controls`: Vê se os controles parentais estão ligados ou não.

`bandwidth`: Qualidade escolhida de banda larga.

`bookmarks`: Lista de itens salvos.

`watch_history`: Lista de itens assistidos.

## Métodos:
### bandwidth_settings
Página de configuração da banda larga.
### bookmarks_or_watch_history_page(option:str) <- nome a ser mudado
Lista os itens dos itens salvos ou histórico, dependendo de `option`

`option`: A página escolhida para ser mostrada, "bookmarks" ou "watch_history". (Provavelmente deveria deixar de usar strings pra isso)

# 4 - Catalog
Classe de catálogo, armazena os itens de maneira similar a como eles estão em data.py.

`catalog_name`: Nome do catálogo (show ou movie)

`catalog_dict`: Dicionário onde será armazenados os itens. Serão armazenados na chave do genêro e suas informações na chave do seu nome.
## Métodos:
### show_catalog()
Imprime o catálogo usando o(s) genêro(s) como parâmetro.

`genres`: Lista ou string (rever isso aqui) de genêros escolhidos.

`i`: Iterador para a escolha do item.

`items`: Lista de `Watchable` a serem salvos para a escolha.
        
`return`: Retorna o iterador `i`

# 5 - Item
Usa data.py para criar um item. Feito para ser herdado.

# 6 - Watchable
Classe de itens "assistiveis", usa `Item` em herança para escanear os catálogos em data.py.

A seguir são os itens que **devem** estar no objeto.

`name`: Nome do filme/show.

`category`: Categoria do item (filme ou show).

`genre`: Genêro do item.

`description`: Descrição ou sinopse.

`year`: Ano de lançamento do item (será que eu devia mudar para int?)

`rating`: Classificação indicativa.

`reviews`: Dicionário com dicionários de informações das reviews.

## Métodos:
### watch()
"Assiste" o item e o salva no perfil do usuário.
### bookmark()
Salva o item em `bookmarks` no perfil.
### print_reviews()
Imprime as reviews salvas no dicionário do item e a nota média.
### review_page()
Página para o usuário escrever sua review. Salva ela no dicionário `reviews` do item.
### show_details()
Mostra as opções do item, como assistir ou salva-lo e seus detalhes.

# 7 - Ad
Classe de propagandas, usa `Item` como herança.

Os dados das propagandas ainda são um W.I.P, porém *no momento* eles **devem** ser assim:

`name`: Nome do catálogo (no caso, ad)

`banner`: Dicionário com as informações das propagandas em banner.

`placement`: Dicionário com as informações das propagandas de "lugar" (no catálogo ou comercial no filme/show).

## Métodos
### show_random_ad()
Pega um banner aleatório para imprimi-lo.

# 8 - Funções soltas
## login_menu()
Primeiro menu do programa. O usuário pode logar ou criar uma conta aqui.
## initial_menu()
Segundo menu do programa. Aqui o usuário pode criar, escolher ou deletar um perfil e configurar sua conta.
## main_menu()
Terceiro menu do programa. Aqui pode ser escolhido como o usuário ira ver o(s) catálogo(s).

# TO DO:
- Polir e debugar.
- Talvez adicionar uma classe Catalog**s**
