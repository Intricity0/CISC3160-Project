import parser
import sys

def print_result(variables):
  for var, val in variables.items():
    print(f"{var} = {val}")

def main():
  try:
    if (len(sys.argv) == 1):
      raise Exception('Incorrect usage. Expected "main.py <input file>"')
  
    input_file = sys.argv[1]
    print(input_file)
    try:
      variables = {}
      with open(input_file) as read:

        for line in read:
          parsed_line = parser.Parser(line, variables)
          variables[parsed_line.var] = parsed_line.result

      print_result(variables)
    except FileNotFoundError:
      print(f'File "{input_file}" not found.')
    except IOError:
      print(f'An error occurred while reading the file "{input_file}"')
    except Exception as e:
      print(f"{e}: {line}")
  except Exception as e:
    print(f"{e}")

if __name__ == "__main__":
  main()