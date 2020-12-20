

def main():

    carList =['ford','porsche','volve',"BMW"]

    carList.extend(["datsun","Toyota","Tesla"])

    for car in carList:
        print(car)
if __name__ == '__main__': main()