def arithmetic_arranger(problems, display_answers=False):
  # Iniitialize Variables
  arranged_problems = ""
  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""

  # Check if Too Many Problems
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # Main Loop Start
  index = 0
  for problem in problems:
    # Split Problem into Constituents
    split_problem = problem.split()
    num1 = split_problem[0]
    operator = split_problem[1]
    num2 = split_problem[2]
    result = ""

    # Check if Incorrect Operator
    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."
    # Check if Only Digits
    elif not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."
    # Check if Too Many Digits
    elif len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    # Arrangement of Numbers
    first_line += "  "
    second_line += operator + " "
    for i in range(abs(len(num1) - len(num2))):
      if len(num2) > len(num1):
        first_line += " "
      elif len(num1) > len(num2):
        second_line += " "
    first_line += num1
    second_line += num2
  
    # Display Dashes Below the Numbers
    for i in range(max(len(num1), len(num2)) + 2):
        third_line += "-"
    
    # Display and Compute Results if Wanted
    if display_answers:
      if operator == "+":
        result = str(int(num1) + int(num2))
      elif operator == "-":
        result = str(int(num1) - int(num2))
      for i in range(max(len(num1), len(num2)) + 2 - len(result)):
        fourth_line += " "
      fourth_line += result
    
    # Space Between Problems
    if index != len(problems) - 1:
      first_line += "    "
      second_line += "    "
      third_line += "    "
      fourth_line += "    "
      index += 1    
  # Loop End
  
  # Combine the Lines
  arranged_problems = first_line + "\n" + second_line + "\n" + third_line
  if display_answers:
    arranged_problems += "\n" + fourth_line

  return arranged_problems