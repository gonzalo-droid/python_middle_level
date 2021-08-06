def divisors(num):

    assert  num > 0 , "ingresa un número positvo"
    return [i for i in range(1,num+1) if num%i==0 ]
    

def run():
    
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un numero")
    

if __name__ == '__main__':
    run()