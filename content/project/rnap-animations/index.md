---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "RNA Polymerase Animations"
summary: ""
authors: []
tags: []
categories: []
date: 2021-04-13T11:18:31-04:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

To convert the EXRs into a movie file, we use the following `ffmpeg` command:

```
ffmpeg -f lavfi -i color=c=white:s=1920x1080 -r 60 -apply_trc iec61966_2_1 -i output/%04d.exr -filter_complex "[0:v][1:v]overlay=shortest=1" -vcodec libx264 -pix_fmt yuv420p -preset slow -crf 18 -r 60 output_filename.mp4
```

To run the headless Blender render, we use:

```
path_to_blender/blender -b -y polymerase_movie_baked.blend -a
```
