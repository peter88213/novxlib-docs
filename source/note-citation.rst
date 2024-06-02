=======================
The <note-citation> tag
=======================

.. admonition:: <note-citation>
   
   Purpose
      Defines a marker for a footnote or endnote.


This will be a marker in the body text of the exported
ODT manuscript, linking to the footnote or endnote.

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

