import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


setup(name='guestbook',
      packages=find_packages(),
      author='hirokiky',
      author_email='hirokiky@gmail.com',
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'paste.app_factory': ['main=uiro:main'],
      },
      install_requires=[
          'uiro',
          'deform==2.0a2',
      ],
      )
