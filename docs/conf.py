import os
import sys

# Project info
project = 'RepoA'
author = 'Dan'
release = '0.1'

extensions = [
    'sphinx_needs',
]

# Give each repo a unique ID prefix
needs_id_prefix = "MODA_"   
needs_id_required = True   
needs_build_json = True
master_doc = 'index'


# Optional but helps:
needs_version = "v1"
needs_versions = {"v1": "Initial version"}
needs_current_version = "v1"


# Paths: include your docs folder so Sphinx can find index.rst
sys.path.insert(0, os.path.abspath('.'))


