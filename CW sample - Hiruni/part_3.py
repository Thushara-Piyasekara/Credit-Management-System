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
list=[]
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
            element=a+' - '+str(Pass)+','+str(Defer)+','+str(Fail)
        elif Pass == 100:
            print('Progress(Module trailer)')
            T += 1
            element=b+' - '+str(Pass)+','+str(Defer)+','+str(Fail)
        elif Fail >= 80:
            print('Exclude')
            E += 1
            element=c+' - '+str(Pass)+','+str(Defer)+','+str(Fail)
        else:
            print('Module Retriever')
            R += 1
            element=d+' - '+str(Pass)+','+str(Defer)+','+str(Fail)
        list.append(element)
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
print('vertical Histogram')
print(' ')
header=[h1,'|',h2,'|',h3,'|',h4,]            # REFERENCE - https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
print(' '.join(header))
for x in range(max(P,T,R,E)):
    print("   {0}            {1}             {2}             {3}".format(
        '*' if x < P else ' ',
        '*' if x < T else ' ',
        '*' if x < R else ' ',
        '*' if x < E else ' '))
print(' ')
print(Total, 'outcomes in total.')
print('-' * 100)
print('Data stored in the list')
print(' ')
print(*list,sep='\n')                        # REFERENCE - https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
