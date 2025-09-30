==============
The <span> tag
==============

.. admonition:: <span>
   
   Purpose
      Defines a text area that is not in the document language.

   Attributes
      - `xml:lang <#the-xml-lang-attribute>`__

   Content
      - `em <em.html>`__
      - `strong <strong.html>`__
      - `comment <comment.html>`__
      - `note <note.html>`__
      - Plain Text 

The span is within a paragraph. Whole paragraphs in another language
than the document language get the

The xml:lang attribute
----------------------

The required locale is for ODF document spell check control.

The attribute has the form ``<Language code>`` or
``<Language code>-<Country code>``,
where the language code is according to ISO 639-1,
and the optional country code is according to ISO 3166-2.

Example: ``en-GB`` is for British English.
