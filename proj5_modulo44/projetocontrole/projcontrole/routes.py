from flask import render_template, flash, redirect, url_for, request, abort
from projcontrole import app, database, bcrypt
from projcontrole.forms import FormCriarConta, FormLogin,FormEditarPerfil,FormCriarPost
from projcontrole.models import Usuario, Post
from flask_login import  login_user,logout_user, current_user, login_required
from PIL import Image
import secrets
import os




@app.route("/")
def home():
    Posts = Post.query.order_by(Post.id.desc())
    return render_template('home.html',posts=Posts)

@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route("/login", methods=["POST","GET"])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha,form_login.senha.data):
            #Chamada para login e o remember é usado pra dar função ao flag de lembrar na tela de login.
            login_user(usuario,remember=form_login.lembrar.data)
            flash(f"login feito com sucesso no e-mail: {form_login.email.data}",'alert-success')
            part_next = request.args.get('next')
            if part_next:
                return redirect(part_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f"Falha no login. Email ou senha incorretos, tente novamente ou crie uma conta!", 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(usuario=form_criarconta.usuario.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f"Conta criada com sucesso para o e-mail:  {form_criarconta.email.data}",'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f"Logout feito com sucesso!", 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static',filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html',foto_perfil=foto_perfil)

@app.route('/post/criar',methods=["POST","GET"])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash(f"Post criado com sucesso", 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarpost.html',form=form)

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome,extensao = os.path.splitext(imagem.filename)
    #nome_completo = os.path.join(nome,codigo,extensao) #por algum motivo ele não usou esse comando, apenas juntou as variaveis.
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path,'static/fotos_perfil',nome_arquivo)
    tamanho = (200,200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return  nome_arquivo
    # Add um codigo aleatorio, reduzir tamanho, salvar imagem na pasta e mudar o campo foto_perfil no banco

def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if "curso_" in campo.name and campo.data:
            lista_cursos.append(campo.label.text)
    return ";".join(lista_cursos)



@app.route('/perfil/editar',methods=["POST","GET"])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form.senha.data)
        current_user.email = form.email.data
        current_user.usuario = form.usuario.data
        current_user.senha = senha_cript
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash(f"Perfil atualizado com sucesso",'alert-success')
        return redirect(url_for('perfil'))
    #usado para quando o metodo for get (carregar dados) já carregar o formulario preenchido
    elif request.method == "GET":
        form.usuario.data = current_user.usuario
        form.email.data = current_user.email
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html',foto_perfil=foto_perfil,form=form)

@app.route('/post/<post_id>',methods=["POST","GET"])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        form = FormCriarPost()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash(f"Post atualizado com sucesso",'alert-success')
            return redirect(url_for('home'))
        #Criar logica de editar post
    else:
        form = None
    return render_template('post.html',post=post,form=form)


@app.route('/post/<post_id>/excluir',methods=["POST","GET"])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash("Registro excluído com sucesso",'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)