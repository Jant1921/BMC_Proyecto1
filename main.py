
import sys
import webapp

# Check Python version, abort for Python 2
if sys.version_info[0] != 3:
    print("Only Python 3.x is supported. Your current Python version is {0}".format(sys.version))
    sys.exit(0)

if __name__ == "__main__":
    webapp.start_web_server()