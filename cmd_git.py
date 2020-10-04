import os
from datetime import datetime

# Commit comment
now = datetime.now()
comment = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

# Push
os.system('git add .')
os.system('git commit -am "Regular update"')
os.system('git push')
