---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Reverse Engineering Keyence metadata"
subtitle: "Decoding the Keyence-inserted metadata in output TIF images."
summary: ""
authors: []
tags: [keyence, microscopy, TIF, reverse-engineering]
categories: []
date: 2021-05-19T14:36:46-04:00
lastmod: 2021-05-19T14:36:46-04:00
featured: false
draft: false
toc: true
highlight_languages: ["shell"]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
If you are just looking for the final TIFF and metadata file format, jump to the [TL;DR](#TLDR).

{{< toc >}} 

## Problem statement
Our lab uses the  [Keyence BZ-X800](https://www.keyence.com/ss/products/microscope/bz-x800_research/) to take lots of fluorescence images. The analyzer software
that comes with the insturment is relatively full-featured, but analysis using the tool is ultimately a manual process. When taking hundreds of thousands of images,
reliably reading the attached metadata is important.

In particular, if we were able to extract the lens used to take images, we could reliably auto-insert scale bars
on all captured images. Similarly, if stage-positioning information could be extracted from a multi-capture image series,
these hints could be passed to external stitching programs.

The Keyence analayzer software is capable of reading the attached metadata:

{{< figure src="analyzer_metadata.png" caption="The properties video visible when opening a TIF file in the Keyence analyzer software." >}}

This properties windows is reading some information from the TIFF tag region, so what happens if we dump the TIFF metadata? Are these reported
properties simply TIFF tags?

## Diving into the Keyence TIFF tags

```shell
$ tifftools dump .\test.tif
-- .\test.tif --
Header: 0x4949 <little-endian> <ClassicTIFF>
Directory 0: offset 683586 (0xa6e42)
  ---snip---
  EXIFIFD 34665 (0x8769):0
    Directory 0,EXIFIFD:0,0: offset 685708 (0xa768c)
      MakerNote 37500 (0x927C) UNDEFINED: <158> b'KmsFile\x01\x0c\x00\x01\x00\x03\x00\x01\x00\x00\x00\x06\x00' ...
      OffsetSchema 59933 (0xEA1D) SLONG: 0
```

Well there's only one user-defined tag here, and it is of type `UNDEFINED`. What is `UNDEFINED`? Well as listed in the [tifftools code](https://github.com/DigitalSlideArchive/tifftools/blob/611b663367c84aa3804a6488aee9a929129b0c87/tifftools/constants.py#L184):

```python
7: {'pack': None, 'name': 'UNDEFINED', 'size': 1, 'desc': 'arbitrary binary data'},
```
It looks like the Keyence software is writing their data as a single monolithic binary blob. 



## TL;DR
test
