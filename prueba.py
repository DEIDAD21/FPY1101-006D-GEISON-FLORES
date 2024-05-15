'''
En este codigo se hara una lista de stock ocupando variables , for, if, while con un a lista un diccionario y un menu
con el cual haremos que pueda ver los productos, añadir productos, modificar el producto, eliminar el producto y salir
'''


import os

menu = ['Ver stock de productos', 'Añadir nuevo producto', 'Ajustar nuevo producto', 'Eliminar producto', 'Salir' ]

agenda = {'Lechuga': 10,'Sandia': 12,'Melon': 7,'Zapallo': 15}

while True:
        
        print('\n','*'*49,'\n','*'*12,'Administracion de stock','*'*12,'\n','*'*49)
        print('1. Ver stock de productos\n2. Añadir nuevo producto\n3. Ajustar nuevo producto\n4. Eliminar producto\n5. Salir')

        opcion = input('¿Que desea hacer?:\n')

        if opcion == '1':
            os.system('cls')
            for ind in enumerate(agenda):
                print(f'{agenda}')

        elif opcion == '2':
            os.system('cls')
            nombre_producto = input('Que producto desea agregar\n')
            cantidad_producto = input('¿Cuanta cantidad desea agregar?\n')
            print(f'El nuevo producto {nombre_producto} agreagado con exito')
            agenda[nombre_producto] = {cantidad_producto}

        elif opcion == '3':
            os.system('cls')
            produc_modific = input('¿Que producto desea modificar?')

        elif opcion == '4':
            os.system('cls')
            while True:
                procucto_eliminado = input('¿Que producto desea eliminar?\n')
                if procucto_eliminado in agenda.items():
                    del procucto_eliminado
                    print(f'El {procucto_eliminado} se eliminado perfectamente')
                    break
                else:
                    os.system('cls')
                    print('Error producto no encontrado')

        elif opcion == '5':
            os.system('cls')
            exit('!Adios que tenga un buen dia')
        else:
            os.system('cls')
            print('Error opcion ingresada no es valida')