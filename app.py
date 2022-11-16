from flask import Flask, render_template

app = Flask("Olá mundo")

@app.route("/") # Rota Principal
def hello():
    return "Olá mundo"


@app.route("/nome") # Rota nome
def nome():
    return ("Marcos Vinicius")


@app.route("/sobrenome") # Rota sobrenome
def sobrenome():
    return ("Novais Santos")


@app.route("/alunas") # Rota alunas
def alunas():
    return render_template("alunas.html")


@app.route("/alunos") # Rota alunos
def alunos():
    return render_template("hello.html")