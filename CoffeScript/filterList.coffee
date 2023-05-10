filter_list = (lst) ->
  # Create an empty array to store the filtered integers
  filtered = []
  
  # Loop through each element in the input list
  for elem in lst
    # Check if the element is an integer using the `typeof` operator
    if typeof elem == 'number'
      # If the element is an integer, add it to the filtered array
      filtered.push(elem)
  
  # Return the filtered array
  return filtered
