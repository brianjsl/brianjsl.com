# Source for https://www.brianjsl.com

This repository contains the source for [https://www.brianjsl.com](https://www.brianjsl.com)

## Building the Blog

Clone the repository and make sure submodules are included:

```
$ git clone https://github.com/brianjsl/brianjsl.com.git
$ git submodule update --init --recursive
```

Install the required packages with a virtual environment using condas:

```
$ conda create -n pelican-web python=3.10
$ conda activate pelican-web
$ conda install -c conda-forge pelican Markdown pelican-render-math
```

Build the html and serve locally:

```
$ pelican content
$ pelican --listen
```

Deploy to github-pages (using actions):

```
$ git push origin main
```