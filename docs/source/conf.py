# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'XuanPolicy'
copyright = '2023, Wenzhang Liu, Wenzhe Cai, Kun Jiang, Yuanda Wang, Guangran Cheng, Jiawei Wang, Jingyu Cao, Lele Xu, Chaoxu Mu, and Changyin Sun'
author = 'Wenzhang Liu, Wenzhe Cai, Kun Jiang, Yuanda Wang, Guangran Cheng, Jiawei Wang, Jingyu Cao, Lele Xu, Chaoxu Mu, and Changyin Sun'
release = 'v0.1.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The master toctree document.
master_doc = 'index'
