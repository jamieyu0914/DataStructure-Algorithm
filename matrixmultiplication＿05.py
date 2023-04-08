#CH02_04
#matrix multiplication

#運算兩個矩陣相乘的結果

def MatrixMultiplication(arrA, arrB, arrC, M, N, P):
    global C
    if M<=0 or N<=0 or P<=0:
        print('[錯誤：維數M,N,P必須大於0]')
        return
    for i in range(M):
        for j in range(P):
            Temp=0
            for k in range(N):
                Temp = Temp + int(arrA[i*N+k])*int(arrB[k*P+j])
            arrC[i*P+j] = Temp
print('請輸入矩陣A的維數(M,N):')
M = int(input('M= '))
N = int(input('N= '))
A = [None]*M*N #宣告大小為MXN的串列A

print('[請輸入矩陣A的各個元素]')
for i in range(M):
    for j in range(N):
        A[i*N+j] = input('a%d%d='%(i,j))

print('請輸入矩陣B的維數(N,P):')
N = int(input('N= '))
P = int(input('P= '))

B = [None]*N*P #宣告大小為NXP的串列B

print('[請輸入矩陣B的各個元素]')
for i in range(N):
    for j in range(P):
        B[i*P+j] = input('b%d%d='%(i,j))

C = [None]*M*P #宣告大小為MXP的串列C
MatrixMultiplication(A,B,C,M,N,P)
print('[AXB的結果是]')
for i in range(M):
    for j in range(P):
        print('%d' %C[i*P+j], end='\t')
    print ()