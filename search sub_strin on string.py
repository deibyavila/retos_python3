

def count_substring(string, sub_string):
    count = 0
    if 1 <= len(string) <= 200:
        for i in range(0, len(string)):
            if string.find("sub_string") != -1:
                count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)