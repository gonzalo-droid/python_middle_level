def run():
    
    # my_list = [i for i in range(1,100000) if i%36==0]
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

    


if __name__ == '__main__':
    run()