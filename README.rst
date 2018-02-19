|package-version| |python-compat| |travis-build| |appveyor-build| |license-apache|


hdrpy
=====

``hdrpy`` is a pure\* Python implementation of HDR histograms.
Compatible with Python 2.7 and Python 3.5+.

\*: Well, if you not count numpy.



Technically, it can be considered a fork of
`hdrhistogram <https://github.com/HdrHistogram/HdrHistogram_py/>`__ with
C extension removed. The motivation for that was that deploying C-based
Python extensions is a bit tough, when there's a lot of platforms
involved.




.. |python-compat| image:: https://img.shields.io/pypi/pyversions/hdrpy.svg
.. |package-version| image:: https://img.shields.io/pypi/v/hdrpy.svg
.. |travis-build| image:: https://img.shields.io/travis/dmand/hdrpy.svg
.. |appbeyor-build| image:: https://img.shields.io/appveyor/ci/dmand/hdrpy.svg
.. |license-apache| image:: https://img.shields.io/pypi/l/hdrpy.svg
   :trim:
