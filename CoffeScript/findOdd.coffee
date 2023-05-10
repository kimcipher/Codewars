findOdd = (arr) ->
  # Create an empty object to store the count of each integer
  counts = {}
  
  # Loop through each integer in the array
  for num in arr
    # If the integer has already been counted, increment its count
    if counts[num]?
      counts[num]++
    # Otherwise, add it to the counts object with a count of 1
    else
      counts[num] = 1
  
  # Loop through the counts object and find the integer with an odd count
  for num, count of counts
    if count % 2 == 1
      return parseInt(num)
