
def third(user_input = ('1,2,3,4,5,6,7,8,9')):
    user_input
    try:    
        arry = list(map(int,user_input.split(',')))
        arry.sort()
        return(f'The third smallest number is {arry[2]}')
    except Exception as e:
        print(f'Error:{e}')