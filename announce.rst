===========
 pdbcs 0.3
===========

.. tags:: pdbcs release python

What is pdbcs?
==============

A console script installed by setuptools is a thin wrapper that loads
the defined entry point and invokes it. pdbcs uses the console script
name to load the entry point itself and invoke the debugger. The
debugger automatically stops on the first line of the main function of
the console script.

What's New?
===========

- Support command line arguments to the script being
  debugged. (Contributed by Dan Mick)

See https://pypi.python.org/pypi/pdbcs for details.
