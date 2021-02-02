
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="academia_onedera"
    )




mycursor = banco.cursor()


#mycursor.execute("DROP DATABASE ")

#mycursor.execute("CREATE DATABASE academia_onedera")



mycursor.execute("CREATE TABLE Usuario(id_usuario smallint NOT NULL AUTO_INCREMENT, nome_usuario VARCHAR(40), email_usuario VARCHAR(40), dt_cadastro DATE, senha_aplicacao VARCHAR(500), CONSTRAINT pkcod_usuario PRIMARY KEY (id_usuario), CONSTRAINT uq_email_usuario  UNIQUE (email_usuario))")




mycursor.execute("INSERT INTO Usuario(nome_usuario,email_usuario,senha_aplicacao) VALUES ('ADMINISTRADOR','administrador@administrador.com','91f5167c34c400758115c2a6826ec2e3')")

banco.commit()