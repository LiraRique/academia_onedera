class Usuario:
    def __init__(self, nome_usuario, email_usuario, dt_cadastro, senha_aplicacao,  id_usuario=None):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.dt_cadastro = dt_cadastro
        self.senha_aplicacao = senha_aplicacao