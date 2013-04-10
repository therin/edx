def checkio(number):
  tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  result = ''

  if number % 100 < 20:
    result = nums[number % 100]
    number /= 100
  else:
    result = nums[number % 10]
    number /= 10

    result = tens[number % 10] + '' + result
    number /= 10

  if number is 0:
    return result.strip()

  if number > 7:
    return nums[number] + ' hundred ' + result
  else:
    return nums[number] + ' hundred ' + result

print checkio(4) + "'"
print checkio(133) + "'"
print checkio(12) + "'"
print checkio(101) + "'"
print checkio(212) + "'"
print checkio(40) + "'"
print checkio(380) + "'"
print checkio(100) + "'"
print checkio(784) + "'"