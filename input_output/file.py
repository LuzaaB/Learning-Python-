# file class
poem = '''\
    Programming is fun 
    When the work is done
    If you wanna make your work fun
        use python
    '''
# Open for writing - "w" for writing mode (default mode, use 'wt' for text mode, use 'wb' for binary mode)
f = open("poem.txt", "w")
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified then read mode is assumed by default
f = open("poem.txt")
while True :
    line = f.readline()
    # Zero length indicates EOF (End of File)
    if len(line) == 0 :
        break
    # The 'line' already has a new line at the end of each line since it is reading from a file
    print(line, end='')
# Close the file
f.close()