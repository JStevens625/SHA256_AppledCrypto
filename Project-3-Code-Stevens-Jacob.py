# Student Name: Jacob Stevens Student ID: U0000002672
# Imports just the SHA 256 function for use in project
from hashlib import sha256 as sha

def main():
	# Calls the two files that were given in canvas and reads them
	readhello = open("Hello.txt","r")
	readanarchy = open("anarchism.txt","r")

	# Reads the contents of each file as text.
	hellocontents = readhello.read()
	anarchycontents = readanarchy.read()

	# The SHA256 is now accessed in order to encode it to SHA and call hexdigest to concatenate the data fed so far
	hellosha = sha(hellocontents.encode()).hexdigest().upper()
	anarchysha = sha(anarchycontents.encode()).hexdigest().upper()

	# Prints the files contents and then the SHA256 form of each files contents
	print("Hello World File Contents: \n" + hellocontents + "\nSHA256 Hash Value: \n" + hellosha + "\n\n")
	print("Anarchy File Contents: \n" + anarchycontents + "\nSHA256 Hash Value: \n" + anarchysha)

	# Closes files as not to continually waste memory and leaving files open accidently for corruption
	readhello.close()
	readanarchy.close()
main()
