Text-analytics-lecture
==============================

This is the practice project for the Text Analytics lecture at Nova Information Management School in summer semester of 2018.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── week_3.data
    │   ├── interim        <- Intermediate week_3.data that has been transformed.
    │   ├── processed      <- The final, canonical week_3.data sets for modeling.
    │   └── raw            <- The original, immutable week_3.data dump.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── presentations      <- Presentations that cover the course content.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml    <- The environment file (Anaconda) for reproducing the analysis environment.
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── week_3.data           <- Scripts to download or generate week_3.data
        │   └── make_dataset.py
        │
        ├── week_3.features       <- Scripts to turn raw week_3.data into week_3.features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py
--------

# Text Analytics Lecture
This is the practice project for the Text Analytics lecture at Nova Information Management School in summer semester of 2018.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine, so can develop and practice at home.
### Prerequisites
This project requires an installation of [`Git`](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [`Anaconda`](https://www.anaconda.com/download/) or [`Miniconda`](https://conda.io/miniconda.html), [`Jupyter Notebook`](http://jupyter.readthedocs.io/en/latest/install.html) and a Python IDE (we recommend [`IntelliJ IDEA`](https://www.jetbrains.com/help/idea/install-and-set-up-intellij-idea.html)).
### Installation
Once you have th prerequisites installed, you can create a local copy of this repositoy by opening `Git Bash` and executing:
```
git clone https://github.com/jbj2505/lecture-text-analytics
```
Next we reproduce the virtual environment `text_analytics` by opening the `Anaconda Prompt` and executing:
```
conda env create -f environment.yaml
```
Before starting the code, we activate the `text_analytics` environment by executing:
```
conda activate text_analytics # on Windows
conda source activate text_analytics # on Mac
```
## Authors
Jan-Benedikt Jagusch	m2016022@novaims.unl.pt