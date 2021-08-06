def divisors(num):
    return [i for i in range(1,num+1) if num%i==0 ]
    

def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()