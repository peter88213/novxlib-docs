==============
The <novx> tag
==============


.. admonition:: <novx>
   
   Purpose
      Identify the file type.
   
   Attributes   
      - version
      - xml:lang
   
   Contains
       - `PROJECT <project.html>`__
   
The version attribute
---------------------

The Version number is for compatibility check.
It consists of the major version number,
and the minor version number, separated by a decimal point.
When reading a novx file, NovxFile.read() checks the major and
minor version numbers against its built-in reference version number.

- The major version number must match the internal reference.
- The minor version number must be equal or less then the reference.

The xml:lang attribute
----------------------

The locale is for ODF document spell check control.