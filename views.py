#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
from metodos import metodo_login
from models import Usuario
import mysql.connector

from datetime import date, datetime


app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="academia_onedera"
    )
    
db = banco.cursor()



login_usuario = metodo_login.UsuarioDao(db)

data_atual = date.today()

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS ADMINISTRADOR       ######################


@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)



@app.route('/deashboard')
def deashboard():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('deash_usuario')))
     return render_template('deashboard.html')
    

@app.route('/calendario')
def calendario():
     return render_template('calendario.html')


@app.route('/relatorio_evento')
def relatorio_evento():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('deash_usuario')))
     return render_template('relatorio_evento.html')  
   
#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO ##########################################

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usuario.buscar_por_id(request.form['email_usuario'])
    password = request.form['senha_usuario']
    password_app = hashlib.md5(password.encode())
    senha_aplicacao = password_app.hexdigest()
    if usuario:
        if usuario.senha_aplicacao == senha_aplicacao:
                session['usuario_logado'] = usuario.email_usuario
                flash('Administrador(a)  ' + usuario.nome_usuario + ' logado!')
                proxima_pagina = url_for('deashboard')
                return redirect(proxima_pagina)
        else:
            flash('Senha invalida, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Usuario não encontrado!')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Deslogado com sucesso!')
    return redirect(url_for('login'))

#################################### ^^^^^^^^^^^^^^^^^^ ####################################





 

app.run(debug=True)


