from test import *

from timeit import timeit
def main():
  execution_time=timeit(stmt='runTestScript()', globals=globals(), number=1)
  print(f"Execution time is {execution_time / 1} seconds")
if __name__ == "__main__":
    main()
