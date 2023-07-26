import math

def gradingStudents(grades):
    result = []
    for elem in grades:
        if elem < 38:
            result.append(elem)
            continue
        elif elem == 100:
            result.append(elem)
            continue
        else:
            if math.ceil(elem/5)*5 - elem >= 3:
                result.append(elem)
            else:
                result.append(math.ceil(elem/5)*5)
    
    return result

print(gradingStudents([75, 67, 34, 55]))