def enum_combination(selection_len, candidate_len):
    selection = list(range(selection_len))
    proceed = True
    while proceed:
        print(str(selection))
        seek = 0
        proceed = False
        while seek < selection_len and (not proceed):
            if selection[selection_len - seek - 1] < candidate_len - seek - 1:
                proceed = True
                selection[selection_len - seek - 1] = selection[selection_len - seek - 1] + 1
                restore = selection_len - seek
                while restore < selection_len:
                    selection[restore] = selection[restore - 1] + 1
                    restore = restore + 1
            seek = seek + 1

enum_combination(3, 6)