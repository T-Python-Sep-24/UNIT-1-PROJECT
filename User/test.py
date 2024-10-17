import re
password:str='05914a45281'
pattern=r'^05\d{8}$'
if re.match(pattern,password):
    print("true")
else:
    print("false")
