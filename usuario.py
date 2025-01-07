import json
import os
from packages.models.episodio import Episodio
from shapes.viewers.decorando_terminal import DecorandoTerminal

class Usuario:
    def __init__(self, nome_usuario, senha, email=None, episodios=None):
        if episodios is None:
            episodios = []  # Inicializando com uma lista vazia
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.email = email
        self.episodios = [Episodio(**episodio) for episodio in episodios]
        

    def __str__(self):
        return f"Usuário: {self.nome_usuario}"

    @staticmethod
    def verificar_usuario(nome_usuario):
        arquivo_usuario = 'packages/data/usuarios.json'

        if not os.path.exists(arquivo_usuario):
            return False

        with open(arquivo_usuario, 'r') as file:
            usuarios = json.load(file)
            return any(usuario['nome_usuario'] == nome_usuario for usuario in usuarios)

    @staticmethod
    def criar_conta():
        nome_usuario = input("Escolha seu nome de usuário: ")
        if Usuario.verificar_usuario(nome_usuario):
            print("Este nome de usuário já existe. Tente outro.")
            return None

        senha = input("Crie uma senha: ")
        confirmar_senha = input("Confirme sua senha: ")

        if senha != confirmar_senha:
            print("As senhas não coincidem. Tente novamente.")
            return None

        email = input("Digite seu email: ")
        novo_usuario = Usuario(nome_usuario, senha, email)

        arquivo_usuario = 'packages/data/usuarios.json'
        if not os.path.exists(arquivo_usuario):
            with open(arquivo_usuario, 'w') as file:
                json.dump([], file)

        with open(arquivo_usuario, 'r+') as file:
            usuarios = json.load(file)
            usuarios.append({
                'nome_usuario': nome_usuario,
                'senha': senha,
                'email': email,
                'episodios': []  # Inicializa a lista de episódios
            })
            file.seek(0)
            json.dump(usuarios, file, indent=4)

        print(f"Conta criada com sucesso!")
        DecorandoTerminal.limpar_terminal()
        return novo_usuario

    @staticmethod
    def login():
        nome_usuario = input("Digite seu nome de usuário: ")
        if not Usuario.verificar_usuario(nome_usuario):
            print("Usuário não encontrado. Crie uma conta primeiro.")
            return None

        senha = input("Digite sua senha: ")
        arquivo_usuario = 'packages/data/usuarios.json'

        with open(arquivo_usuario, 'r') as file:
            usuarios = json.load(file)
            for usuario in usuarios:
                if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
                    print(f"Bem-vindo de volta, {nome_usuario}!")
                    DecorandoTerminal.limpar_terminal()
                    episodios = usuario.get('episodios', [])
                    episodios_objetos = [Episodio(**episodio) for episodio in episodios]
                    return Usuario(nome_usuario, senha, usuario['email'], episodios_objetos)

        print("Senha incorreta. Tente novamente.")
        return None

    def salvar_episodios(self):
        arquivo_usuario = 'packages/data/usuarios.json'

        if os.path.exists(arquivo_usuario):
            with open(arquivo_usuario, 'r') as file:
                usuarios = json.load(file)

            for usuario in usuarios:
                if usuario['nome_usuario'] == self.nome_usuario:
                    usuario['episodios'] = [{'numero': e.numero, 'nome': e.nome} for e in self.episodios]

            with open(arquivo_usuario, 'w') as file:
                json.dump(usuarios, file, indent=4)
