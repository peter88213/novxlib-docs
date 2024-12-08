===============
The <Field> tag
===============

.. admonition:: <Field>
   
   Purpose
      Defines a custom data field.

   Attributes
      - `tag <#the-tag-attribute>`__

   Content
      - Plain Text 
      
Custom data fields allow plugins to save custom data without requiring
a new DTD. This feature must be used carefully. Plugins that save fields
shall provide an option to remove them from the project file.

*novelibre* reads the content as a string and stores it internally in a
*Python* dictionary.


The tag attribute
-----------------

This attribute is required.
The *tag* attribute is used as a tag in the internal dictionary holding the content.

Example: ``zim-notebook-abs``


