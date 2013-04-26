=======
 pdbcs
=======

pdb for setuptools console scripts

Using
=====

A console script installed by setuptools is a thin wrapper that loads
the defined entry point and invokes it. pdbcs uses the console script
name to load the entry point itself and invoke the debugger. The
debugger automatically stops on the first line of the main function of
the console script.

::

  $ pdbcs /Users/dhellmann/Envs/pdbcs/bin/pdbcs
  > /Users/dhellmann/Devel/pdbcs/pdbcs/pdbcs/main.py(11)main()
  -> parser = argparse.ArgumentParser()
  (Pdb)
