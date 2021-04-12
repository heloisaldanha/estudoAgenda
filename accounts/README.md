 # ANOTAÇÕES APP ACCOUNTS  

 
> ## **ARQUIVO views.py:** 

### _**(1) - É importante que o app de contas de usuários receba o nome de "accounts".**_
Eu tinha colocado "contas" e ficou dando um erro de caminho na parte do dashboard, que teria que redirecionar pra página de login, caso o login não tivesse sido feito.
O erro:


_Page not found (404)_
_Request Method: 	GET_
_Request URL: 	http://127.0.0.1:8000/accounts/login/?login=/contas/dashboard_

_Using the URLconf defined in AGENDA.urls, Django tried these URL patterns, in this order:_

    admin/
    contas/
    [name='index']
    busca/ [name='busca']
    <int:contato_id> [name='detalhes']
    ^media/(?P<path>.*)$

_The current path, accounts/login/, didn't match any of these._

**Depois de renomear o app para accounts e seus caminhos, o dashboard sem logar, foi sim para a página de login**

Não consegui descobrir como alterar o nome de accounts para contas para não dar erro sem precisar mudar de nome (na raiz do projeto).
