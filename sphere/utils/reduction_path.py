from pathlib import Path


class ReductionPath(object):
    '''
    Reduction path class

    Provides easy access to all the path components of a reduction.
    '''

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, path):
        self._root = Path(path).expanduser()

        # update all subpaths
        self._raw      = self._root / 'raw'
        self._calib    = self._root / 'calib'
        self._sof      = self._root / 'sof'
        self._tmp      = self._root / 'tmp'
        self._preproc  = self._root / 'preproc'
        self._products = self._root / 'products'

    ##################################################
    # Representation
    ##################################################

    def __repr__(self):
        return str(self._root)

    ##################################################
    # Properties
    ##################################################

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, path):
        self._root = Path(path).expanduser()

        # update all subpaths
        self._raw      = self._root / 'raw'
        self._calib    = self._root / 'calib'
        self._sof      = self._root / 'sof'
        self._tmp      = self._root / 'tmp'
        self._preproc  = self._root / 'preproc'
        self._products = self._root / 'products'

    @property
    def raw(self):
        # create sub-directory if needed
        if not self._raw.exists():
            self._raw.mkdir(exist_ok=True)

        return self._raw

    @property
    def calib(self):
        # create sub-directory if needed
        if not self._calib.exists():
            self._calib.mkdir(exist_ok=True)

        return self._calib

    @property
    def sof(self):
        # create sub-directory if needed
        if not self._sof.exists():
            self._sof.mkdir(exist_ok=True)
            
        return self._sof

    @property
    def tmp(self):
        # create sub-directory if needed
        if not self._tmp.exists():
            self._tmp.mkdir(exist_ok=True)

        return self._tmp

    @property
    def preproc(self):
        # create sub-directory if needed
        if not self._preproc.exists():
            self._preproc.mkdir(exist_ok=True)
            
        return self._preproc

    @property
    def products(self):
        # create sub-directory if needed
        if not self._products.exists():
            self._products.mkdir(exist_ok=True)
            
        return self._products
