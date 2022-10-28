.. Sphinx Examples documentation master file, created by
   sphinx-quickstart on Fri Oct 28 13:26:26 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx Example's documentation
==============================

.. grid:: 2
   :gutter: 1

   .. grid-item-card:: Sphinx Design Components
      :text-align: center
      
      Card Header 
      ^^^^^^^^^^^

      Check out this page to learn more about design
      components.

      +++

      .. button-ref:: sphinx-design-components-page
            :ref-type: ref
            :color: info
            :shadow:

            To the design components

   .. grid-item-card:: Sphinx Gallery
      :text-align: center

      Card Header
      ^^^^^^^^^^^

      What to see examples? Check out the gallery.

      +++
     
      .. button-ref:: sphinx-gallery-page
            :ref-type: ref
            :color: info
            :shadow:

            To the gallery
      
.. grid:: 2
   :gutter: 1

   .. grid-item-card::
      :text-align: center

      Another page with stuff

   .. grid-item-card::
      :text-align: center

      Another page with more stuff

.. toctree::
   :maxdepth: 2

   design
   gallery
