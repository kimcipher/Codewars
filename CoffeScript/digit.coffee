squareDigits = (num) ->
  # Convert the number to a string
  numStr = num.toString()
  result = ""
  
  # Loop through each digit in the string
  for i in [0...numStr.length]
    # Convert the digit to a number and square it
    digit = parseInt(numStr[i])
    square = digit * digit
    
    # Append the squared digit to the result string
    result += square.toString()
  
  # Convert the result string back to a number and return it
  parseInt(result)
