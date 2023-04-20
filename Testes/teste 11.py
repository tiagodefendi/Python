for i in range(19):
    if i not in [7, 9, 11]:
        if i % 2 == 0:
            for j in range(19):
                print('\033[30;40m---\033[m', end='')
            print('')
        else:
            for j in range(19):
                if j % 2 == 0:
                    print('\033[30;40m---\033[m', end='')
                else:
                    if j not in [7, 9, 11]:
                        print('\033[7m 0 \033[m', end='')
                    else:
                        print('\033[30;44m 0 \033[m', end='')
            print('')
    else:
        if i % 2 == 0:
            for j in range(19):
                print('\033[30;40m---\033[m', end='')
            print('')
        else:
            for j in range(19):
                if j % 2 == 0:
                    print('\033[30;40m---\033[m', end='')
                else:
                    if j not in [7, 9, 11]:
                        print('\033[30;44m 0 \033[m', end='')
                    else:
                        print('\033[7m 0 \033[m', end='')
            print('')