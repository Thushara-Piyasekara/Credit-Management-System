# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1899372 # Date: 16/04/2022

credit_pass = int(0)
credit_defer = int(0)
credit_fail = int(0)
option = str('y')
count = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []


def value_check(credit_name):
    global total
    while True:
        try:
            credit_input = int(input('Please enter your credits at {} : '.format(credit_name)))
            if credit_input not in (0, 20, 40, 60, 80, 100, 120):
                print('Out of range')
            else:
                total = total + credit_input
                return credit_input

        except ValueError:
            print('Integer required')


def list_call(list_name, outcome_list):
    for i in range(0, len(outcome_list), 3):
        small_list = outcome_list[i:i + 3]
        print(list_name, end='')
        print(*small_list, sep=", ")


while True:
    if option in ('Y', 'y'):
        total = 0
        print('')

        credit_pass = value_check("pass")
        credit_defer = value_check("defer")
        credit_fail = value_check("fail")

        if total != 120:
            print("Total incorrect")
            continue
        elif credit_pass == 120:
            print('Progress')
            progress += 1
            progress_list.extend((credit_pass, credit_defer, credit_fail))
        elif credit_pass == 100:
            print('Progress (module trailer)')
            trailer += 1
            trailer_list.extend((credit_pass, credit_defer, credit_fail))
        elif credit_fail >= 80:
            print('Exclude')
            exclude += 1
            exclude_list.extend((credit_pass, credit_defer, credit_fail))
        else:
            print('Module retriever')
            retriever += 1
            retriever_list.extend((credit_pass, credit_defer, credit_fail))
        count += 1
    elif option in ('q', 'Q'):
        break
    else:
        print('\nPlease Enter a Valid Input')
    option = str(input('\nWould you like to enter another set of data? '
                       '\nEnter \'y\' for yes or \'q\' to quit and view results: '))

# Horizontal Histogram

print('\n','-'*100)
print('\nHorizontal Histogram\n')
print('  Progress', progress, '    :', '*'*progress)
print('  Trailer', trailer, '     :', '*'*trailer)
print('  Retriever', retriever, '   :', '*'*retriever)
print('  Excluded', exclude, '    :', '*'*exclude)
print('\n', count, 'outcomes in total.')
print('\n','-'*100)



# Vertical Histogram
# Learned how to print stars vertically from here:-
# https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops

print('\nVertical Histogram\n')
header = ['  Progress', str(progress), '| Trailing', str(trailer), '| Retriever', str(retriever), '| Excluded', str(exclude)]
print(' '.join(header))
for x in range(max(progress, trailer, retriever, exclude)):
    print("       {0}           {1}            {2}            {3}".format(
        '*' if x < progress else ' ',
        '*' if x < trailer else ' ',
        '*' if x < retriever else ' ',
        '*' if x < exclude else ' '))

print('\n',count, 'outcomes in total.')
print('\n','-'*100)


print('\nList View\n')
list_call('  Progress - ',progress_list)
list_call('  Progress (module trailer) - ',trailer_list)
list_call('  Module retriever - ',retriever_list)
list_call('  Exclude – ',exclude_list)
