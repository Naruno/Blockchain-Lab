0.4.0-alpha Release Notes
====================

In this minor version, added some features and control points.

Please report bugs using the issue tracker at GitHub:

  <https://github.com/Decentra-Network/Blockchain-Lab/issues>

Compatibility
==============

There have been no compatibility changes.

Notable changes
===============

## Path to Blockchain Lab

With this release you can set a path for your blockchain lab,
please read readme.md for instruction.

0.4.0-alpha change log
=================

### Blockchain Lab
- Staticmethod removed from create and delete function. 
- Added change and return workdir for path argument.
- Added linux system control point to create_local function.
- Added linux system control point to delete_local function.
- Added argument based function named:
  - blockchain_lab_create_docker
  - blockchain_lab_create_local
  - blockchain_lab_delete_docker
  - blockchain_lab_delete_local

### Readme
- Added path instruction for create and delete function.

### Setup
- Some console_scripts changed with argument based functions

Credits
=======

Thanks to everyone who directly contributed to this release:

- Onur Atakan ULUSOY
