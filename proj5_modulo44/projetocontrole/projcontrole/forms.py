from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_login import current_user
from projcontrole.models import Usuario


class FormCriarConta(FlaskForm):
    usuario = StringField("Nome de usuário", validators=[DataRequired()])
    email =  StringField("E-mail", validators=[DataRequired(), Email()])
    senha =  PasswordField("Senha", validators=[DataRequired(),Length(6,20)])
    confirmacao = PasswordField("Confirmação da senha", validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta = SubmitField("Criar Conta")

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, cadastre-se com outro e-mail ou faça login para continuar ")

class FormLogin(FlaskForm):
    email =  StringField("E-mail", validators=[DataRequired(), Email()])
    senha =  PasswordField("Senha", validators=[DataRequired(),Length(6,20)])
    lembrar = BooleanField("Lembrar dados de acesso")
    botao_submit_login = SubmitField("Login")

class FormEditarPerfil(FlaskForm):
    usuario = StringField("Nome de usuário", validators=[DataRequired()])
    email =  StringField("E-mail", validators=[DataRequired(), Email()])
    senha =  PasswordField("Senha", validators=[DataRequired(),Length(6,20)])
    confirmacao = PasswordField("Confirmação da senha", validators=[DataRequired(), EqualTo('senha')])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png'])])
    curso_excel = BooleanField("Cursando excel")
    curso_vba = BooleanField("Cursando vba")
    curso_powerbi = BooleanField("Cursando powerbi")
    curso_python = BooleanField("Cursando python")
    curso_ppt = BooleanField("Cursando powerpoint")
    curso_sql = BooleanField("Cursando sql")
    botao_submit_editarperfil = SubmitField("Confirmar")

    def validate_email(self,email):
        #verificar se ele mudou o email
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("E-mail já cadastrado, registre outro e-mail")


class FormCriarPost(FlaskForm):
    titulo = StringField("Titulo Post", validators=[DataRequired(),Length(2,140)])
    corpo = TextAreaField("Escreva seu post aqui", validators=[DataRequired()])
    botao_submit = SubmitField("Confirmar")