import hashlib

# Definindo a classe Usuario
class Usuario:
    def __init__(self, nome, senha_hash, nivel_acesso):
        self.nome = nome
        self.senha_hash = senha_hash
        self.nivel_acesso = nivel_acesso

# Definindo a classe SistemaDeLogin
class SistemaDeLogin:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
        # Solicitando informações do usuário
        nome = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        nivel_acesso = int(input("Digite o nível de acesso (1, 2, 3, ...): "))

        # Validando o nome do usuário
        if not self.validar_nome(nome):
            return "Nome de usuário inválido."

        # Calculando o hash da senha
        senha_hash = self.calcular_hash(senha)

        # Criando um novo usuário e adicionando-o à lista
        novo_usuario = Usuario(nome, senha_hash, nivel_acesso)
        self.usuarios.append(novo_usuario)
        return "Usuário criado com sucesso."

    def validar_nome(self, nome):
        return nome.isalnum() and not nome.isspace()

    def calcular_hash(self, senha):
        # Calculando o hash da senha usando SHA-256
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        return senha_hash

    def verificar_login(self):
        # Solicitando informações de login
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        nivel_acesso_requerido = int(input("Digite o nível de acesso requerido (1, 2, 3, ...): "))

        for usuario in self.usuarios:
            if usuario.nome == nome:
                # Verificando a senha
                senha_hash_input = self.calcular_hash(senha)
                if usuario.senha_hash == senha_hash_input:
                    # Verificando o nível de acesso
                    if usuario.nivel_acesso >= nivel_acesso_requerido:
                        return "Sua entrada foi permitida."
                    else:
                        return "Seu nível de acesso não permite."
                else:
                    return "Senha incorreta."
        return "Usuário inexistente."

# Criando uma instância do SistemaDeLogin e executando-o
sistema = SistemaDeLogin()
print(sistema.criar_usuario())
print(sistema.verificar_login())
