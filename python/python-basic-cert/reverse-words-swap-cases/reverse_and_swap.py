
def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    ret_val = str()
    s_case_swapped = sentence.swapcase()
    s_list = s_case_swapped.split(" ")
    s_list.reverse()
    ret_val = " ".join(s_list)
    # print(ret_val)
    return ret_val