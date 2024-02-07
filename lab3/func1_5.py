import itertools
def permutation(string):
    perm_list=itertools.permutations(string)
    for perm in perm_list:
        print(''.join(perm))

string=str(input())
permutation(string)