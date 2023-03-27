# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1898953
# Date: 17/04/2022
Pass=0
Defer=0
Fail=0
P=0
T=0
E=0
R=0
Total_credits=0
Total=0
a='Progress'
b='Trailing'
c='Retriever'
d='Excluded'
print('Staff Version with Histogram')
print(' ')
key='y'
def enter_credits(x,y):                     # A user defined function to input the credits
    while True:
        try:                                # Making sure credits are valid and within range
            x= int(input('Enter your total credits at {} :'.format(y)))
            if x % 20 != 0 or x > 120 or x < 0:
                print("Out of range")
            else:
                return x
        except ValueError:
            print('Integer required')
def string_add(l,m):                        # A user defined function to make the headings of columns
    heading=l+' '+str(m)
    return heading
def input_key():                            # A user defined function for getting the value for key
    key = input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')
    key = key.lower()
    return key
while key!='q' and key=='y':                # A while loop for multiple progression outcomes
    Pass=enter_credits(Pass,"PASS")
    Defer=enter_credits(Defer,"DEFER")
    Fail=enter_credits(Fail,"FAIL")
    Total_credits = Pass + Defer + Fail
    if Total_credits != 120:                # Ensuring total_credits of a student is 120
        print('Total is incorrect')
    else:
        Total += 1
        if Pass == 120:                     # Deducing the progressive outcome
            print('Progress')
            P += 1
        elif Pass == 100:
            print('Progress(Module trailer)')
            T += 1
        elif Fail >= 80:
            print('Exclude')
            E += 1
        else:
            print('Module Retriever')
            R += 1
    print(' ')
    key=input_key()
    while key != 'y' and key != 'q':
        print('Invalid input...')
        key=input_key()
    print(' ')
h1=string_add(a,P)
h2=string_add(b,T)
h3=string_add(c,R)
h4=string_add(d,E)
print('-' * 100)
print('Horizontal Histogram')                # Printing the horizontal histogram using string multiplication
print(' ')
print(h1, '    ', ':', P * '*')
print(h2, '    ', ':', T * '*')
print(h3, '   ', ':', R * '*')
print(h4, '    ', ':', E * '*')
print(' ')
print(Total, 'outcomes in total.')
print('-' * 100)
