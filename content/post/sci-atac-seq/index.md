---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "sci-ATAC-seq: from FASTQs to single cell phenotypes"
subtitle: "Enabling repeatable sci-ATAC-seq analyses"
summary: "Discusses the necessary steps for a full analysis of a sci-ATAC-seq dataset and provides a repeatable framework for this analysis."
authors: [admin]
tags: [sci-ATAC-seq,illumina,NGS,snakemake]
categories: []
date: 2021-04-29T14:05:24-04:00
lastmod: 2021-04-29T14:05:24-04:00
featured: false
draft: false
toc: true
highlight: true
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
{{< toc >}} 

## Summary
Hello there? Why isn't this updating?

## The sci-ATAC-seq protocol
Before we dive into bioinformatics,


## Prior art

https://github.com/r3fang/SnapTools

## Bioinformatics

### Setting up your environment

Before we start, we recommend using Mamba as your package manager. Mamba
has rewritten much of Conda's internals and is at least an order of magnitude
faster than Conda.

The cleanest way to use Mamba is to install it with Conda into its own environment, by doing:

```shell
$ conda create -n mamba mamba
...lots of Conda output. It takes >1 minute to install a single package!
$ conda activate mamba
```

Once in the mamba-only environment, 

```shell
$ git clone https://github.com/GallowayLabMIT/sci-atac-seq-analysis.git
```

After installing

```shell
$ conda config --set channel_priority strict
test
$ conda env create -p ./cenv -f=environment.yml
Collecting package metadata (repodata.json): done
Solving environment: done
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate /path/to/your/location/cenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate
$ conda activate ./cenv
```
