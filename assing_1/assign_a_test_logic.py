def priem_test(a =2,b =9):
    total = 0
    
    if b > a:
        for number in range(a,b+1):
            if number >= 2:
                is_prime = True
                for i in range(2, int(number**0.5) + 1):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                        total += number
                        
        return(f'addition of prim numbers is {total}')
    else:
        return('please enter numbers  and second number should be > than first')
priem_test()