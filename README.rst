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
