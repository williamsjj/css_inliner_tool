#!venv/bin/python
# -*- coding: utf-8-*-
####################################################################
# FILENAME: css_inliner_tool.py
# DESCRIPTION: Retrieves an HTML file from a URL and outputs a new
#              HTML file that inlines all of its CSS.
#
#
# $Id$
####################################################################
# (C)2017 DigiTar, All Rights Reserved
####################################################################

import premailer, requests
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--page_url", dest="page_url", required=True)



if __name__ == "__main__":
    args = parser.parse_args()
    
    # Retrieve Main Page
    html_text = requests.get(args.page_url).text
    
    # Transform HTML
    html_inliner = premailer.Premailer(
            html_text,
            strip_important=False,
            remove_classes=True,
            remove_unset_properties=True)
    inlined_html = html_inliner.transform()

    print inlined_html.encode("utf-8")
    
