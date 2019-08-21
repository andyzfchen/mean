from mean import *

def test_ints():
  num_list = [4,3,52,9]
  obs = mean(num_list)
  exp = 17
  assert obs == exp

def test_zero():
  num_list = [2,0,7]
  obs = mean(num_list)
  exp = 3
  assert obs == exp

def test_neg():
  num_list = [-3,0,6]
  obs = mean(num_list)
  exp = 2
  assert obs == exp

