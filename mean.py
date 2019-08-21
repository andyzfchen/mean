def mean(num_list):
  assert isinstance(num_list, list)
  try:
    return sum(num_list)/len(num_list)
  except ZeroDivisionError:
    return 0
  except TypeError as detail:
    msg = "Please provide a list of numbers."
    raise TypeError(detail.__str__() + "\n" + msg)
