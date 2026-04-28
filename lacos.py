def criar_perfil(nome,idade,admin=False):
    print(f"nome:{nome }, idade:{idade}, admin:{admin}")

    criar_perfil(cidade="Curitiba",nome="Cauã",idade=18)

def somar_tudo(*numeros):
    return sum(numeros)

somar_tudo(1,2)
somar_tudo(1,2,3,4)
somar_tudo(1,2,3,4,5,6)
