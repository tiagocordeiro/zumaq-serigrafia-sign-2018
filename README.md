# zumaq-serigrafia-sign-2018
Projeto simples para cadastro de visitantes durante a Serigrafia Sign 2018

## Rodando localmente

### Clonando o repo
```console
foo@bar:~$ git clone https://github.com/tiagocordeiro/zumaq-serigrafia-sign-2018.git
```

### Acesse a pasta do projeto e crie um ambiente de desenvolvimento.
```console
foo@bar:~$ cd zumaq-serigrafia-sign-2018
foo@bar:~/zumaq-serigrafia-sign-2018 $ python3 -m venv venv
```

### Ativando o ambiente e instalando as dependências
```console
foo@bar:~/zumaq-serigrafia-sign-2018 $ source venv/bin/activate
(venv) foo@bar:~/zumaq-serigrafia-sign-2018 $ pip install -r requirements.txt
```

### Criando o banco de dados
```console
(venv) foo@bar:~/zumaq-serigrafia-sign-2018 $ python manage.py migrate
```

### Pronto, basta rodar o projeto e abrir o endereço no seu navegador (http://127.0.0.1:8000/)
```console
(venv) foo@bar:~/zumaq-serigrafia-sign-2018 $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 23, 2018 - 22:36:44
Django version 2.0.7, using settings 'zumaqleads.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Sorteio
Talvez você queira realizar um sorteio entre os cadastrados.
Para isso, acesse a url: http://127.0.0.1:8000/sorteio/
e clique em sortear.

É isso.


#### Criando um administrador para o Django Admin
```console
(venv) foo@bar:~/zumaq-serigrafia-sign-2018 $ python manage.py createsuperuser
```
Para acessar o django-admin a url: http://127.0.0.1:8000/admin/
