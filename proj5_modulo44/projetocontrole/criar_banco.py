from projcontrole import app, database
from projcontrole.models import Post



#criar o banco e adicionar o usuário
# with app.app_context():
#     database.create_all()
#     usuario = Usuario(usuario='Kaio',email='kaio@gmail.com',senha='123123')
#     database.session.add(usuario)
#     database.session.commit()

#Buscar usuários no banco.

with app.app_context():

    post = Post.query.first()
    print(post.corpo)
    # meu_usuario = Usuario.query.all() # Outras formas: .firt(), .get(), .filter_by(paramentro=valor)
    # print(meu_usuario)
    # print(meu_usuario[0].email)
    #
    # usuario_teste = Usuario.query.filter_by(id=1)
    # print(usuario_teste[0].email)


#criar um post
# with app.app_context():
#     meu_post = Post(id_usuario=1,titulo='primeiro post kaio',corpo='Testando banco de dados')
#     database.session.add(meu_post)
#     database.session.commit()

#Buscar posts
# with app.app_context():
    # meu_post = Post.query.all() # Outras formas: .firt(), .get(), .filter_by(paramentro=valor)
    # print(meu_post)
    # print(meu_post[0].corpo)

    # meu_post = Post.query.first() # Outras formas: .firt(), .get(), .filter_by(paramentro=valor)
    # print(meu_post)
    # print(meu_post.autor.usuario)

#deletar tudo no banco:
# with app.app_context():
#     database.drop_all()
#     database.create_all()