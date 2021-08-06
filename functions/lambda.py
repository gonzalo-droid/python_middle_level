from functools import reduce

def run():
    #lambda
    palindromo = lambda string: string == string[::-1]
 

    #filter
    '''
    ilter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
    '''
    my_list =[1,2,5,9,56,12,3,10]
    odd = list(filter(lambda x: x%2 != 0, my_list))

    #map
    '''Map funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.
    '''
    my_list =[1,2,5,9,56,12,3,10]
    odd = list(map(lambda x: x%2 != 0, my_list))

    #reduce
    my_list =[2,2,2,2,2]
    odd = reduce(lambda a,b : a*b, my_list)

    print(odd)
    


if __name__ == '__main__':
    run()