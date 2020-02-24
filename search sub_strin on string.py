"""
soliucion con comprehension list y sin comprehension list
ambas solucione sllevan al mismo lugar
"""

def count_substring(string, sub_string):
    count =(sum([ 1 for i in range(len(string)-len(sub_string)+1) 
                        if string[i:i+len(sub_string)] == sub_string]
                        ))
    return count

def count_substring_sc(string, sub_string):
    count = 0
 
    if 1 <= len(string) <= 200:
        for i in range(0, len(string)-len(sub_string)+1):
            
            if string[i:i+len(sub_string)]== sub_string :
                count += 1
            

    return count

print(count_substring_sc("jaajaja", "a"))
print(count_substring("jaajaja", "a"))

