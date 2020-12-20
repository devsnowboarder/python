
t
def main():

    try:
        x=5/2
    except ValueError:
        print('I caught a ValueError')
    except:
        print('unknow error')
    else:
        print('good job')
        print(x)
if __name__ =='__main__': main()
