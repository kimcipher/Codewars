createPhoneNumber = (numbers) ->
  # Join the array of numbers into a string
  phone_number = numbers.join('')
  # Use string interpolation to format the phone number
  "(#{phone_number.substr(0, 3)}) #{phone_number.substr(3, 3)}-#{phone_number.substr(6)}"
