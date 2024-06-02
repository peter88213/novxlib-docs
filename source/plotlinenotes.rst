=======================
The <PlotlineNotes> tag
=======================

.. admonition:: <PlotlineNotes>
   
   Purpose
      Defines plot line notes of a section. 

   Attributes
      - `id <#the-id-attribute>`__

   Content
      - `p <p.html>`__

Plot line notes are entered in the section's "Plot" area in *novelibre*.
The plot line notes describe how a section contributes to
the plot line identified by the **id** attribute.
They are optional and consist of one or more paragraphs.
Highlighting or other formatting is not supported.


Example:

.. code-block:: xml

   <PlotlineNotes id="ac2">
      <p>The gun is on the wall.</p>
   </PlotlineNotes>


The id attribute
----------------

This is a reference to an existing plot line.
This attribute is required. The plot line ID consists of the
plot line prefix **ac** and a number.

