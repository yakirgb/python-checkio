def verify_anagrams(first_word, second_word):
    return sorted(list(first_word)) == sorted(list(second_word))
verify_anagrams1 = lambda f_w, s_w: sorted(f_w.replace(" ","").upper()) == sorted(s_w.replace(" ","").upper())
