===================
The <Locations> tag
===================

.. admonition:: <Locations>
   
   Purpose
      Lists the locations that are related to a section.

   Attributes
      - `ids <#the-ids-attribute>`__

This is an optional  list of references to existing locations.

Example:

.. code-block:: xml

   <Locations ids="lc2 lc3" />

The ids attribute
-----------------

This attribute is required. A location ID consists of the
location prefix **lc** and a number.
Multiple IDs are separated by spaces.
