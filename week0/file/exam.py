from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
for a in LETTERS:
    for b in LETTERS:    
        find_me = a + b
        secret_password = find_me + 'bcmpda'
        result = unzip_with_7z(zip_file_path, dest_path, secret_password)
        if result == True:    
            print(f'Password found: {secret_password}')
            break
        else:
            continue
    if result == True:    
        break
    else:
        continue