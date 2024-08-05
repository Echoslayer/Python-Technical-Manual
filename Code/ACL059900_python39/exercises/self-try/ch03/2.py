import sys

input_args = sys.argv

if len(input_args) > 2:
    select_word = sys.argv[1]
    compare_words = sys.argv[2:]
    
    print(compare_words.count(select_word))