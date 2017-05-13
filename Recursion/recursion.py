def rec_sum(n):

    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print(rec_sum(5))

def sum_func(n):
    if n < 1:
        return 0
    else:
        return n%10 + sum_func(n//10)

print(sum_func(4321))


def word_split(phrase,list_of_words, output = None):

    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startwith(word):
            output.append(word)
            return  word_split(phrase[len(word):],list_of_words, output)
    return output