def checkweirdnum(x):
    if(x%2!=0):
        print("Weird")
    else:
        if (x>=2 and x<=5):
            print("Not Weird")
        elif (x>=6 and x<=20):
                print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    checkweirdnum(n)