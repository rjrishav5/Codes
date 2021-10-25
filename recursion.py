def sum_of_num(n):
    assert n>=0 and int(n)==n,'Number should be positive only!'
    if n==0:
        return 0
    else:
        return int(n%10) + sum_of_num(int(n/10))

def Power(num,exp):
    assert exp >=0 and int(exp) == exp,'The exponent must be Positive number'
    if exp ==0:
        return 0
    if exp ==1:
        return num
    return num * Power(num,exp-1)


print(sum_of_num(4523))
print(Power(2,4))