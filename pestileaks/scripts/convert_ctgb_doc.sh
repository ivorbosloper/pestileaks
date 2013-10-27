#!/bin/bash

# this requires a working version of libreoffice / openoffice, with an executable called soffice (staroffice legacy)
# TODO: describe how to install this, and use html-tidy to clean up the HTML

for i in doc/ctb_files/*.doc;
    do soffice --headless --convert-to html:HTML --outdir doc/ctgb_html $i;
done
