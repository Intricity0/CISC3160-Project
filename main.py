import parser
import sys

def print_result(variables):
  for var, val in variables.items():
    print(f"{var} = {val}")

def split_line(line):
  result = []
  i = 0
  start = i
  while i < len(line):
    if line[i] == ';' or i >= len(line):
      i += 1
      #print(start, i+1)
      result.append(line[start:i])
      start = i+1
    i += 1
  
  if (line[start:]):
    result.append(line[start:])
  return result

def makeAssignments(input_file):
  try:
    variables = {}
    with open(input_file) as read:

      for line in read:
        s = split_line(line)
        for assignment in s:
          if len(assignment) > 0:
            parsed_line = parser.Parser(assignment, variables)
            variables[parsed_line.var] = parsed_line.result

    print_result(variables)
  except FileNotFoundError:
    print(f'File "{input_file}" not found.')
  except IOError:
    print(f'An error occurred while reading the file "{input_file}"')
  except Exception as e:
    print(f"{e}: {line}")

def main():
  try:
    if (len(sys.argv) == 1):
      raise Exception('Incorrect usage. Expected "main.py <input file>"')
  
    input_file = sys.argv[1]
    print(input_file)
    makeAssignments(input_file)
    
  except Exception as e:
    print(f"{e}")

if __name__ == "__main__":
  main()