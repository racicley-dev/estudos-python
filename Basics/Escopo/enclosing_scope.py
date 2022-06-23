# scopes3.py
# Local, Enclosing and Global
def enclosing_func():
    m = 13
    def local():
        # A variável m não pertence ao escopo da função
        print(m, 'printando m do escopo local')
    # chamando a função, pela regra LEGB, ela buscará por m necessariamente na ordem LEGB (Local -> Enclosing -> Global -> Built-in)
    local()
m = 5
print(m, 'printing printing do escopo global')
enclosing_func()
