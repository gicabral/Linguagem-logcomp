print(1)

def worker(arg1,arg2)
{
    print(arg1*arg2)
    print(0)
    print(arg1+arg2)
    
    return arg1/arg2
}

a = 10
b = 4
print(a**(b-1))
print(worker(a,b))