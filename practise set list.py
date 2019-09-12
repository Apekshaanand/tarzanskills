spam = ['apples','bananas','tofu','cats']
def spam_string(spam):
    new_spam = ""
    for value in spam:
        if value == spam[-1]:
            new_spam = new_spam + " and "
            new_spam = new_spam + value
        else:
            new_spam = new_spam + value + ","
    final_value = "'" + new_spam + "'"

    return final_value
print(spam_string(spam))


