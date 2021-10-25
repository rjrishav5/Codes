#n = int(input())
#s = input()
#if s.count('A')>s.count('D'):
#    print('Anton')
#elif s.count('A')==s.count('D'):
#    print('Friendship')
#else:
#    print('Danik')

#s = input()
#t = input()
#if s[::-1]==t:
#    print('YES')
#else:
#    print('NO')



#n = int(input())
#inpu_arr = []
#while n>0:
#    a = list(map(int,input().split()))
#    inpu_arr.append(a)
#    n-=1
#max_number = 0
#presion_count = 0
#for a in inpu_arr:
#    presion_count = presion_count - a[0]+a[1]
#    if max_number < presion_count:
#        max_number = presion_count
#print(max_number)



#n,x=map(int,input().split())
#s=input()
#for i in range(x):
#    s=s.replace("BG","GB")
#print(s)



#n = int(input())
#n = str(n)
#if n.count('4')+n.count('7') == 7 or n.count('7')+n.count('4')==4:
#    print('YES')
#else:
#    print('NO')


#def dist(a):
#    s = str(a)
#    t = set()
#    for i in s:
#        if i in t:
#            return False
#        t.add(i)
#    return True
#a = int(input())
#while True:
#    a+=1
#    if dist(a):
#        print(a)
#        break


#n,h = map(int,input().split())
#arr=list(map(int,input().split()[:n]))
#count = 0
#for i in arr:
#    if i >h:
#        count+=2
#    else:
#        count+=1
#print(count)


#n = int(input())
#count = 0
#for i in range(n):
#    x,y = list(map(int,input().split()))
#    if y-x>=2:
#        count+=1
#print(count)


n = int(input())
main_list = list(map(int,input().split()))
main_dict = dict()
ans = ''
for i in range(1,n+1):
    main_dict[main_list[i-1]] = i

for i in range(1,n+1):
    ans +=str(main_dict[i])+ ' '
print(ans)
