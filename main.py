if __name__ == "__main__":
  def print_and_true():
    print("I got called")
    return True

  def print_and_return(x):
    print(f"I am returning {x}")
    return x

  print(True)
  print(type(True))

  print(False)
  print(type(False))

  a_true_alias = True
  print(a_true_alias)

  print(f"True == 1: {True == 1}")
  print(f"False == 0: {False == 0}")
  print(f"True + (False / True): {True + (False / True)}")

  poem = """\
  He took his vorpal sword in hand;
    Long time the manxome for he sought-
  So rested he by the Tumtum tree
    And stood awhile in thought.\
  """
  lines = poem.splitlines()
  sum = sum("the" in line.lower() for line in lines) / len(lines)
  print(poem)
  print(lines)
  print(sum)

  print(not True)
  print(not False)

  print(not print_and_true())

  print(True and print_and_return(True))
  print(True and print_and_return(False))
  print(False and print_and_return(True))
  print(False and print_and_return(False))

  print(True or print_and_true())
  print(False or print_and_true())

  print(1 == 1)
  print(1 == 1.0)
  print(1 == 2)
  print(1 != 2)
  print(1 != (1 + 0.0))

  print(1 <= 1)
  print(1 < 1)
  print(2 > 3)
  print(2 >= 2)

  x = []
  y = []
  print(x is x)
  print(x is not x)
  print(x is y)
  print(x is not y)

  small_even = [2, 4]
  print(1 in small_even)
  print(2 in small_even)
  print(10 in small_even)

  string = "hello beautiful world"
  print("e" in string)
  print("x" in string)
  print("beautiful" in string)
  print("belle" in string)

  print(1 < 2 < 3)
  print(1 < 2 and 2 < 3)
  print(1 < 3 < 2)
  print(1 < 3 and 3 < 2)
  print(1 < 2 < 1)
  print(1 == 1.0 < 0.5)
  print(1 == 1.0 == True)
  print(1 < 3 > 2)
  print(1 < 2 < 3 < 4 < 5)
  print(3 < 2 < "2")    # returns Flase
                        # does not raise exception, because 2 < 3 return False, so 2 < "2" does not evaluated
  print(3 < 2 < (1//0)) # returns Flase

  def foo():
    print("I'm foo")
    return 1
  print(0 < foo() < 2)
  print((0 < foo()) and (foo() < 2))

  hours_worked = 5
  print(1 <= hours_worked <= 25)

  a = 0
  print(a is a < 1)
  print((a is a) < 1)
  print(a is (a < 1))
  print(a is a)
  print(True == 1)
  print((a is a) < 1)

  print(bool(None))

  def add_num_and_len(num, things = None):
    return num + len(things or [])
  print(add_num_and_len(5, [1, 2, 3]))
  print(add_num_and_len(6))

  print(bool(3))
  print(bool(-5))
  print(bool(0))

  import math
  print([bool(x) for x in [0, 1.2, 0.5, math.inf, math.nan]])
  print(bool(0.1 + 0.2 + (-0.2) + (-0.1)))

  import fractions
  print(bool(fractions.Fraction("1/2")))
  print(bool(fractions.Fraction("0/1")))

  print(bool([1]))
  print(bool([]))

  print(bool((1, 2)))
  print(bool(()))

  print(bool({1, 2, 3}))
  print(bool({}))

  print(bool({1: 2}))
  print(bool({}))

  print(bool("hello"))
  print(bool(""))

  print(bool(b"xyz"))
  print(bool(b""))

  def func():
    pass
  print(bool(func))

  import datetime
  def before_noon():
    return datetime.datetime.now().hour < 12

  def greet():
    if before_noon:
      print("Good morning")
    else:
      print("Good evening!")
  greet()

  class Dummy:
    pass
  print(bool(Dummy()))

  class BoolLike:
    am_i_truthy = False
    def __bool__(self):
      return self.am_i_truthy
  bool_like = BoolLike()
  print(bool(bool_like))
  bool_like.am_i_truthy = True
  print(bool(bool_like))

  class DummyContainer:
    my_len = 0
    def __len__(self):
      return self.my_len
  dummy_container = DummyContainer()
  print(bool(dummy_container))
  dummy_container.my_len = 5
  print(bool(dummy_container))

  class AlwaysTrue:
    def __bool__(self):
      return True
  print(bool(AlwaysTrue()))

  class AlwaysFalse:
    def __bool__(self):
      return False
  print(bool(AlwaysFalse()))

  class BooleanContainer:
    def __len__(self):
      return 100

    def __bool__(self):
      return False

  boolean_container = BooleanContainer()
  print(len(boolean_container))
  print(bool(boolean_container))

  from numpy import array
  import textwrap

  x = array([0])
  print(len(x))
  print(bool(x))

  y = array([0, 1])
  try:
    bool(y)
  except ValueError as exc:
    print("\n".join(textwrap.wrap(str(exc))))

  print(bool(array([])))

  print(not 1)
  print(not 0)

  print(1 and 2)
  print(0 and 1)
  print(1 or 2)
  print(0 or 2)

  def summarize(long_text) -> str:
    if len(long_text) <= 4:
      return long_text

    return long_text[:2] + "..." + long_text[-2:]
  print(summarize("hello world"))
  print(summarize("hi"))
  print(summarize(""))
  for a in ["hello world", "hi", "", None]:
    print("-->", summarize(a or ""))

  print(all([1, 2, 3]))
  print(all([0, 1, 2]))
  print(all(x / (x - 1) for x in [0, 1]))

  print(any([1, 0, 0]))
  print(any([False, 0, 0.0]))
