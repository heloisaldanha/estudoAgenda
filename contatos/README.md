 #ANOTAÇÕES APP CONTATOS  

 
> ##**ARQUIVO models.py:** 

### _**(1) - blank = true significa que ele pode ser vazio**_

-> Qual a diferença entre null e blank? -> https://docs.djangoproject.com/en/2.2/ref/models/fields/

Note que blank é diferente de null. null é especificamente relacionado ao banco de dados, enquanto o blank é relacionado à validação. Se um campo tiver blank=True, a validação de um formulário permitirá a entrada de um valor vazio. Se o campo tiver blank=False, então o campo será obrigatório.

### _**(2) - ao ser deletado algo da categoria, não faça nada com os atributos de Contato**_

### _**(3) - A classe Categoria tem que vir antes da classe contato porque ela é usada em um atributo.**_

Eu tinha colocado no final e deu o erro: NameError: name 'Categoria' is not defined.

### _**(4) - Se precisar alterar algo no model, vai ter que fazer o makemigrations e o migrate novamente**_


###_**(5) - Quando se cria os grupos lá no django admin, na aplicação rodando, geralmente não aparece os nomes, mas sim "Categoria object (1)(2)(3)...". Fica ruim de saber qual a classificação foi dada, logo, essa função transforma o nome da categoria e aparece lá com o nome que foi dado. Mudar representação de classe (lembrar POO).**_


###_**(6) - Esse upload_to é pra onde vai a imagem, que no caso é pasta fotos. Esse %Y/%m/%d é para cada imagem adicionada, vai criando uma página para dia do mês que foi adicionada aquela imagem. É mais por questão de organização.**_
Pode organizar só por ano: %Y

Por ano e mês: %Y/%m

e por ano, mês e dia: %Y/%m/%d
___


> ##**ARQUIVO admin.py:**

###_**(1) - Esse .models é pra importar o model DA PASTA em que SE ENCONTRA o admin, pois é referente aquele app.**_

###_**(2) - Para mostrar mais campos dos contatos no admin, deve-se criar uma classe.**_

O admin.ModelAdmin quem faz essa mostra.
___

> ##**ARQUIVO urls.py:**

###_**(1) - Esse int é pra dizer qual o tipo do dado que vai utilizar pra entrar na urls, que, nesse caso, é o id, que é um int. Seguido do dado, que é o id do contato. Tudo isso entre <>.**_
___


> ##**ARQUIVO views.py:**

###_**(1) - Raise tem como finalidade invocar uma Exception no momento oportuno. Da mesma forma que as outras linguagens quando usamos o throw new Exception , a exceção é invocado no momento que chamarmos raise . ... O raise é o mecanismo responsável exatamente pelo chamamento de uma exceção, independente da condição.**_

###_**(2) - Quando tava filtrando pelo if diretamente no html, quando ocultava algum contato no admin, diminuía um contato da página.**_
Por exemplo, se ocultasse o contato "Léia", ao invés de continuar aparecendo 5 na página, só aparecia 4. Fazendo o filtro diretamente no views, mesmo ocultando, agora sim aparece os 5.

###_**(3) - campos = Concat('nome', Value(' '), 'sobrenome')**_
Essa variável campos vai servir pra concatenar os campos 'nome' e 'sobrenome' que já estão no banco de dados. Mas entre o nome e sobrenome tem um espaço. Se colocasse:

`campos = Concat('nome', ' ', 'sobrenome')`

Daria erro porque não existe o campo ' ' no model. Então o Value(' ') simula um campo existente na base de dados. Creio que se quisesse colocar o telefone junto ou qualquer outro campo, seria o mesmo raciocínio.

`campos = Concat('nome', Value(' '), 'sobrenome', Value(' '), 'telefone')`

###_**(4) - Esse annotate vai criar uma variável que guarda a concatenação dos campos para filtrar por essa variável o termo parcial ou total, escrito no formulário.

`contatos = Contato.objects.annotate(
    nome_completo=campos
).filter(
    nome_completo__icontains=termo
)`
