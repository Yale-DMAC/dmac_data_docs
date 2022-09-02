ArchivesSpace Plugin to provide a link (on resource AND archival object pages) to static PDF files
===============


## Getting Started

Enable the plugin by editing the file in `config/config.rb`:

  AppConfig[:plugins] >> 'yale_pdf'

Also add the following to `config/config.rb`:

  AppConfig[:pui_page_actions_print] = false

This will turn off the default PDF page action that is set to appear in the PUI.

Yale plans to use something like this plugin so that the PDF links in the PUI will go to statically generated PDF/UA files, which will be available on another web server. These PDF/UA files will be generated and updated nightly by Hudson Molonglo's ArchivesSpace Export Service plugin: https://github.com/hudmol/archivesspace_export_service

For now, the expectation is that you would change the PDF root URI directly within the ERB file.

Restart the application.
