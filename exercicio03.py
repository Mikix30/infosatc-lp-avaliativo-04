name=[]
password=[]
pronto=[]
cpf=[]


def fc(name, cpf, password, pronto, z, a):
    
    print("")
    
    print("O nome do cliente", z," é ",name[a])
    
    print("A senha do cliente", z," é ",password[a])
    
    print("O cliente ", z," esta pronto? ",pronto[a])
    
    print("O cpf do cliente", z," é ",cpf[a])
    

def user():

    name.append(input("Qual o seu nome? "))
    
    password.append(input("Qual a sua senha? "))
    
    cpf.append(input("Qual o seu cpf? "))

    pronto.append(input("Você está disposto? "))

tp = (int(input("Qual é o número total de pessoas que irão realizar o exame? ")))

for z in range(tp):


    ap = " "
    
    print(" ")

    alt = 0
    
    user = 0
    
    
    

    kg = (float(input("Qual o seu peso? ")))
   
    i = (float(input("Quanto tempo você dormiu no ultimo dia ?(em h) ")))
   
    age = (int(input("Qual a sua idade? ")))
    
    


    if age > 16 and age < 69:
    
        alt = alt + 1
    
    else:
    
        ap = " idade " + ap
    
    if kg > 50:
    
        alt = alt + 1
    
    else:
    
        ap = "kg " + ap
    
    if i > 6:
    
        alt = alt + 1
    
    else:
    
        ap = " horas dormidas " + ap

    if alt == 3:
    
        print("Sim, pode ser um doador.")
    
        alt=(input("Gostaria de se cadastrar? (y/n): "))
    
        if (alt == "y"):
    
            user = user + 1
    
            user()
    
        else:
    
            pass
    
    else:
    
        print("Você não está dentro dos requesitos.")

for z in range(user):

    cont = z + 1

    fc(cont, name, password, cpf, pronto, z)
