==============
The <novx> tag
==============

.. admonition:: <novx>
   
   Purpose
      Encloses the whole *novelibre* project.

   Attributes
      - `version <#the-version-attribute>`__
      - `xml:lang <#the-xml-lang-attribute>`__

   Content
      - `PROJECT <project.html>`__
      - `CHAPTERS <chapters.html>`__
      - `CHARACTERS <characters.html>`__
      - `LOCATIONS <locations.html>`__
      - `ITEMS <items.html>`__
      - `ARCS <arcs.html>`__
      - `PROJECTNOTES <projectnotes.html>`__
      - `PROGRESS <progress.html>`__

The version attribute
---------------------

The fixed Version number is for compatibility check.
It consists of the major version number,
and the minor version number, separated by a decimal point.
When reading a novx file, NovxFile.read() checks the major and
minor version numbers against its built-in reference version number.

- The major version number must match the internal reference.
- The minor version number must be equal or less then the reference.

The xml:lang attribute
----------------------

The optional locale is for ODF document spell check control.
