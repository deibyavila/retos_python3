"""
Read an integer . For all non-negative integers , print . See the sample for details.
"""

if __name__ == '__main__':
    print("")
    n = int(input())

    if 1<= n <= 20:
        for i in range(0,n):
            print(i**2)