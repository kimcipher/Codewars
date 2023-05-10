duplicateCount = (input) ->
  # Convert the input string to lowercase for case-insensitive comparison
  input = input.toLowerCase()
  
  # Create an empty object to store the count of each character
  counts = {}
  
  # Loop through each character in the input string
  for char in input
    # If the character has already been counted, increment its count
    if counts[char]?
      counts[char]++
    # Otherwise, add it to the counts object with a count of 1
    else
      counts[char] = 1
  
  # Loop through the counts object and count the number of characters that occur more than once
  duplicates = 0
  for char, count of counts
    if count > 1
      duplicates++
  
  # Return the number of duplicates
  duplicates
