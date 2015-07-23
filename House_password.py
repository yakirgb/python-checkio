import re
checkio= lambda x: re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}',x)
