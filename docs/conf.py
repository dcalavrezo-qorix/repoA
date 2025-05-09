import os
import sys
import logging
logger = logging.getLogger("sphinx_needs")
logger.setLevel(logging.DEBUG)



project = 'RepoA'
author = 'Dan'
release = '0.1'
version = "v1"

extensions = [
    'sphinx_needs',
]

needs_id_prefix = "MODA_"
needs_id_required = True

# ✅ Proper export settings
needs_build_json = True
needs_json_indent = 2

# ✅ Versioning (important!)
needs_extra_options = ["version"]
needs_version = "v1"
needs_versions = {"v1": "Initial version"}
needs_current_version = "v1"

master_doc = 'index'

# Setup need types
needs_types = [
    dict(directive="req", title="Requirement", prefix="REQ_", color="#BFD8D2", style="node"),
]
sys.path.insert(0, os.path.abspath('.'))
