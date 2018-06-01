"""
Usage:
  1.py init_instance [--configSvr] [--replname] [--port=<port>]
  1.py serial <port> [--baud=9600] [--timeout=<seconds>]
  1.py -h | --help | --version
Options:
  --port=<port>   self port
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    print(arguments)