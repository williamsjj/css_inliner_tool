# CSS Inliner Tool #

`css_inliner_tool` will retrieve an HTML page from a URL and then inline all of its CSS to make it suitable for e-mail (including external stylesheets). Resulting HTML with inlined CSS is output to stdout.

## Install ##
```
make prepare_env
```

## Run ##
```
./css_inliner_tool.py --page_url <URL>
```
