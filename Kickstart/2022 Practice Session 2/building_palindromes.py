def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    N, Q = map(int, input().split())
    blocks = input()
    questions = []
    for i in range(Q):
      L, R = map(int, input().split())
      questions.append((L, R))

    answer = count_yes(N, Q, blocks, questions)

    print(f'Case #{test_case}: {answer}')


def count_yes(N, Q, blocks, questions):
  yes_answers = 0
  mem = {}
  for question in questions:
    substr = blocks[question[0] - 1:question[1]]
    if is_palindrome_possible(substr, mem):
      yes_answers += 1
  return yes_answers

def is_palindrome_possible(substr, mem):
  if substr in mem:
    return mem[substr]

  count_dict = {}
  for char in substr:
    if char not in count_dict:
      count_dict[char] = 1
    else:
      count_dict[char] += 1

  occ = list(count_dict.values())
  i = 0
  chance = 1
  while i < len(occ) and chance >= 0:
    if occ[i] % 2 != 0:
      chance -= 1
    i += 1
  
  if chance >= 0:
    mem[substr] = True
  else:
    mem[substr] = False

  return mem[substr]

if __name__ == '__main__':
  main()
