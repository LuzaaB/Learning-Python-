# version 2

import os 
import time

# 1.
source = [r'D:\\Specimen Papers']

# 2.
target_dir = 'E:\\Backup'

if not os.path.exists(target_dir) :
    os.mkdir(target_dir)

# 3.
# 4. The current day is the name of the subdirectory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# the name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today) :
    os.mkdir(today)
    print('Successfully created directory', today)

# 5.
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Run the backup
print('Zip command is : ')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0 :
    print('Successful backup to', target)
else :
    print('Backup Failed')