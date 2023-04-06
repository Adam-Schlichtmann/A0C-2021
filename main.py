import os
import sys 

class colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'



if (len(sys.argv) != 2):
  print(f"{colors.FAIL}Invalid options.\n{colors.WARNING}Usage:`python3 main.py [day]`")
  exit(0)


os.system("cd src/day{:02d} && python3 main.py".format(int(sys.argv[1])))

