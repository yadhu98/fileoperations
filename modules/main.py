print("Before Math helper import")
from math_helper import PI,sum
print("Module Imported")

def main():
    print("Main Loaded")
    print("PI Value",PI)
    print("sum operation started")
    print(sum(3,4))


if __name__ == '__main__':
    print("Main is running first")
    main()