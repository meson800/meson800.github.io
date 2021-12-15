---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Seaborn tips: Contexts and subplot label alignment"
subtitle: ""
summary: ""
authors: []
tags: [seaborn, dataviz]
categories: [bites]
date: 2021-12-14T12:19:53-05:00
lastmod: 2021-12-14T12:19:53-05:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
#image:
#  caption: ""
#  focal_point: ""
#  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

{{< toc >}}

## Seaborn contexts

When playing around with Seaborn-generated graphs within a Jupyter notebook, the default settings output graphs
that are appropriate for viewing in a notebook. However, you can use different [contexts](https://seaborn.pydata.org/generated/seaborn.set_context.html)
to control the output scaling of the graph,
including both the text size, marker size, and default line-widths.

The relevant contexts are:
- ```python
  sns.set_context("paper")
  ```
  Uses display sizes that are appropriate when added to a fixed-page document.
  When using this scaling, output works best if you properly set the width/height
  of the figure to the actual desired print scale (with `plt.figure(width=3, height=5)`
  for example for a 3 inch by 5 inch figure).
  ![A two-paned plot at paper scale](piggybac_integration_paper.svg)
- ```python
  sns.set_context("notebook")
  ```
  Uses display sizes appropriate for interactive viewing of your figures while testing.
  This gives good results for viewing directly within the notebook.
  ![A two-paned plot at notebook scale](piggybac_integration_notebook.svg)
- ```python
  sns.set_context("talk")
  ```
  Uses display sizes that are appropriatly large for placing on presentation
  slides.
  ![A two-paned plot at talk scale](piggybac_integration_talk.svg)
- ```python
  sns.set_context("poster")
  ```
  Uses display sizes that are readable at a distance when printed
  on a poster.
  ![A two-paned plot at poster scale](piggybac_integration_poster.svg)

## Matplotlib: aligning subplot labels

When dealing with a plot with multiple subpanels, the x and y labels may not be necessarily
aligned. Instead of manually aligning, you can use [figure.align_xlabels](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.align_xlabels)
and [figure.align_ylabels](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.align_ylabels)
to [align a specific set of axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html).
