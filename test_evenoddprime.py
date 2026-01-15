def evenodd_(num):
    if num %2==0:
        return "Even"
    else:
        return "Odd"

def prime_check(num):
    if num<=1:
        return "Not Prime"

    for i in range (2,num):
        if num % i==0:
            return "Not Prime"
    return "Prime"

if __name__=="__main__":
    print(evenodd_(10))
    print(prime_check(11))