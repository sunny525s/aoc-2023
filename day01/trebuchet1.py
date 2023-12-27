# calibration value can be found by combining first and last digit for single two-digit number
sum = 0
while True:
  try: 
    inp = input()
    if inp == '-':
      break
    else:
      numbers = "0123456789"
      nums = []
      for i in inp:
        if i in numbers:
          nums.append(i)
      sum += int(nums[0] + nums[-1])
  except EOFError:
    break

print(sum)