import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pandas import DataFrame, Series
#y = [17,17.5,76,210.5,1970]
#x = [1,2,3,4,7]
# x = [1,1.2,1.4,1.6,2]
# y = [2.1435,2.297,2.639,3.031,4]

# x = [1,2,3,4,5]
# y = [2,4,8,16,32]


def multiPoly(A, B):
    prod = [0]*(len(A) + len(B) - 1)
    for i in range(0, len(A), 1):
        for j in range(0, len(B), 1):
            prod[i + j] += A[i] * B[j]
    return prod

def Lagrange(x, y, F, L):
    L = [[0] * len(x)] * len(x)
    poly = [[0, 0]]*len(x)  # mảng cho các đa thức đơn vị
    temp = [1]*len(x)
    tempPoly = [[]]*len(x)  # đa thức cơ sở ( 1 + 0*x)
    for i in range(len(x)):
        poly[i] = [-x[i], 1]
        # hàm tạo các đa thức nhỏ từ mảng x
    for i in range(len(x)):
        if i == 0:
            tempPoly[i] = poly[1]
        else:
            tempPoly[i] = poly[0]
        for j in range(len(x)):
            if (j != 0 and j != i and i != 0) or (i == 0 and (j > 1)):
                # if i != j:
                tempPoly[i] = multiPoly(tempPoly[i], poly[j])
                # tinh tu so L[i]
            if j != i:
                temp[i] *= (-poly[i][0] + poly[j][0])
                # tính mẫu số L[i]
    for i in range(len(tempPoly)):
        L[i] = [tempPoly[i][j]/temp[i] for j in range(len(tempPoly[i]))]
        # tính các đa thức Lagrange cơ bản

    for i in range(len(x)):
        for j in range(len(x)):
            F[i] += L[j][i] * y[j]
            # tính đa thức Lagrange
    return L, F

def printPoly(F):
    print("F = ", end='')
    for i in range(len(F)):
        if i != len(F)-1:
            print(f'{F[i]}*x^{i} + ', end='')
        else:
            print(f'{F[i]}*x^{i}  ', end='')

def choosePoint(x, y):
    index = 0
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if y[j] > y[j + 1]:
                m = x[j]
                x[j] = x[j + 1]
                x[j + 1] = m
                n = y[j]
                y[j] = y[j + 1]
                y[j + 1] = n 
    print(x)
    print(y)
    point = float(input("Nhap diem noi suy: "))
    for i in range(len(y)):
        if point < (y[i]):
            index = i
            break
    
    print("Vị trí mở rộng lấy mốc: " + str(index))
      
    
    if index == 0 or index == None:
        print("Moc duoc chon khong nam trong khoang noi suy.")
    else:
        if len(x) < 6:
            print("Lay tat ca cac moc noi suy vi so moc noi suy khong nhieu")
            newX = x
            newY = y
        else:
            head = index
            tail = index
            numbermoc = int(input("Nhap so moc noi suy muon lay: "))
            while numbermoc >= 0:
                if head == 0:
                    tail += 1
                    numbermoc -= 1
                if tail == len(x):
                    head -=1
                    numbermoc -= 1
                else:
                    if(numbermoc % 2 == 0):
                        head -= 1
                        tail += 1
                        numbermoc -= 2
                    else:
                        head -= 1
                        numbermoc -=1
            print(str(head) + "/" + str(tail))
            newX = x[head:tail]
            newY = y[head:tail]
    return newX, newY

def drawGraph(x, x_inver, y):
    plt.plot(y,x,'r')
    plt.plot(y, x_inver,'gr')
    plt.show()

if __name__ == "__main__":
    data = pd.read_excel('VD.xlsx')
    x = []
    y = []
    for i in range(len(data)):
        x.append(data.iat[i, 0])  # đọc dữ liệu lưu cho x
        y.append(data.iat[i, 1])  # đọc dữ liệu lưu cho y
    print(x)
    print(y)
    x, y = choosePoint(x, y)
    print(x)
    print(y)
    F = [0]*len(x)  # mảng cho đa thức nội suy Lagrange
    L = [[0]*len(x)]*len(x)  # mảng cho các đa thức Lagrange cơ bản
    L, F = Lagrange(y, x, F, L)
    printPoly(F)
    k = 0.15

    result = 0
    for i in range(len(F)):
        result += F[i]*pow(k,i)
        #thử lại 
    print("\n kết quả")
    print(result)
    
    x_inver = [0]*len(y)
    for i in range(len(y)):
        for j in range(len(F)):
            x_inver[i] += F[j]*pow(y[i],j)
    print(x_inver)
    
    #drawGraph(x,x_inver,y)
    
   
   

