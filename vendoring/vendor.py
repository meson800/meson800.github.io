from pathlib import Path

JS_LIST = [
    'jquery.min.js',
    'lazysizes.min.js',
    'imagesloaded.pkgd.min.js',
    'isotope.pkgd.min.js',
    'jquery.fancybox.min.js',
    'instantpage.min.js',
    'highlight.min.js',
    'leaflet.min.js',
    'fuse.min.js',
    'jquery.mark.min.js',
    'custom.js',
]

CSS_LIST = [
    'all.min.css',
    'jquery.fancybox.min.css',
    'academicons.min.css',
    'github.min.css',
    'leaflet.min.css',
    'custom.css',
]

if __name__ == '__main__':
    output_dir = Path('output')
    css_dir = Path('css')
    js_dir = Path('js')
    with open(output_dir / 'main.min.js', 'wb') as js_file:
        for js in JS_LIST:
            with open(js_dir / js, 'rb') as input_js:
                js_file.write(input_js.read())

    with open(output_dir / 'main.min.css', 'wb') as css_file:
        for css in CSS_LIST:
            with open(css_dir / css, 'rb') as input_css:
                css_file.write(input_css.read())
