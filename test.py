import re 
pattern=r'\d{10}$'
id='1115331975'
if re.match(pattern,id):
    print('True')
else:
    print('False')