def hcf(a,b):
    assert int(a)==a and int(b)==b ,'Enter a  integer '
    if a<0:
        a =-1*a
    if b<0:
        b =-1*b
    if b==0:
        return a
    else:
        return hcf(b,a%b)
    

print(hcf(48,-18))