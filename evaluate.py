from tokenizer import isIdentifier

def toPostfix(tokens):
  output = []
  operators = []
  precedence = {'NEG': 3, '*': 2, '/': 2, '+': 1, '-': 1}
  associativity = {'NEG': 'R', '*': 'L', '/': 'L', '+': 'L', '-': 'L'}

  prev_token = None
  
  for token in tokens:
    if token.isdigit() or isIdentifier(token):
      output.append(token)
      prev_token = 'number'
    elif token == '-' and (prev_token is None or prev_token in ('operator', '(',)):
      # This is a unary minus
      while (operators and precedence.get(operators[-1], 0) > precedence['NEG']):
          output.append(operators.pop())
      operators.append('NEG')
      prev_token = 'operator'
    elif token in ('+', '-', '*'):
      while (operators and operators[-1] != '(' and
          (precedence[operators[-1]] > precedence[token] or
          (precedence[operators[-1]] == precedence[token] and associativity[token] == 'L'))):
        output.append(operators.pop())
      operators.append(token)
      prev_token = 'operator'
    elif token == '(':
      operators.append(token)
      prev_token = '('
    elif token == ')':
      while operators and operators[-1] != '(':
          output.append(operators.pop())
      if not operators or operators[-1] != '(':
          raise ValueError("Mismatched parentheses")
      operators.pop()
      prev_token = 'number'
    else:
      raise ValueError(f"Unknown token: {token}")

  #print(operators)
  while operators:
    op = operators.pop()
    if op == '(':
      raise ValueError("Mismatched Parentheses")
    output.append(op)
  
  return output

def evaluateExpression(tokens, variables):
  stack = []
  #print(f"Evaluating Tokens {tokens}")
  tokens = toPostfix(tokens)
  #print(f"Postfix Tokens: {tokens}")
  if not tokens:
    raise Exception(f"Empty expression")

  for token in tokens:
    #print(f"evaluating {token}")
    if token.isdigit():
      stack.append(int(token))
    elif token in variables:
      stack.append(variables[token])
    elif token == 'NEG':
      a = stack.pop()
      stack.append(-a)
    elif token in ('+', '-', '*'):
      b = stack.pop()
      a = stack.pop()
      if token == '+':
          stack.append(a + b)
      elif token == '-':
          stack.append(a - b)
      elif token == '*':
          stack.append(a * b)
    else:
      raise Exception(f"Variable not defined: {token}")

  return stack[0]