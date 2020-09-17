



def sum_n(n):
  if n == 0:
    return n 
  return n + sum_n(n-1)

def print_n(s, n):
  if n == 0:
    return
  print(f"{s}")
  print_n(s, n - 1)

def run():
  nIN = int(input("Enter an int: "))
  print(f"sum is {sum_n(nIN)}.")

  sIN = input("Enter a string: ")
  print_n(sIN, nIN)


if __name__ == "__main__":
  run()