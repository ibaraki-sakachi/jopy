from arr import *
def main():
    print('行列計算機 by そらみ')
    print('1 = 加算、2 = 減算 3 =整数倍 4 = 行列式 5 = 逆行列')
    menu = input('何を計算しますか:')
    if menu == '1': arrayAdd(1)
    elif menu == '2': arrayAdd(-1)
    elif menu == '3': multiArray()
    elif menu == '4': detArray()
    elif menu == '5': invArray()

if __name__ == '__main__':
    main()
