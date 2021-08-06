---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Running Alphafold Without Docker"
subtitle: ""
summary: "A brief tutorial on installing all relevant Alphafold dependencies is presented"
authors: []
tags: []
categories: []
date: 2021-08-06T11:56:08-04:00
lastmod: 2021-08-06T11:56:08-04:00
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

With the release of [Alphafold 2](https://github.com/deepmind/alphafold), we have an alterate way to predict structure that is much faster than similar tools, such as Rosetta. Alphafold 2 also crushed CASP14, the main protein prediction competition, having the lowest RMS atom position error in many categories.

However, by default, Alphafold uses a Docker container to run. This is great if you own your own cluster, but many shared clusters do not have Docker (for good reason; having Docker access is effectively having root access, even with a lot of laborious hardening work).
By reading the [run_alphafold.py](https://github.com/deepmind/alphafold/blob/main/run_alphafold.py), [run_docker.py](https://github.com/deepmind/alphafold/blob/main/docker/run_docker.py), and [Dockerfile](https://github.com/deepmind/alphafold/blob/main/docker/Dockerfile) used in Alphafold, we can backtrack
the commands needed to setup a local install.

{{< toc >}} 

### Installing CUDA.

As seen at the top of the Dockerfile:

```
ARG CUDA=11.0
FROM nvidia/cuda:${CUDA}-cudnn8-runtime-ubuntu18.04
# FROM directive resets ARGS, so we specify again (the value is retained if
# previously set).
ARG CUDA
```

Alphafold expects that the CUDA version used is hard-coded to `11.0`. Installing CUDA drivers is outside of the scope of this post; if you are running on a cluster, you may have multiple different CUDA versions available.
Loading a CUDA version later than 11.0 will likely result in a "drivers out of date" error.

### Target directory layout

Pick a directory to install all of the relevant Alphafold content into. If you are downloading the full dataset, be warned; unpacked, the dataset takes around 2.3TiB of space! The size of all other files is relatively small.

```shell
$ mkdir alphafold_install
$ cd alphafold_install
```

The final directory layout will look like this (many files removed for brevity):
```
├───alphafold
│   ├───alphafold
│   │   └───common
│   │       ├───stereo_chemical_props.txt
│   │       ├───stereo_chemical_props.txt.1
│   │       └───stereo_chemical_props.txt.2
│   ├───docker
│   │   └───openmm.patch
│   ├───run_alphafold.py
│   └───scripts
│       └───download_all_data.sh
├───alphafold_env
├───bin
│   ├───(others)
│   ├───alphafold
│   ├───aria2c
│   ├───hhalign
│   ├───hhblits
│   └───kalign
├───dataset
│   ├───archives
│   ├───bfd
│   ├───mgnify
│   ├───params
│   ├───pdb70
│   ├───pdb_mmcif
│   ├───small_bfd
│   ├───uniclust30
│   └───uniref90
├───deps
│   ├───install
│   ├───hh-suite
│   ├───hmmer-3.3.2
│   └───kalign-3.3.1
└───setup_scripts
    ├───create_env.sh
    └───env.yml
```

### Clone the Alphafold repository and download parameters

To get started, clone the Github repository and switch into it:

```shell
$ git clone https://github.com/deepmind/alphafold.git
Cloning into 'alphafold'...
remote: Enumerating objects: 233, done.
remote: Counting objects: 100% (123/123), done.
remote: Compressing objects: 100% (75/75), done.
remote: Total 233 (delta 52), reused 72 (delta 47), pack-reused 110
Receiving objects: 100% (233/233), 5.68 MiB | 42.76 MiB/s, done.
Resolving deltas: 100% (89/89), done.
Checking out files: 100% (89/89), done.
$ cd alphafold
```



### Compile and install dependencies: aria2c, HMMER, kalign, and HHsuite

### Download the dataset and squashfs'ing


### Create the necessary conda environment and patch OpenMM

### Wrap the run script

### Running Alphafold!
