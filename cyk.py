import networkx as nx
import matplotlib.pyplot as plt

# Función para leer el archivo de gramática y analizar las reglas
def leer_gramatica(archivo):
    reglas = {}
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                izquierda, derecha = linea.split('->')
                izquierda = izquierda.strip()
                derecha = [parte.strip() for parte in derecha.split()]
                reglas[izquierda] = derecha
    return reglas

# Función para generar el árbol gramatical usando las reglas
def generar_arbol(gramatica, simbolo_inicial='S'):
    G = nx.DiGraph()  # Grafo dirigido
    agregar_reglas_al_grafo(G, gramatica, simbolo_inicial)
    return G

# Función auxiliar para agregar reglas al grafo de árbol
def agregar_reglas_al_grafo(G, gramatica, simbolo, padre=None):
    if padre:
        G.add_edge(padre, simbolo)  # Crear una arista entre el padre y el símbolo actual
    
    # Si el símbolo está en las reglas gramaticales, seguir expandiendo
    if simbolo in gramatica:
        for parte in gramatica[simbolo]:
            agregar_reglas_al_grafo(G, gramatica, parte, simbolo)
    else:
        G.add_node(simbolo)  # Añadir terminal

# Función para dibujar el árbol
def dibujar_arbol(G):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # Disposición del gráfico
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.show()

# Programa principal
if __name__ == '__main__':
    archivo_gramatica = 'gramatica.txt'  # Especificar el archivo de gramática
    gramatica = leer_gramatica(archivo_gramatica)  # Leer y analizar la gramática
    arbol = generar_arbol(gramatica, simbolo_inicial='S')  # Generar el árbol a partir del símbolo inicial
    dibujar_arbol(arbol)  # Dibujar el árbol



