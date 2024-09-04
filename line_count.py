def line_count():
  
  try:
    file = open('file.txt', 'r')
  # opens the file up and reads it
  
  except FileNotFoundError:
    print ('not found')
    return 0
  # if the file is not found, it will post as "not found"
  
  else:
    lne = 0
    for x in file:
      lne += 1
  # if there is a file, it counts how many lines there are starting from 0
  
  return lne
  # returns the result