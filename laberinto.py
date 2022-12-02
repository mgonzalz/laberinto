como_debe_Ser_el_laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
laberinto= []
def laberinto():
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) #Coordenadas de las X
    for x in range(5):
        filas=[]
        for y in range(5):
            if (x,y) in muro:
                filas.append('X')
            else:
                filas.append(' ')
        print(filas)

if __name__ == '__main__':
    laberinto()
