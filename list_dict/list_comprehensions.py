def run():
    
    my_list = [i for i in range(1,100000) if i%36==0]

    print(my_list)


if __name__ == '__main__':
    run()