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

The attribute has the form ``<Language code>`` or
``<Language code>-<Country code>``,
where the language code is according to ISO 639-1,
and the optional country code is according to ISO 3166-2.

Example: ``en-GB`` is for British English.

- If the *xml:lang* attribute is not set, the system locale is used.
- If the *xml:lang* attribute does not look plausible,
  it is replaced with *zxx*,
  which means "no linguistic information at all".
