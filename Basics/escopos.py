# escopo.py 
# Local versus Global
# definindo uma função local
def local():
    m = 7
    #printando m no escopo local da função
    print(m)
# definindo m no escopo global
m = 5
# chamando/executando a função
local()
#printando m no escopo global
print(m)
