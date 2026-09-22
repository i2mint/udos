# udos

> **Superseded.** This project's brief (dataset search, acquisition, reusable preparation, sharing) is being built as [`conte`](https://github.com/thorwhalen/conte). No code was ever written here beyond a docstring. The `udos` name is kept reserved on PyPI for a possible standalone dataset-descriptor standard, which `conte` will settle first.

Universal Dataset Open Standard

A place to develop an open standard for dataset 
search, acquisition, reusable preparation, and sharing.

# Target user stories

- Search outside data (use several sources such as kaggle, github, named urls, etc?)
- Get local copy of data 
    - Set rules for automatic updates of data
- Search locally using:
    - General query expansion (using word2vec?)
    - Custom aliases
    - Fuzzy matching
- Construct data feeds by combining multiple data feeds
- Visualize relationships (to understand the data, spot errors, etc.)
- Operable quick models (for quick-and-dirty inference)
