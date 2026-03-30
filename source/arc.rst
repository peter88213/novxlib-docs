=============
The <ARC> tag
=============

.. admonition:: <ARC>
   
   Purpose
      Defines a plot line.

   Attributes
      - `id <#the-id-attribute>`__
      - `color <#the-color-attribute>`__

   Content
      - `Title <title.html>`__
      - `Desc <desc.html>`__
      - `Link <link.html>`__
      - `Notes <notes.html>`__
      - `ShortName <shortname.html>`__
      - `Sections <sections.html>`__
      - `POINT <point.html>`__

The id attribute
----------------

This attribute is required. The plot line ID consists of the
plot line prefix **ac** and a number.

Example: ``ac13``

The color attribute
-------------------

This attribute is optional.
The color is specified according to the tkinter conventions,
either as hexadecimal RGB value, or as color name.

Examples: ``#FFFFFF``, ``red``

