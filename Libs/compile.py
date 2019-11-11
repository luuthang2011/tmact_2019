from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("feature2geodatabase", ["feature2geodatabase.py"]),
    Extension("updateDataSource", ["updateDataSource.py"]),
    Extension("publish_mapService_from_mapDocument", ["publish_mapService_from_mapDocument.py"]),
    Extension("listing_layer", ["listing_layer.py"]),
    Extension("flowProcess",  ["flowProcess.py"]),
    Extension("SQLServer", ["SQLServer.py"]),
    Extension("PostgresServer", ["PostgresServer.py"]),
    Extension("rabbitmq", ["rabbitmq.py"]),
    Extension("delete", ["delete.py"]),
    #   ... all your modules that need be compiled ...
]
setup(
    name='tmact2019',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)