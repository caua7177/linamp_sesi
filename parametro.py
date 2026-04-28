def criar_usuario(nome,idade,admin=False):
    print(f"nome:{nome }, idade:{idade}, admin:{admin}")

nome = input("qual seu nome:")
idade = int(input("Qual a sua idade: "))

criar_usuario(nome,idade,admin=False)

nome2 = input("Qual o seu nome:")
idade2 = int(input("Qual sua idade: "))

criar_usuario(nome2,idade2,admin=True)