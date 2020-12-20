def check_if_exists(x, ls):
    if x in ls:
        print(str(x) + ' is inside the list')
    else:
        print(str(x) + ' is not present in the list')


ls = [1, 2, 3, 4, 'Hello', 'from', 'AskPython']

def main():
    check_if_exists(2, ls)
    check_if_exists('Hello', ls)
    check_if_exists('Hi', ls)
if __name__ == '__main__': main()