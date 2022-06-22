#escopo_global.py
# Local versus Global
def local():
    #m não pertence ao escopo da função local
    #então o Python vai procurar no próximo escopo, no caso o global utilizando a regra LEGB 
    
    #The order Local, Enclosing, Global, Built-in is the order of precedence for scope resolution. 
    # That means Python searches for the value of a name in each of these namespaces in turn

    #The local scope is the scope of all objects in the current namespace

    #The enclosing scope is the scope of any objects in the namespace that encloses the current namespace, which may or may not exist.

    #The global scope is the scope of objects in the module-level namespace.

    #The built-in scope is the scope of all objects that are built into the Python language. Reserved names like dict are found in this namespace.

    print(m, 'printando o escopo local')
m = 5
print(m, 'printando o escopo global')
local()
