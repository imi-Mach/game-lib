import timeit

mySetup = '''
board = [["0"]*3]*3
'''

tests = list()

tests.append('''
def Method1(board):
    board_str = list()
    for i, row in enumerate(board):
        board_str.append(" | ".join(row))
    return "\\n\{\}\\n".format("-"*3*3).join(board_str)
''')

tests.append('''
def Method2(board):
    def F(row):
        return " | ".join(row)
    #F = lambda row: " | ".join(row)
    return "\\n\{\}\\n".format("-"*3*3).join(map(F,board))
''')

tests.append('''
def Method2(board):
    #F = lambda row: " | ".join(row)
    return "\\n\{\}\\n".format("-"*3*3).join(map(F,board))
''')

print("---------------Tests Start---------------")
for i, test in enumerate(tests):
    print("Test: Method {}".format(i+1))
    print("\t", timeit.timeit(setup=mySetup, stmt=test, number=10000000), end="\n\n")
print("----------------Tests end----------------")