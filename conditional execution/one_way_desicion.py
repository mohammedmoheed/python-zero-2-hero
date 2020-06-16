

"""
    In python spacing does matter
    as we can see in this code ouput "is 6" is not printed becuse is wrong
    but next statement printed because i is outside of loop
    it ignore conditional statement

"""


x = 5
if x == 5:
    print('is 5')          #conditional code
    print('stiil 5')       #conditional code
print("before 6")    #sequential code
if x == 6:
    print('is 6')
print('after 6')


"""    ****OUTPUT*******
is 5
stiil 5
before 6
after 6
"""