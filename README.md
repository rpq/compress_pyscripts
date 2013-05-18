Examples:

python scripts/yui_compress_files.py \
--compressor path/to/yuicompressor-2.4.8.jar \
--root path/to/stylesheets \
--files cssfile1.css stylesheetlib/cssfile2.css cssfile3.css

creates files: cssfile1.min.css, stylesheetlib/cssfile2.min.css, cssfile3.min.css using yuicompressor jar file

python scripts/compile_single_file.py \
--root path/to/javascripts \
--files jsfile1.js jsfile2.js jsfile3.js
--filename single_optimized_file.js

creates one file single_optimized_file.js using unix concat
