import logging
import pandas
import sys

logging.basicConfig(level=logging.DEBUG)

assert(sys.version[0] == "3")
assert(pandas.__version__ == "1.0.3")
logging.info(" Perfect your environment is ok")
