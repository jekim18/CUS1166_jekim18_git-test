def average_grade(roster):
    mysum = 0
    count = 0
    for i in roster:
        mysum += i.get_grade()
        count += 1
    return mysum / count