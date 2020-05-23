import pandas
import sys

from setting import logger

assert(sys.version[0] == "3")
assert(pandas.__version__ == "1.0.3")
logger.info(" Perfect your environment is ok")
