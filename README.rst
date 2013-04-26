=======
 pdbcs
=======

pdb for setuptools console scripts

Using
=====

A console script installed by setuptools is a thin wrapper that loads
the defined entry point and invokes it. pdbcs uses the console script
name to load the entry point itself and invoke the debugger.

::

  $ pdbcs /full/path/to/console-script
  (pdb) 
