import sys
def hello(name):
	return "hello " + name

def main():
	if len(sys.argv) is 1:
		print("Incorrect format used.\nCorrect format is: Python3 CI_Practice.py name_here ")

	elif(sys.argv[1] in ("backwards","backward","reverse")):
		print(hello(" ".join(str(x) for x in sys.argv[:0:-1])))

	else:
		print(hello(" ".join(str(x) for x in sys.argv[1:])))

def test_hello():
	assert hello("bob") == "hello bob"



if __name__ == "__main__":
    main()