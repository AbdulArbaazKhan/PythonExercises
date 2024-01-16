

def arithmetic_arranger(arth_problems: list, *display: bool):
    problem_results = []
    spaces_of_max_operand = []
    spaces_of_row2 = []

    if len(arth_problems)>5:
        return print("Error: Too many problems.")

    for problem in arth_problems:  # Errors handling
        p = problem.split(" ")
        if len(p[0]) > 4 or len(p[2])>4:
            return print("Error: Numbers cannot be more than four digits.")
        try:
            if p[1]=="+":
                problem_results.append(int(p[0])+int(p[2]))
            elif p[1]=="-":
                problem_results.append(int(p[0]) - int(p[2]))
            else:
                return print("Error: Operator must be '+' or '-'.")
        except Exception:
            return print("Error: Numbers must only contain digits.")



    i = 0
    for problem in arth_problems:  #Row1 - First Operand
        p = problem.split(" ")
        if len(p[0]) > len(p[2]):  # Getting the length(or spaces) of maximum of the two operands
            spaces_of_max_operand.append(len(p[0]))
        else:
            spaces_of_max_operand.append(len(p[2]))
        spaces_of_row2.append(len(f"{p[1]:<2}{p[2]:>{spaces_of_max_operand[i]}}"))
        print(f"{p[0]:>{spaces_of_row2[i]}}\t", end="")
        i += 1
    print("")
    i = 0
    for problem in arth_problems: #Row2 - Operator and Second Operand
        p = problem.split(" ")
        print(f"{p[1]:<2}{p[2]:>{spaces_of_max_operand[i]}}\t", end="")
        i+=1
    print("")
    for i in range(0, i): #Row3 - Dash lines along the entire length of each problem individually)
        print(f"{'-'*spaces_of_row2[i]}\t", end="")

    print("")
    if display: #Row4 - Result display
        for i in range(0, i+1):
            print(f"{problem_results[i]:{spaces_of_row2[i]}}\t", end="")


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

arithmetic_arranger(["7 + 6698", "3801 - 2", "123 + 49", "90 - 34", "90 + 34", "32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
