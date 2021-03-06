#!/usr/bin/python

input_file="..\\input\\problema1.txt"
lines = open(input_file,'r').readlines()

# node class used by BTree
class Node():    
    def __init__(self, info: tuple) -> None:
        self.name = str(info[0])
        self.qtd = int(info[1])
        self.rchild = None
        self.lchild = None    

# simple binary search tree
class BTree():
    def __init__(self) -> None:
        self.node = None
    
    # retorna o último colo
    def get_minor(self):
        c_node = self.node
        while None != c_node.lchild:
            c_node = c_node.lchild
        return (c_node.name,c_node.qtd)
        
    # funcao para adicionar um novo nó na arvore de acordo com seu peso
    # este por sua vez é definido pela qtd de problemas resolvidos
    # em caso de empate entre a qtd, o desempate é realizado por 
    # ordem alfabética do nome 
    def add_node(self, newNode: Node) -> None:
        if None == self.node:
            self.node = newNode
            return            
        c_node = self.node
        while True:
            if newNode.qtd > c_node.qtd:
                if None == c_node.rchild:
                    c_node.rchild = newNode
                    return
                else:
                    c_node = c_node.rchild
            elif newNode.qtd < c_node.qtd:
                if None == c_node.lchild:
                    c_node.lchild = newNode
                    return
                else:
                    c_node = c_node.lchild
            else: 
                # caso haja empate a decisao de ordenacao 
                # é tomada pela ordem alfabética do nome
                if alfabetica(newNode.name,c_node.name):
                    # newNode < c_node
                    if None == c_node.lchild:
                        c_node.lchild = newNode
                        return
                    else:
                        c_node = c_node.lchild
                else:
                    # newNode > c_node
                    if None == c_node.rchild:
                        c_node.rchild = newNode
                        return
                    else:
                        c_node = c_node.rchild                

# funcao para identificar o menor elemento, utiliza 0 e 1 para 
# sinalização externa de qual é menor
arg_min = lambda x,y: (x,0) if x < y else (y,1)

# retorna um bool
# True:  o primeiro parâmetro vem antes que o segundo em ordem alfabética
# False: o segundo parâmetro vem antes que o primeiro em ordem alfabética
def alfabetica(str1, str2):
    lim = arg_min(len(str1),len(str2))
    df = lim[1] # decisao final
    lim = lim[0] # len da menor string
    index = 0
    # normalização das strings em lowercase para não dar conflito entre 
    # 'A' e 'a'
    # remoção de espacos da string para otimização
    str1 = str1.lower().replace(' ','')
    str2 = str2.lower().replace(' ','')
    # antecipa se as fatias são iguais 
    if str1[:lim] != str2[:lim]:        
        # tenta diferenciar nos caracteres
        while index < lim:
            if ord(str1[index]) < ord(str2[index]):
                return True
            elif ord(str1[index]) > ord(str2[index]):
                return False
            index+=1
    # caso não seja diferenciado nos caracretes a menor string 
    # vem primeiro
    # df 0 -> primeira string é menor
    # df 1 -> segunda string é menor
    return 0==df

# funcao para limpar as linhas brutas extraindo
# o nome e a quantidade de probelmas resolvidos
def get_info(x):
    x = x.replace('\n','').split(' ')
    n_problems = x[len(x)-1]
    name = ''
    for e in x[:len(x)-1]:
        name+=e+' '
    #id = hash(name)
    return (name[:len(name)-1],n_problems)

# funcao que recebe as linhas brutas de uma instância 
# limpa as linhas e preenche a árvore binária de 
def verificar_instancia(l: list):
    tree = BTree()
    index = 0
    while index < len(l):
        info = get_info(l[index])
        tree.add_node(Node(info))
        index+=1    
    return tree.get_minor()

# funcao para receber as linhas brutas do arquivo
# e separalas em grupos de instâncias
def separar_instancias(lines: list):
    index = 0
    instancias = []
    while index < len(lines):
        n_registers = int(lines[index].replace('\n',''))
        index+=+1 # avança 1 linha
        instancias.append(lines[(index):(index+n_registers)])
        index = index+n_registers+1
    return instancias

instancias = separar_instancias(lines=lines)
id = 0
while id < len(instancias):
    result = verificar_instancia(instancias[id])
    print('Instância {}\n{} {}\n'.format((id+1),result[0],result[1]))
    id+=1
