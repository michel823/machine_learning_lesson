from setuptools import setup, find_packages
import liu_ml_pkg

setup(
    name = 'liu_ml_pkg',
    version = liu_ml_pkg.__version__, 
    author = 'liu_sulan',
    packages = find_packages(),
    include_package_data=True,
    install_requires=['pandas'],
    tests_require=['pandas','liu_ml_pkg']
)
