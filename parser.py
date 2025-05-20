import tokenizer
import evaluate

class Parser:
  def __init__(self, line, variables):
    list_of_tokens = tokenizer.tokenize(line)

    if len(list_of_tokens) <= 2:
      raise Exception(f"Syntax error")
    else:
      self.var = list_of_tokens[0]
      equation = list_of_tokens[2:]
      self.result = evaluate.evaluateExpression(equation, variables)
    
  def __str__(self):
    return f"{self.var} = {self.result}"
