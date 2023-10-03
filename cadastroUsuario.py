from datetime import datetime

input("--------IDENTIFICAÇÃO--------\n")
identificacao()

input("\n--------ENDEREÇO--------\n")
endereco()

def identificacao():
    while True:
        name = input("Nome: ")
        if len(name) > 3:
            print("Nome válido!\n")
            break
        else:
            print("Nome deve ter mais de 3 caracteres.\n")

    while True:
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
            print("Data de nascimento válida:", data_nascimento)
            break
        except ValueError:
            print("Data de nascimento inválida. Certifique-se de usar o formato dd/mm/aaaa.")
    
    while True:
        titulo = int(input("Titulo de eleitor: "))
        if salario == 12:
            print("Titulo de eleitor válido!\n")
            break
        else:
            print("Titulo de eleitor invalido.\n")
    
    while True:
        sx = input("Digite seu Sexo (f/m): ")
        if sx == 'f' or sx == 'm':
            print("Sexo válido!\n")
            break
        else:
            print("Sexo deve ser 'f' ou 'm'.\n")
    
    while True:
        naturalidade = input("Naturalidade: ")
        if len(naturalidade)>2:
            print("Naturalidade válido!\n")
            break
        else:
            print("Naturalidade invalida.\n")
            
    while True:
        nome_mae = input("Nome da mãe: ")
        if len(naturalidade)>3:
            print("nome da mãe válido!\n")
            break
        else:
            print("nome da mae invalida.\n")


#########################################################################

def endereco():
    while True:
        cep = input("CEP: ")
        if len(name) == 8:
            print("CEP valido!\n")
            break
        else:
            print("CEP invalido.\n")

    while True:
         municipio = input("municipio: ")
        if len(municipio) > 2:
            print("municipio valido!\n")
            break
        else:
            print("municipio invalido.\n")
    
    while True:
        uf = input("UF: ")
        if len(uf) == 2:
            print("UF válido!\n")
            break
        else:
            print("UF invalido.\n")
    
    while True:
        logradouro = input("logradouro: ")
        if len(logradouro) > 2:
            print("logradouro válido!\n")
            break
        else:
            print("logradouro invalido.\n")
    
    while True:
        endereco = input("Endereco: ")
        if len(endereco)>5:
            print("Endereco válido!\n")
            break
        else:
            print("Endereco invalida.\n")
            
    while True:
        numero_residencia = int(input("Numero da residencia: "))
        if len(numero_residencia)>0:
            print("Numero de residencia Valido!\n")
            break
        else:
            print("Numero de residencia invalido.\n")
            
     while True:
        ddd = int(input("DDD: "))
        if len(numero)==3:
            print("DDD Valido!\n")
            break
        else:
            print("DDD invalido.\n")
    
     while True:
        numero_telefone = int(input("Numero Telefone: "))
        if len(numero)==9:
            print("Numero de telefone Valido!\n")
            break
        else:
            print("Numero de telefone invalido.\n")
    
     while True:
        numero_celular = int(input("Numero celular: "))
        if len(numero_celular)==9:
            print("Numero de celular Valido!\n")
            break
        else:
            print("Numero de celular invalido.\n")
            
     while True:
        complemento = input("complemento: ")
        if len(complemento)>3:
            print("complemento válido!\n")
            break
        else:
            print("complemento invalida.\n")
            
     while True:
        bairro = input("bairro: ")
        if len(bairro)>3:
            print("bairro válido!\n")
            break
        else:
            print("bairro invalida.\n")
