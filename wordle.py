import sys
kelime = sys.argv[1]
while True:
    for k in range(6):
        print(k+1,end='')
        val = input('. try: ')
        if len(val) == 5:
            for m in range(5):
                if kelime[m] == val[m]:
                    print(m + 1, '. letter exists and located right place.')
                else:
                    if val[m] in kelime:
                        print(m + 1, '. letter exists but located wrong place.')
                    if val[m] not in kelime:
                        print(m + 1, '. letter does not exist.')
            if val == kelime:
                print('Congratulations! You guess right in', k+1,'. shot!')
                sys.exit()
        else:
            print('The length of word must be five!')
    if k == 5:
        print('You failed!')
        sys.exit()