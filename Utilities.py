import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

def batches(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


class smart_dict(dict):
    def __missing__(self, key):
        return key