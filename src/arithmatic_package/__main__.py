print("Arithmatic Package Called")

from arithmatic_package import arithmatic
from arithmatic_package import numpy_arithmatic

def main():
    a = 10
    b = 12.3
    print(arithmatic.add(a, b))
    print(arithmatic.substract(a,b))
    print(arithmatic.multiply(a,b))
    print(arithmatic.divide(a,b))

#if __name__ == '__main__':
#    main()
main()