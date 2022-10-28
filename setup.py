from setuptools import setup

setup(name='BookLover',
      version='0.1.0',
      description='A simple python class that determines a book lover from non-booklover.',
      url='https://github.com/brooksideas/book-lover',
      author='Brook Tarekegn Assefa',
      author_email='brooksideas@gmail.com',
      license='MIT',
      packages=['booklover', 'booklover_test'],
      install_requires=["pandas"])
