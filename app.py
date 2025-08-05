from flask import Flask
from flask import render_template
from flask import request

app= Flask(__name__)

from utils import conectarBD

@app.route("/")
def inicio():
    return render_template("form.html")


@app.route("/envioFormulario", methods=["POST"])
def envio():
    n = request.form.get('nome')
    c = request.form.get('cidade')
    dn = request.form.get('nascimento')

    if n=='':
        n = None
    if c =='':
        c = None
    if dn=='':
        dn = None
    
    #codigo do mysql

    cnx = conectarBD()

    cursor = cnx.cursor()

    sql = "INSERT INTO pessoa(nome, cidade, nascimento) VALUES (%s, %s, %s)"
    dados = (n, c, dn) #os dados que são pegos com o GET 

    cursor.execute(sql, dados)
    cnx.commit()

    cnx.close() #fecho a conexão

    return render_template('sucesso.html')


@app.route('/remover')
def remove():
    return render_template("formRemover.html")


@app.route('/formRemover', methods=["POST"])
def remover():
    n = request.form.get('nome')
    dados = (n,)

    cnx = conectarBD()

    cursor = cnx.cursor()
    sql = "DELETE from pessoa\
        WHERE nome = %s"  #nessa linha de codigo, nome é a coluna
    

    cursor.execute(sql, dados)
    cnx.commit()
    
    cnx.close()
    return render_template('sucesso.html')

