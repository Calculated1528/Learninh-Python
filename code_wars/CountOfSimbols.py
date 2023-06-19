def duplicate_count(text):
    text.lower()
    for i in text:
            n = text.count(i)
            return n 
print (duplicate_count('hellooo')) 