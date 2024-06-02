=================
The <SECTION> tag
=================

.. admonition:: <SECTION>
   
   Purpose
      Defines a section.

   Attributes
      - `id <#the-id-attribute>`__
      - `append <#the-append-attribute>`__
      - `scene <#the-scene-attribute>`__
      - `status <#the-status-attribute>`__
      - `type <#the-type-attribute>`__

   Content
      - `Title <title.html>`__
      - `Desc <desc.html>`__
      - `Link <link.html>`__
      - `Notes <notes.html>`__
      - `Tags <tags.html>`__
      - `Goal <goal.html>`__
      - `Conflict <conflict.html>`__
      - `Outcome <outcome.html>`__
      - `PlotlineNotes <plotlinenotes.html>`__
      - `Date <date.html>`__
      - `Day <day.html>`__
      - `Time <time.html>`__
      - `LastsDays <lastsdays.html>`__
      - `LastsHours <lastshours.html>`__
      - `LastsMinutes <lastsminutes.html>`__
      - `Characters <_characters.html>`__
      - `Locations <_locations.html>`__
      - `Items <_items.html>`__
      - `Content <content.html>`__

The id attribute
----------------

This attribute is required. The section ID consists of the
section prefix **sc** and a number.

Example: ``sc13``


The append attribute
--------------------

- 0: Put a section separator between this section and the previous one.
- 1: Append this section to the previous one without a section separator.

Default value: 0

The scene attribute
-------------------

- 0: Not a scene.
- 1: Action scene.
- 2: Reaction scene.
- 3: Other scene.

Default value: 0

The status attribute
--------------------

- 1: Outline.
- 2: Draft.
- 3: First Edit.
- 4: Second Edit.
- 5: Done.

Default value: 1

The type attribute
------------------

- 0: Normal section.
- 1: Unused section.
- 2: Level 1 stage.
- 3: Level 2 stage.

Default value: 0
