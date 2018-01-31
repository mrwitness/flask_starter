
#!/bin/bash
import os
import sys
#from subprocess import process
from subprocess import *

# wrapper sh code,return stdout string
def sh_wrapper_string(args):
	if not args or len(args) == 0:
		return ""
	
	ret = ""
	process = Popen(args, stdout=PIPE, stderr=STDOUT)
	while True:
        	out = process.stdout.read(1)
        	if out == '' and process.poll() != None:
            		break
	        if out != '':
			ret = ret + out
    	return ret

