=================
The <CHAPTER> tag
=================

.. admonition:: <CHAPTER>
   
   Purpose
      Defines a part or chapter.

   Attributes
      - `id <#the-id-attribute>`__
      - `noNumber <#the-nonumber-attribute>`__
      - `isTrash <#the-istrash-attribute>`__
      - `level <#the-level-attribute>`__
      - `type <#the-type-attribute>`__

   Content
      - `Title <title.html>`__
      - `Desc <desc.html>`__
      - `Notes <notes.html>`__
      - `Link <link.html>`__
      - `SECTION <section.html>`__

The id attribute
----------------

This attribute is required. The chapter ID consists of the
chapter prefix **ch** and a number.

Example: ``ch13``

The noNumber attribute
----------------------

- 0: Auto-number this chapter, if applicable.
- 1: Exclude this chapter from auto-numbering.

Default value: 0

The isTrash attribute
---------------------

- 0: This is a chapter or part.
- 1: This chapter is the novelibre project's "trash bin".

Default value: 0

The level attribute
-------------------

- 1: Part level.
- 2: Regular chapter level.

Default value: 2

The type attribute
------------------

- 0: Normal.
- 1: Unused.

Default value: 0
