# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

%pip install semantic-link-labs

import sempy_labs as labs
from sempy_labs import directlake as dl

dl.get_direct_lake_sources(dataset="sales_model", workspace="wksp-feature-models")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
