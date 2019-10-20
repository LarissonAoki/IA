from experta import *
from random import choice
from random import randint

class Guerreiro(Fact):
    """Informações do Guerreiro"""
    pass

class Vilao(Fact):
    """Informcações do Vilao"""
    pass

class Atacar(Fact):
    """Iformações se devo atacar"""
    pass

class DevoAtacar(KnowledgeEngine):
    
    #Regras do Ataque
    @Rule (AND(Atacar(level="sim"), Atacar(dano="sim")))
    def ataquePerfeito(self):
        print("Devo Atacar")

    @Rule(AND(AND(Atacar(level="sim"), Atacar(dano="não")), Atacar(poder="sim")))
    def ataque1(self):
        print("Devo Atacar")

    @Rule(AND(AND(Atacar(level="sim"), Atacar(dano="não")), Atacar(poder="não")))
    def naoataque1(self):
        print("Não Devo Atacar")

    @Rule(AND(AND(Atacar(level="não"), Atacar(dano="sim")), Atacar(poder="sim")))
    def ataque2(self):
        print("Devo Atacar")

    @Rule(AND(AND(Atacar(level="não"), Atacar(dano="sim")), Atacar(poder="não")))
    def naoataque2(self):
        print("Não Devo Atacar")

    @Rule(AND(Atacar(level="não"), Atacar(dano="não")))
    def naoataquePerfeito(self):
        print("Não Devo Atacar")
        
        
    #Regras dos Poderes do Guerreiro
    @Rule(AND(Guerreiro(poder ="fogo")) , Vilao(poder = "agua"))
    def fogoagua(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="fogo")) , Vilao(poder = "terra"))
    def fogoterra(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="terra")) , Vilao(poder = "ar"))
    def terraar(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="terra")) , Vilao(poder = "agua"))
    def terraagua(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="agua")) , Vilao(poder = "ar"))
    def fogoagua(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="ar")) , Vilao(poder = "fogo"))
    def ar_fogo(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="agua")) , Vilao(poder = "agua"))
    def agua_agua(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="fogo")) , Vilao(poder = "fogo"))
    def fogo_fogo(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="terra")) , Vilao(poder = "terra"))
    def terra_terra(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))
    @Rule(AND(Guerreiro(poder ="ar")) , Vilao(poder = "ar"))
    def ar_ar(self):
        print("Poder Valido")
        engine.declare(Atacar(poder = "sim"))

    #Regras dos Poderes do Vilao
    @Rule(AND(Guerreiro(poder ="agua")) , Vilao(poder = "fogo"))
    def agua_fogo(self):
        print("Poder Invalido")
        engine.declare(Atacar(poder = "não"))
    @Rule(AND(Guerreiro(poder ="terra")) , Vilao(poder = "fogo"))
    def terra_fogo(self):
        print("Poder Inalido")
        engine.declare(Atacar(poder = "não"))
    @Rule(AND(Guerreiro(poder ="ar")) , Vilao(poder = "terra"))
    def ar_terra(self):
        print("Poder Invalido")
        engine.declare(Atacar(poder = "não"))
    @Rule(AND(Guerreiro(poder ="agua")) , Vilao(poder = "terra"))
    def agua_terra(self):
        print("Poder Inalido")
        engine.declare(Atacar(poder = "não"))
    @Rule(AND(Guerreiro(poder ="ar")) , Vilao(poder = "agua"))
    def ar_agua(self):
        print("Poder Inalido")
        engine.declare(Atacar(poder = "não"))
    @Rule(AND(Guerreiro(poder ="fogo")) , Vilao(poder = "ar"))
    def fogo_ar(self):
        print("Poder Invalido")
        engine.declare(Atacar(poder = "não"))

          


#definir level
def retornar_level(g, v):
    glvel = int(g)
    vlevel = int(v)
    if(glvel >= vlevel):
        level = "sim"
    else:
        level = "não"
    print("level: ", level)
    return level

#definir dano
def definir_dano(level, tipo):
    poder = {"agua":10, "fogo":40, "terra":30, "ar":20}
    dano = poder[tipo] * level
    return dano

def retornar_dano(vHP, gdano):
    if(gdano > vHp):
        dano = "sim"
    else:
        dano = "não"
    print("dano: ", dano)
    return dano

#criando variaveis do Guerreiro
gHp = randint(100,300)
gpoder = choice(["fogo", "agua", "terra", "ar"])
glvel = randint(2, 6)
gdano = definir_dano(glvel, gpoder)

#criando variaveis do Vilao
vHp = randint(100,300)
vpoder = choice(["fogo", "agua", "terra", "ar"])
vlvel = randint(2, 6)
vdano = definir_dano(vlvel, vpoder)

#Personagens
def personagem(hp, dano, poder, level):
    print(" HP: ", hp)
    print(" Dano: ", dano)
    print(" Poder: ", poder)
    print(" Level: ", level)

print("\nGuerreiro")
personagem(gHp, gdano, gpoder, glvel)
print("\nVilao")
personagem(vHp, vdano, vpoder, vlvel)
print()

engine = DevoAtacar()
engine.reset()

engine.declare(Guerreiro(poder = gpoder))
#engine.declare(Guerreiro(hp = gHp))
#engine.declare(Guerreiro(level = glvel))
#engine.declare(Guerreiro(dano = gdano))

engine.declare(Vilao(poder = vpoder))
#engine.declare(Vilao(hp = vHp))
#engine.declare(Vilao(level = vlvel))
#engine.declare(Vilao(dano = vdano))

engine.declare(Atacar(level = retornar_level(glvel, vlvel)))
engine.declare(Atacar(dano=retornar_dano(vHp, gdano)))

engine.run()










    
