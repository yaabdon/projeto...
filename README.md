ALUNA: YASMIN SOUSA ABDON
MATRÍCULA: 232014271

Visual Novel - Projeto em Python

Este projeto é uma visual novel desenvolvida em Python com um sistema de personalização de personagem e escolhas interativas.

Como executar o projeto

Siga os passos abaixo para configurar e executar o projeto corretamente:

1. Clone o repositório

# Clone este repositório no seu computador

```
$ git clone https://github.com/yaabdon/projeto_livre_turma3.git
```

# Acesse o diretório do projeto
```
$ cd projeto_livre_turma3
```

2. Crie e ative um ambiente virtual

# Crie um ambiente virtual chamado venv
```
$ python -m venv venv
```

# Ative o ambiente virtual:
# No Windows:
```
$ venv\Scripts\activate
```

# No MacOS/Linux:
```
$ source venv/bin/activate
```

3. Instale as dependências

# Instale os pacotes listados no arquivo requirements.txt
```
$ pip install -r requirements.txt
```

4. Execute o projeto

# Inicie o jogo executando o arquivo main.py
```
$ python main.py
```

Observação

Certifique-se de estar utilizando uma versão do Python compatível com o projeto (recomendado Python 3.8 ou superior).

O arquivo original se chama "Project_00_2024":										
-------------------------------

-> project_00_2024:
	
 	código: main

	pasta: packages

	pasta: shapes

	pasta: assets

	pasta: venv


-> packages:
	
	__init__.py
 
	pasta: models -> cena.py, dialogo.py, episodio.py, escolha.py, usuario.py
 
	pasta: controllers -> controller_episodio.py, controller_personagens.py, menu.py, tutorial.py
 
	pasta: data -> usuarios.json, pasta: episodios -> episodios.json e pasta: personanges -> personagens.json e personagens.py

  
-> shapes:

	__init__.py
 
	pasta: viewers -> decorando_terminal.py

 	
-> assets:

	__init__.py
 
	pasta: sounds -> audio.py, efeito_som.wav, musica_fundo.mp3
 	

O CODIGO É SOBRE UM JOGO DE VISUAL NOVEL CHAMADO "CONTOS EM BRANCO":
--------------
Tanto menu.py quanto controller_episodios.py são os códigos com as que apresentam o maior comando de controle do jogo,
enquanto em MENU conseguimos navegar por todo o jogo, em CONTROLLER_EPISODIO iniciamos a parte principal do jogo que é o episodio a ser jogado

Quando aberto o terminal: O usuario deve receber uma mensagem de boas-vindas, logo depois escolher entre as opcoes de login (models - usuario.py),
se já estiver logado, um arquivo json com seus dados homologa o acesso a conta e em seguida é apresentado o menu para o usuario,
se não estiver logado, vai ter uma opção de inscrição.

Ao chegar na página do menu, o usuario vai poder escolher entre 4 opcoes: 1.ler o pequeno tutorial, 2.jogar diretamente os episodios disponiveis
da historia, 3.ler sobre os personagens disponiveis e 4.sair 

