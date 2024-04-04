# Mean-Variance-Standard Deviation Calculator

This is a fork and has implementation for calculating Men, Variance and Standard deviation values from series of values in a list. 

The boiler plate is located here: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

The requirement for implemantation is located here: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

note(s)
1. As of 2024-04-04, the test_module.py needs updating. The assertAlmostEqual is returning error when parsing a dictionary of list of values.
======================================================================
ERROR: test_calculate (test_module.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-mean-variance-standard-deviation-calculator/test_module.py", line 10, in test_calculate
    self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")
  File "/home/gitpod/.pyenv/versions/3.8.19/lib/python3.8/unittest/case.py", line 943, in assertAlmostEqual
    diff = abs(first - second)
TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
