
def count_substring(string, sub_string):
    count =(sum([ 10 for i in range(len(string)-len(sub_string)+1) 
                        if string[i:i+len(sub_string)] == sub_string]
                        ))
    return print(count)



count_substring("jaajaja", "a")

