def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line, second_line, third_line, fourth_line = "", "", "", ""

    for problem in problems:
        num1, operator, num2 = problem.split()
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(width) + "    "
        second_line += operator + num2.rjust(width - 1) + "    "
        third_line += "-" * width + "    "

        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            fourth_line += answer.rjust(width) + "    "

    problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip() 
    if show_answers:
        problems += "\n" + fourth_line.rstrip()   

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')