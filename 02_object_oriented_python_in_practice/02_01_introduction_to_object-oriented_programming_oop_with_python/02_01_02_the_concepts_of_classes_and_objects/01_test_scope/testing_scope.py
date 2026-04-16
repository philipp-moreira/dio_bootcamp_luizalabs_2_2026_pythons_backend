# global number_a
# number_a = 1


def func_1():
    # global number_a
    number_a = 2

    print('func_1()', 'number_a', number_a)

    def func_2():
        # nonlocal number_a
        # number_a += 4
        number_aa = 6
        print('func_2()', 'number_a', number_a)
        print('func_2()', 'number_aa', number_aa)

        def func_3():
            # nonlocal number_a, number_aa
            # number_a += 6
            # number_aa += 8
            number_aaa = 10
            print('func_3()', 'number_a', number_a)
            print('func_3()', 'number_aa', number_aa)
            print('func_3()', 'number_aaa', number_aaa)

        func_3()

    func_2()


func_1()
