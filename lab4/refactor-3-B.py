def fix(moves, should):
    if moves:
        if not should:
            return "duct tape"
        else:
            return "good"
    else:
        if not should:
            return "good"
        else:
            return "duct tape"

print(fix(False, False))
