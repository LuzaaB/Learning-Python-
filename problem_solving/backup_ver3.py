# version 3

import os
import time

# 1.
source = [r'D:\\Specimen Paper']

# 2.
target_dir = 'E:\\Backup'

#
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3.
# 4.
today = target_dir + os.sep + time.strftime('%Y%m%d')
#
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
#check if the comment was entered
if len(comment) == 0 :
    target = today + os.sep + now + '.zip'
else :
    target = today + os.sep + now + comment.replace(' ','_') + '.zip'
    
#
if not os.path.exists(today) :
    os.mkdir(today)
    print('Successfully creates directory',today)

# 5.
zip_command = f'zip -r {target} {' '.join(source)}'

# Run the backup
print('Zip command is ')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0 :
    print('Successful backup to ', target)
else :
    print('Backup Failed')