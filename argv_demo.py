import sys

if __name__ == "__main__":
    print(f"The number of arguments is: {len(sys.argv)}")
    for index, arg in enumerate(sys.argv):
        print(f"Argument number {index} is {arg}")
