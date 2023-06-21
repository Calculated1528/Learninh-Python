# text = "spam"
# ending = "eggs"
# "samurai", "ra"   


def solution(text:str, ending:str):
    # i = len(ending) - 1
    # print(text[-i-1:])
    # if text[-i-1:] == ending:
    #     return True
    # else:
    #     return False
    if text.endswith(ending):
        return True
    else: 
        return False

print(solution('samurai', 'ri'))
