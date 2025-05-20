def isLetter(input):
  return input.isalpha() or input == '_'

def isDigit(input):
  return input.isnumeric()

def isNonZeroDigit(input):
  return False if input == '0' else isDigit(input)

def isOperator(input):
  return input in "+-*="

def isLiteral(input):
  if (input == ""):
    return False
  
  if (len(input) == 1):
    return True
  elif (input[0] == '0'):
    if (input[1] == '0'):
      return False
    else:
      for num in input[1:]:
        if not isDigit(num):
          return False
  else:
    for num in input[1:]:
      if not isDigit(num):
        return False
  
  return  True

def isIdentifier(input):
  if (input == ''):
    return False
  
  if (not isLetter(input[0])):
    return False
  else:
    for letter in input[1:]:
      if (not isLetter(letter) and not isDigit(letter)):
        print(f"{letter} is not a letter or digit")
        return False
  return  True
  

def tokenize(input):
  input = input.strip()
  tokens = []
  i = 0
  
  if (input[-1] != ';'):
    raise Exception(f"Syntax Error. Line does not end with a semicolon")

  while i < len(input):
    current = input[i]

    if current.isspace():
      i += 1
      continue

    if isLetter(current):
      start = i
      while i < len(input) and (isLetter(input[i]) or isDigit(input[i])):
        i += 1
      iden = input[start:i]
      if isIdentifier(iden):
        tokens.append(iden)
      else:
        raise Exception(f"Invalid identifier {iden}")
    elif isDigit(current):
      start = i
      while i < len(input) and isDigit(input[i]):
        i += 1
      num = input[start:i]
      if isLiteral(num):
        tokens.append(num)
      else:
        raise Exception(f"Invalid literal {num}")
    elif isOperator(current):
      tokens.append(current)
      i += 1
    elif current in '()':
      tokens.append(current)
      i += 1
    elif current == ';':
      i += 1
      if i < len(input):
        raise Exception(f"Missing semicolon {i} < {len(input)}")
    else:
      raise Exception(f"Invalid syntax with line {input} at index {i}: {current}")
  
  return tokens