from grpc import ClientCallDetails
#이마이카나성우기원
import numpy as np
level = 0
class noInverse(Exception):
    def __init__(self):
        super().__init__('行列式が0であるため、逆行列が存在しません。')

def arrayAdd(c):
    row = int(input('行列の行の数を入力してください:'))
    col = int(input('行列の列の数を入力してください:'))
    a = np.zeros(shape = (row, col))
    for i in range(row):
        for j in range(col):
            a[i][j] = float(input('1番目の行列の{}行、{}列の成分を入力してください:'.format(i+1, j+1)))
    b = np.zeros(shape = (row, col))
    for i in range(row):
        for j in range(col):
            b[i][j] = float(input('2番目の行列の{}行、{}列の成分を入力してください:'.format(i+1, j+1)))
    level = 0
    print('0段階: 入力された行列です。')
    print(a, b, sep = '\n\n')
    input()
    ans = a.copy()
    if c == 1: #加算
        for j in range(row):
            for k in range(col):
                ans[j][k] += b[j][k]
                level += 1
                print('{}段階: {}行、{}列の成分同士を加えます。'.format(level, j+1, k+1))
                print(ans)
                input()
        print('行列の加算が完了されました。')
        print(a, '+', b, '=', ans, sep = '\n')
    else: #減算
        for j in range(row):
            for k in range(col):
                ans[j][k] -= b[j][k]
                level += 1
                print('{}段階: {}行、{}列の成分同士を減らします。'.format(level, j+1, k+1))
                print(ans)
                input()
        print('行列の減算が完了されました。')
        print(a, '-', b, '=', ans, sep = '\n')



def invArray():
    row = int(input('行列の行の数を入力してください:'))
    a = np.zeros(shape = (row, row))
    for i in range(row):
        for j in range(row):
            a[i][j] = float(input('行列の{}行、{}列の成分を入力してください:'.format(i+1, j+1)))
    b = np.identity(n = row)
    if np.linalg.det(a) == 0: raise noInverse
    level = 0
    print('0段階: 入力された行列です。下に単位行列を書きます。')
    print(a, b, sep = '\n\n')
    input()
    ans = a.copy()
    ans = ans.astype(float)
    for i in range(row):
        if ans[i][i] == 0:
            for j in range(row):
                if ans[j][i] != 0:
                    level += 1
                    ans[i] += ans[j]
                    b[i] += b[j]
                    ans, b = ans.astype(float), b.astype(float)
                    print('{0}段階: {1}行、{1}列の成分を0以外にするため、{1}行に{2}行を加えます。'.format(level, i+1, j+1))
                    print(ans, b, sep = '\n\n')
                    input()
                    break
    for i in range(row):
        for j in range(row):
            if i == j and ans[i][i] != 1:
                level += 1
                c = ans[i][i]
                ans[i] /= c
                b[i] /= c
                ans, b = ans.astype(float), b.astype(float)
                print('{0}段階: {1}行、{1}列の成分を1にするため、{1}行に{2}を引きます。'.format(level, i+1, c))
                print(ans, b, sep = '\n\n')
                input()
            elif i != j and ans[j][i] != 0:
                level += 1
                c = ans[j][i] / ans[i][i]
                ans[j] -= (ans[i] * c)
                b[j] -= (b[i] * c)
                ans, b = ans.astype(float), b.astype(float)
                print('{0}段階: {1}行、{2}列の成分を0にするため、{1}行に{2}行の{3}倍を引きます。'.format(level, j+1, i+1, c))
                print(ans, b, sep = '\n\n')
                input()
    print('逆行列の計算が完了されました。')
    print(a, '^(-1)', '\n=\n', b, '\n' )

def multiArray():
    row = int(input('行列の行の数を入力してください:'))
    col = int(input('行列の列の数を入力してください:'))
    a = np.zeros(shape = (row, col))
    for i in range(row):
        for j in range(col):
            a[i][j] = float(input('行列の{}行、{}列の成分を入力してください:'.format(i+1, j+1)))
    m = float(input('行列に何倍を乗算しますか:'))
    level = 0
    print('0段階: 入力された行列です。')
    print(a)
    input()
    ans = a.copy()
    for j in range(row):
        for k in range(col):
            ans[j][k] *= m
            level += 1
            print('{}段階: {}行、{}列の成分に{}を乗算します。'.format(level, j+1, k+1, m))
            print(ans)
            input()
    print('行列の実数倍が完了されました。')
    print(a, '*', m, '=', ans, sep = '\n')

def calDet(array):
    global level
    if np.shape(array) == (1, 1):
        return array[0][0]
    else:
        det = 0
        for i in range(len(array)):
            calArr = np.delete(np.delete(array, i, axis = 0), 0, axis = 1)
            det += calDet(calArr) * array[i][0] * (-1)**i
            level += 1
            print('{}段階: 下の行列に{}を乗算してdetに加えます。'.format(level, array[i][0] * (-1)**i ))
            print(calArr, '\n', det, sep = '')
            input()
        return det
def detArray():
    global level
    row = int(input('行列の行の数を入力してください:'))
    a = np.zeros(shape = (row, row))
    for i in range(row):
        for j in range(row):
            a[i][j] = float(input('行列の{}行、{}列の成分を入力してください:'.format(i+1, j+1)))
    level = 0
    print('0段階: 入力された行列です。')
    print(a)
    input()
    det = calDet(a)
    print('行列式の計算が完了されました。')
    print('det(\n', a, '\n)=', det)

#이마이카나성우기워