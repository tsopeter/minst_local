import pickle as cPickle
import gzip
import numpy as np

class mnist_local:
    def __init__(self, dir='data/mnist.pkl.gz'):
        self._filename=dir

    def raw_data(self):
        f = gzip.open(self._filename, 'rb')

        upick_d = cPickle._Unpickler(f)
        upick_d.encoding = 'latin1'

        train, valid, test = upick_d.load()
        f.close()
        return (train, valid, test)