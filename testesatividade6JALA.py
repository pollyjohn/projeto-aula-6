# Escreva seu código aqui
from faker import Faker
import random

fk = Faker()

class Livro:
     def __init__(self,nome, autor, genero, paginas, resumo) -> None:
          self.nome =  nome
          self.autor = autor
          self.genero = genero
          self.paginas = paginas
          self.resumo = resumo

# Escreva seu código aqui

class Livro:
     def __init__(self,nome, autor, genero, paginas, resumo) -> None:
          self.nome =  nome
          self.autor = autor
          self.genero = genero
          self.paginas = paginas
          self.resumo = resumo

class Livraria:
    def __init__(self, livro = Livro) -> None:
        #generos: drama,ficção,cientifico,autoajuda, 
        self.catalogos = {"seções":{'poesia':[], "drame":[], 'ficcao':[], 'cientifico': [], 'autoajuda':[], 'infantil': [] }}
        self.users = {'users':[]}
        self.livro = livro

    def registrar(self, livro: Livro):
        while True:
            if livro.genero in self.catalogos['seções'].keys():
                self.catalogos['seções'][livro.genero].append(livro)
                print(f"Livro '{livro.nome}' registrado na seção '{livro.genero}'.")
                break
            else:
                print(f"A seção '{livro.genero}', deste livro, não existe. Digite 'L' para ver a lista ed seções")
                secao = input("Deseja criar uma nova seção? (S/N ou L) : ").lower()
                if secao.lower() == 's':
                    self.criar_secao()
                
                elif secao == 'l':
                    self.mostrar_secoes()

    def criar_secao(self):
         # método que permite ao ADM criar novas seções de livros (como por exemplo criar o a subdivisão "country" para livros que antes se encaixavam apenas em "Ação") 
         secao_add = input('informe o nome da nova seção ou pressione X para finalizar: ')
         secao_add = {secao_add:[]}
         self.catalogos['seções'].update(secao_add)

    def mostrar_secoes(self):
         list(map(lambda x: print(x), self.catalogos['seções'].keys()))
    
    def mostrar_cat(self, secao):
        # aplicar lógica para busca de catalogos e respectivos livros dentro atributo catalogos
        # aplicar funcionalidade que mostre caracteristicas do livro
        for i in self.catalogos['seções'].keys():
            print(i.upper())
            list(map(lambda x: print(x), self.catalogos['seções'][i]))
    
    def selecionar(self):
        # funcionalidade para selcionar o livro
             # *** lembrar de aplicar lógica para retirar livro do catalogo
             pass
    
    def devolucao(self):
        ## aplicar lógica retornar livro para catalogo principal
        pass


class Usuario:
    def __init__(self, livraria: Livraria) -> None:
          self.livraria = livraria
          self.livros_alugados = []
    def login(self):
        state = 'deslogado'
        while True:
            username = input('informe seu usuário: ')
            if username in self.livraria.users['users']:
                senha = input('informe sua senha: ')
                print('vc está logado(a)')
                break
            else:
                print('vc não tem uma conta. Vamos criar!')
                self.criar_conta()    
#               opcoes = input('''o que deseja fazer agora: 1. mostrar catalogo
#                                                    2. mostrar generos
#                                                    3. selecionar livro
#                                                    4. devolver livro''')
#        return opcoes
    def criar_conta(self):
        usuario = 'inexistente'
        while usuario == 'inexistente':
            username = input('informe seu usuario')
            self.livraria.users['users'].append(username)
            senha = input('informe sua senha')
            print(self.livraria.users['users'])
            break
class ADM:
    def __init__(self) -> None:
        self.livraria = Livraria
        
        def __getattr__(self, nome):
            if nome in ['registrar','criar_secao','mostrar_secoes','mostrar_cat','selecionar','devolucao']:
                return getattr(self, nome)
        
          

liv_mundo_mag = Livraria()

#Inserindo livros já existentes na biblioteca
for i in liv_mundo_mag.catalogos['seções'].values():
    words = fk.words()
    i.append(f"The {random.choice(words)} {fk.name()} {fk.city()}")

# instanciando usuário
usuarioGab = Usuario(liv_mundo_mag)
livro1 = Livro("livro da vida",'vc mesmo', 'poesia','int(dias vivo)', 'erros e acertos')


usuarioGab.login()

usuarioGab.livraria.registrar(livro1)

livro2 = Livro("livro de teste",'testaldo', 'sci-fi',3, 'resumo')

usuarioGab.livraria.registrar(livro2)