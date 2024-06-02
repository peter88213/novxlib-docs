==============
The <note> tag
==============

.. admonition:: <note>
   
   Purpose
      Defines a footnote or endnote in the section content.

   Attributes
      - `id <#the-id-attribute>`__
      - `class <#the-class-attribute>`__

   Content
      - `note-citation <note-citation.html>`__
      - `p <p.html>`__


This will be a footnote or an endnote in the exported
ODT manuscript.

Example:

.. code-block:: xml

   Achteraus<note id="ftn1" class="footnote">
   <note-citation>1</note-citation>
   <p>Hinter dem Boot</p>
   </note>, hoch oben über dem Boot, blinkten die roten
   Lichter des Offshore-Windparks<note id="ftn0" class="endnote">
   <note-citation>i</note-citation>
   <p>Der Windpark "Schlicktown IV" wurde 2030 in den
   überfluteten Gebieten nahe Bremerhaven errichtet.</p>
   </note> am mondlosen Himmel.


The id attribute
----------------

This attribute is required. The note ID consists of the
ODT footnote prefix **ftn** and a number.

Example: ``ftn13``


The class attribute
-------------------

This attribute is required.

- footnote: The note is a footnote.
- endnote: The note is an endnote.


