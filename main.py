def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  for problem in problems:
    parts = problem.split()
    if len(parts) != 3:
      return "Error: Invalid problem format."

    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    length = max(len(operand1), len(operand2)) + 2

    line1 += operand1.rjust(length) + "    "
    line2 += operator + " " + operand2.rjust(length - 2) + "    "
    line3 += "-" * length + "    "

    if show_answers:
      if operator == "+":
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))

      line4 += answer.rjust(length) + "    "

  arranged_problems = line1.rstrip() + "\n" + line2.rstrip(
  ) + "\n" + line3.rstrip()

  if show_answers:
    arranged_problems += "\n" + line4.rstrip()

  return arranged_problems


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))
