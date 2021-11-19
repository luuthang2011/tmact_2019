from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("SQLServer", ["SQLServer.py"]),
    Extension("rabbitmq", ["rabbitmq.py"]),
    #   ... all your modules that need be compiled ...
]
setup(
    name='tmact2019',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)