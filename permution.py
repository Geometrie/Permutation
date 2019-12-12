def enum_permutation(selection_len, candidate_len):
    permutation = list(range(candidate_len))
    index_tag = [0] * selection_len
    proceed = True
    while proceed:
        print(str(permutation))
        seek = 0
        proceed = False
        while seek < selection_len and (not proceed):
            ind = selection_len - seek - 1
            tmp = permutation[ind]
            while ind < candidate_len - 1:
                permutation[ind] = permutation[ind + 1]
                ind = ind + 1
            permutation[ind] = tmp
            if index_tag[selection_len - seek - 1] == candidate_len - selection_len + seek:
                index_tag[selection_len - seek - 1] = 0
            else:
                index_tag[selection_len - seek - 1] = index_tag[selection_len - seek - 1] + 1
                proceed = True
            seek = seek + 1


enum_permutation(2, 4)

