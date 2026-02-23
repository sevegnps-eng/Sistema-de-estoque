
estoque = []

# Armazenar Produtos

def armazenar():
    
    produto = input("Qual produto deseja armazenar? ").lower()
    quantidade = int(input("Qual quantidade deseja armazenar? "))
    valor = (float(input("Qual valor deseja colocar no produto? ")))  

    for itens in estoque:
        if itens["Produto"] == produto:
            print("Esse produto já existe no estoque, atualizando quantidade. ")
            itens["Quantidade"] += quantidade
            
            return estoque

    estoque.append({
        "Produto": produto,
        "Quantidade": quantidade,
        "Valor": valor
    })

    return estoque

# Listar Produtos

def listar_produtos():
    
    for itens in estoque:
        print(itens)

# Remover Produtos

def remover_produtos():
   
   for itens in estoque:
      
      item = input("Qual produto deseja remover? ")
      
      if item in itens == item:
         del itens["Produto"]


      return
        
            
# Programa principal

def programa_principal():

   while True:
    
      opcao = int(input("\n[1] Adicionar Produto \n[2] Remover produto \n[3] Listar produtos \n[4] Sair do programa \nSelecione uma opcão: ")) 

      if opcao == 1:
       armazenar()

      if opcao == 2:
       remover_produtos()
   
      if opcao == 3:
       listar_produtos()

      if opcao == 4:
         print("Saindo do estoque...")
         break
      
      else:
         
         if opcao > 4:
            print("Opção inválida")
      
programa_principal()




