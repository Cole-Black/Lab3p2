
def sum_n(n):
  if n == 0:
    return n 
  return n + sum_n(n-1)

def print_n(str, n):
  if n == 0:
    return
  print(f"{str}")
  print_n(str, n - 1)

def run():
  nIN = int(input("Enter an int: "))
  print(f"sum is {sum_n(nIN)}.")

  str = input("Enter a string: ")
  print_n(str, nIN)

if __name__ == "__main__":
  run()