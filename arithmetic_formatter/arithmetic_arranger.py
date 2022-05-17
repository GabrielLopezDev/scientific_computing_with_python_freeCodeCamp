def arithmetic_arranger(problems: list, answers: bool = False):
    # Verificando la cantidad de problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands: list = []
    second_operands: list = []
    operators: list = []

    # Separando la data
    for problem in problems:
        parts = problem.split()
        first_operands.append(parts[0])
        operators.append(parts[1])
        second_operands.append(parts[2])

    # Verificando que no existan operadores inválidos (* o /)
    if "*" in operators or "/" in operators:
        return "Error: Operator must be '+' or '-'."

    # Verificando que los operandos solo contengan dígitos
    for i in range(len(first_operands)):
        if not first_operands[i].isdigit() or not second_operands[i].isdigit():
            return "Error: Numbers must only contain digits."

    # Verificando que los operandos no sean mayores a 4 dígitos
    for i in range(len(first_operands)):
        if len(first_operands[i]) > 4 or len(second_operands[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Preparando data a visualizar
    first_line: str = ""
    second_line: str = ""
    third_line: str = ""

    for i in range(len(first_operands)):
        if len(first_operands[i]) > len(second_operands[i]):
            first_line += " " * 2 + first_operands[i]
            second_line += operators[i] + " " + second_operands[i].rjust(len(first_operands[i]))
            third_line += "-" * (2 + len(first_operands[i]))
        else:
            first_line += first_operands[i].rjust(2 + len(second_operands[i]))
            second_line += operators[i] + " " + second_operands[i]
            third_line += "-" * (2 + len(second_operands[i]))

        if i < len(first_operands) - 1:
            first_line += " " * 4
            second_line += " " * 4
            third_line += " " * 4

    # Preparando resultados de la suma de las listas
    fourth_line: str = ""
    if answers:
        for i in range(len(first_operands)):
            if operators[i] == "+":
                temp_value = int(first_operands[i]) + int(second_operands[i])
            else:
                temp_value = int(first_operands[i]) - int(second_operands[i])

            if len(first_operands[i]) > len(second_operands[i]):
                fourth_line += str(temp_value).rjust(2 + len(first_operands[i]))
            else:
                fourth_line += str(temp_value).rjust(2 + len(second_operands[i]))

            if i < len(first_operands) - 1:
                fourth_line += " " * 4

    if not answers:
        return f"{first_line}\n{second_line}\n{third_line}"

    return f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}"