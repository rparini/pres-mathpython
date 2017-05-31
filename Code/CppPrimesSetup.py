# Compile CppPrimes_caller.pyx -> CppPrimes_caller.cpp -> CppPrimes_caller.so
# python CppPrimesSetup.py build_ext --inplace -f

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

setup(
	name = 'CppPrimes',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("CppPrimes_caller", ["CppPrimes_caller.pyx"], language = "c++", include_dirs = [np.get_include()])]
)
