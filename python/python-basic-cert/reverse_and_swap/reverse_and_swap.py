#!/usr/bin/env python3
"""This module reverses case and words in a sentence."""

def reverse_words_order_and_swap_cases(sentence):
    """Reverse the case and order words in a sentence."""
    # Write your code here
    ret_val = str()
    s_case_swapped = sentence.swapcase()
    s_list = s_case_swapped.split(" ")
    s_list.reverse()
    ret_val = " ".join(s_list)
    # print(ret_val)
    return ret_val


if __name__ == '__main__':
    TEST_STR = "This is a regular sentence."
    RESULT = reverse_words_order_and_swap_cases(TEST_STR)
    print(RESULT)
