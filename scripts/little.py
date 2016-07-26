# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# By: 	    Offset
# Greatz:   RATF, Ninja
# Version:  1.0
# Description: This script invert the hexadecimal addres to little endian.

import sys
import os
import platform

clear = "clear"
if platform.system() == "Windows":
    clear = "cls"
os.system(str(clear))


def usage():
	print "[NO]-Fail!\n"
	print "Usage: "+sys.argv[0]+" 0x12345678\n"
	exit()

def main() :
	print " _____ _              ___      _                     _____                     "
	print "/__   \ |__   ___    / __\   _| |__   ___ _ __ ___  /__   \___  __ _ _ __ ___  "
	print "  / /\/ '_ \ / _ \  / / | | | | '_ \ / _ \ '__/ __|   / /\/ _ \/ _` | '_ ` _ \ "
	print " / /  | | | |  __/ / /__| |_| | |_) |  __/ |  \__ \  / / |  __/ (_| | | | | | |"
	print " \/   |_| |_|\___| \____/\__, |_.__/ \___|_|  |___/  \/   \___|\__,_|_| |_| |_|"
	print "                         |___/                                                 "

	try:
		if len(sys.argv[1]) < 8:
			usage()
		else:
			endereco = sys.argv[1]
			teste = []
			i = 0
			temp = ""
			for j in endereco:
				temp += j
				if i == 0:
					i=1
				else:
					i=0
					teste.append(temp)
					temp = ""	


			out = ""
			for i in teste[::-1]:
				if i!="0x":
					out+="\\x"+i 
			
			print "[OK]-Done!"
			print "\nHexadecimal  : "+sys.argv[1]
			print "Little Endian: "+out+"\n"
	except:
		pass


if __name__ == "__main__":
	main()