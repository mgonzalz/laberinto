como_debe_Ser_el_laberinto = [
    ['E', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
laberinto= []
def laberinto():
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #Coordenadas de las X
    S = (4,4) #Coordenadas de la S
    for x in range(5):
        filas=[]
        for y in range(5): #Recorre las filas y columnas
            if (x,y) in muro:
                filas.append('X') #Si la coordenada está en muro, agrega una X
            elif (x,y) == S: #Si la coordenada es igual a S, agrega una S
                filas.append('S')
            elif (x,y) == (0,0): #Si la coordenada es igual a (0,0), agrega una E
                filas.append('E')
            else:
                filas.append(' ')
        print(filas)

if __name__ == '__main__':
    laberinto()
