def checkio(words_set):
    words = list(words_set)
    for w in words:
        for j in words:
            if w != j and w.endswith(j):
                return True
            return False

#checkio({"hello", "lo", "he"})
checkio({"hello", "la", "hellow", "cow"})
checkio({"walk", "duckwalk"})
checkio({"helicopter", "li", "he"})
checkio({"helicopter", "li", "he"})

