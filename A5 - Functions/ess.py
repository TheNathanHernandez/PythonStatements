def ask(prompt):
    response = input(prompt+" ")
    
    try:
        return int(response)
    except ValueError:
        pass
 
    try:
        return float(response)
    except ValueError:
        pass
 
    return response
    
  