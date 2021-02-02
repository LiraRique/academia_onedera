from models import  Usuario

SQL_USUARIO_POR_ID = """SELECT * from Usuario where email_usuario= %s"""




class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_login(dados) if dados else None
        return usuario


def traduz_login(tupla):
    return Usuario(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])




