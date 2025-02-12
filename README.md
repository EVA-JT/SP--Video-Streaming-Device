# Classes:

# 1 - Program
Classe principal do programa, guarda o usuario logado nas informações.
## Métodos
### create_user
Dá os prompts para o usuario criar uma conta, e a salva em user_data (variavel global)
### user_login
Dá os promps para o usuario logar, se ele conseguir o user fica salvo em logged_user.
### user_management
Uma pagina de configurações da conta do usuario, usa métodos de User_Account para mudar as informações da conta.

# 2 -  User:
Cria a conta principal do usuario, armazenando senha, email, plano de pagamento e as informações de perfis que serão adicionadas depois
## Métodos:
### print_user_profile
Imprime todos os perfis associados com a conta do usuario
### choose_user_profile
Usa a print_user_profile para mostrar os perfis ao usuario e o permitir escolher qual ele quer usar, o escolhido ficara em profile_choosen.
### delete_user_profile
Usa o print_user_profile para mostrar os perfis ao usuario e o permitir escolher qual ele quer deletar.
### create_user_profile
Dá os prompts para o usuario criar um perfil com a classe Profile, que ficará salvo na profile_list
### change_email
Dá o prompt para a troca do email nas informações
### change_password
Dá o prompt para a troca da senha nas informações
### change_payment_plan
Dá o prompt para a troca da senha nas informações.

# 3 - Profile
Cria um perfil para uma conta do usuario, armazenando informações como nome, idade, preferencias e etc.
