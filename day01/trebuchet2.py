values = 0
while True:
    try:
      inp = input()
      if inp == '-':
          break
      else:
          numbers = "0123456789"
          othernums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
          nums = []
          for i, num in enumerate(inp):
              if num in numbers:
                  nums.append(num)
              else:
                  for j, othernum in enumerate(othernums):
                      if inp[i:i+len(othernum)] == othernum:
                          nums.append(str(j + 1))  
                          break
          print(nums, int(nums[0] + nums[-1]))
          values += int(nums[0] + nums[-1])
    except EOFError:
        break

print(values)