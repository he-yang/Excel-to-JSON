# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Excel-to-JSON Documentation'
copyright = '2022~2026, WTSolutions'
author = 'WTSolutions'
release = '6.1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['myst_parser','sphinx_sitemap']
html_baseurl = 'https://excel-to-json.wtsolutions.cn/en/latest/'
sitemap_url_scheme = "{link}"
html_extra_path = ['robots.txt','ads.txt','../root_dir','llms.txt']
html_js_files = ['custom.js']
language ='en'
templates_path = ['_templates']
exclude_patterns = [
    'donation.md','usage.md','requirements.txt','.DS_Store'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "shibuya"
html_static_path = ['_static']

# 自定义导航链接
# shibuya 主题的导航链接配置项
html_theme_options = {
    "nav_links": [
        {
            "title": "Product File",
            "url": "https://s.wtsolutions.cn/excel-json-product.html"
        },
        {
            "title": "Excel-to-JSON Web App",
            "url": "https://s.wtsolutions.cn/excel-to-json.html"
        },
    ]
}

html_context = {
    "languages": [
        ("English", "/en/latest/%s.html", "en"),
        ("中文", "/zh-cn/latest/%s.html", "zh-cn"),
    ]
}
