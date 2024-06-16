num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k =3
b=[]
for i in range(len(num_list)-k+1):
    a = num_list[i:i+k]
    b.append(max(a))
print(b)