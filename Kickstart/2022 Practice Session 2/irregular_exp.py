import re


def main():
  # Get the number of test cases
  num_tests = int(input())

  matcher = re.compile(r"(.*[aiueo]+.*[aiueo]+.*).*[aiueo]+.*\1")

  for t in range(num_tests):
    # Get the Witch's expression
    expression = input()
    answer = 'Nothing.'
    if(matcher.match(expression)):
      answer = 'Spell!'
    print(f'Case #{t+1}: {answer}')

if __name__ == '__main__':
  main()
