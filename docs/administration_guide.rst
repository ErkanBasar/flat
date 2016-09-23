*****************************************
FLAT Administration Guide
*****************************************

After FLAT has been properly installed, administration entails the following
parts:

1. Setting up configuration(s) for your annotation task(s) in ``settings.py``
2. Managing user accounts and permissions using the administrative webinterface (``http://your.flat.url/admin/``)
3. Preparing your data in FoLiA

Note that this documentation does not cover installation and the initial setup!

=============================================
Configuration
=============================================

Configuration of FLAT is done in the typical unix fashion by editing a
configuration file, there is no web interface for this. For FLAT
``settings.py`` (or however you renamed) fulfills this role. Making it a
centralized place for all settings. The file is heavily commented to guide you
along.

Although ``settings.py`` is a Python script, no Python knowledge is necessary.
It may help some to know that, the pythonic configuration syntax is also very
similar to JSON.

-----------
Modes
-----------

FLAT is composed of various modules, exposed as modes to the user. The user always chooses
a mode to work in from the menu.

The following are available:

* ``viewer`` - A document and annotation viewer (no editing)
* ``editor`` - The annotation editor
* ``structureeditor`` - A structural editor (not finished yet)
* ``metadata`` - A simple metadata editor

These are defined in the ``MODES`` variable. Individual configurations (see
below) can in turn pick a subset of the modes, if not all of them:

.. code:: python

    MODES = [
        ('viewer','Viewer'),
        ('editor','Annotation Editor'),
        ('structureeditor','Structure Editor'),
        ('metadata','Metadata Editor'),
    ]

The pairs correspond to the internal name for the mode, and a human readable
label.

-----------------
Configurations
-----------------

FLAT supports multiple so-called *configurations*. The user selects what
configuration to use upon login.

This allows using the same FLAT installation
for multiple annotation projects. The document store is shared amongst all
configurations, allowing for different ways to view/edit the same document,
unless explicitly constrained.

Each configuration defines precisely what elements of user interface are shown and
which are not, what functionality is enabled, and what defaults are set. FLAT contains a lot of
features, which will easily overwhelm the user if all are enabled. You will
want to constrain this for your annotation task.

The ``DEFAULTCONFIGURATION`` variable refers to the configuration that is pre-selected
upon login, and will therefore be the default unless the user selects another. 

All configurations are defined in ``CONFIGURATIONS`` (a simple Python
dictionary for those familiar with Python, the keys correspond to the
configuration name and the value is another dictionary with configuration
options). By default, a ``full`` configuration will be defined that is as
permissive as possible. You will want to add your own configurations that are
more restrictive.

We will discuss the individual configuration options here:

* ``name`` - The name of the configuration, this is what users will see in the login screen, make sure the name is indicative of your annotation project, if any.
* ``modes`` - This defines the modes that are enabled for this configuration.  The syntax equals that of ``MODES`` above.
* ``perspectives`` - The viewer and editor allow for different perspectives on the data. This option determines what perspectives may be selected. This is list (of strings) of the following items:
   * ``document``: a view of the entire document
   * ``toc``: a view of a named subsection of the document (a table of contents will be automatically constructed)
   * or any other FoLiA XML tag corresponding to a structural element , such as ``'s'`` for sentence, ``'p'`` for paragraphs, ``'event'`` for events.
* ``allowupload`` - Boolean value indicating whether users may upload their own FoLiA documents or not
* ``annotationfocustype`` - Sets the annotation type for the default annotation focus, effectively highlighting annotations of this type immediately upon opening the document. The type needs to be a valid FoLiA tag name (see the FoLiA documentation at https://proycon.github.io/folia), such as ``'pos'``, ``'lemma'``, ``'entity'``, etc...  If you set this, also set the next option.
* ``annotationfocusset`` - Sets the set for the default annotation focus. The set is a URL pointing to a FoLiA Set Definition file. Set to ``None`` if not used, use with the above otherwise.
* ``allowannotationfocus`` - List of FoLiA annotation types (corresponding to the xml tags) that are allowed as annotation focus, i.e. that can be selected by the user through the menu. Set to ``True`` to enable all. 
* ``initialviewannotation`` - List of FoLiA annotation types (corresponding to the xml tags) that are initially enabled in the local annotation viewer, i.e. the pop-up when the user hovers over elements. Set to ``True`` to enable all.
* ``initialglobviewannotations`` - List of FoLiA annotation types (corresponding to the xml tags) that are initially enabled in the global annotation viewers (the annotation boxes above the words).
* ``allowedviewannotation`` - List of FoLiA annotation types (xml tags) that are allowed to be viewed,  a superset of initialviewannotations/initialglobviewannotations. Users can enable/disable each as they see fit. Set to ``True`` to enable all.
* ``initialeditannotations`` - List of FoLiA annotation types (xml tags) that are initially enabled in the editor dialog (when users click an element for editing), set to ``True`` to enable all.
* ``allowededitannotations`` - List of FoLiA annotation types (xml tags) that are allowed in the editor dialog (the user can enable/disable each as he/she sees fit), set to ``True`` to enable all.
* ``allowaddfields`` - Boolean value, allow the user to add annotation types not yet present on a certain element? 
* ``allowdeclare`` -- Boolean value, allow the user to add annotation types not yet present in the document?
* ``editformdirect`` -- Boolean, enable the direct editing form (this is the default and most basic form of editing, consult the user guide). It should be ``True`` unless you want to force other editing forms.
* ``editformcorrection`` -- Boolean, enable editing as correction.
* ``editformalternative`` -- Boolean, enable editing as alternative.
* ``editformnew`` -- Boolean, enable editing as new annotation, this allows for adding multiple or overlapping annotations of the same type/set.
* ``alloweditformdirect`` -- Boolean, allow the user the enable/disable direct editing himself/herself.
* ``alloweditformcorrection`` -- Boolean, allow the user the enable/disable correction editing himself/herself.
* ``alloweditformalternative`` -- Boolean, allow the user the enable/disable alternative editing himself/herself.
* ``alloweditformnew`` -- Boolean, allow the user the enable/disable new editing himself/herself.
* ``allowconfidence`` -- Boolean, allow confidence values to be set/added?
* ``initialcorrectionset`` - String to the set definition used for corrections.
* ``autodeclare`` -- Automatically declare the following annotation types when a document is loaded. This is a list of 2-tuples ``(tag,set)`` that specify what annotation types and with what sets to declare automatically for each document that is opened.  (recall that FoLiA demands all annotations to be declared and that sets can be customi-made by anyone) 
  

=====================
User permissions
=====================


FLAT comes with a simple administrative webinterface that allows to configure
user permissions. The administrative interface is accessible only by administrators
and can be found at ``http://your.flat.url/admin/``.

You can configure which users may access which namespaces/directories.

(TODO: elaborate)


===============================
Preparing your data in FoLiA
===============================

----------------
Introduction
----------------

We urge people wanting to set up FLAT to familiarise themselves with `FoLiA
<https://proycon.github.io/folia>`_, as
the tool is specifically designed around this format. A main characteristic of FoLiA is
the **class/set paradigm** and the distinction of a large number of specific
**annotation types**, such as for example part-of-speech, lemma, dependencies,
syntax, co-references, semantic roles, and many more...

The values of annotations, of whatever type, are known as **classes**, which in
turn are the elements of **sets**. A set thus defines what classes exist. A set
is for example a part-of-speech tagset, and the invidual part-of-speech tags
would be the classes. **FoLiA itself never prescribes sets**, only annotation
types, it is up to the user to decide what set to use and anybody can freely
create sets! This offers a great deal of flexibility, as you can use FLAT and
FoLiA with whatever tagset you desire (provided you make a set definition for
it).

Sets are defined in Set Definition files, these tie the classes to nice human
presentable labels (they may also impose taxonomies, put constraints on class
combinations,  and link to data category registries). FLAT relies on
these set definitions a great deal, as it uses them to present the labels for
the classes. Examples of set definitions can be found here:
https://github.com/proycon/folia/tree/master/setdefinitions 

For more information about FoLiA, see https://proycon.github.io/folia , the
format itself is extensively documented.

-----------------------
Right-to-left support
-----------------------

FLAT has proper right-to-left support for languages such as Arabic, Farsi and Hebrew.
This relies on the FoLiA document having either a metadata attribute
*direction* set to ``rtl``, or a properly set *language* field in the
metadata with a iso-639-1 or iso-639-3 language code of a known right-to-left
language.