# version 4

import os
import time

# 1.
source = [r'D:\\Specimen Paper']

# 2.
target_dir = 'E:\\Backup'

if not os.path.exists(target_dir) :
    os.mkdir(target_dir)

# 3.
# 4.
today = target_dir + os.sep + time.strftime('%Y%m%d')
#
now = time.strftime('%H%M%S')

#
comment = input('Enter comment --> ')
#
if len(comment) ==0 :
    target = today + os.sep + now + '.zip'
else :
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
    
#
if not os.path.exists(today) :
    os.mkdir(today)
    print('Successfully created directory', today)

# 5.
zip_command = f'zip -r {target} {' '.join(source)}'

# Run the backup
print('Zip command is :')
print(zip_command)
print('Running :')
if os.system(zip_command) == 0 :
    print('Successful backup to', target)
else :
    print('Backup Failed')