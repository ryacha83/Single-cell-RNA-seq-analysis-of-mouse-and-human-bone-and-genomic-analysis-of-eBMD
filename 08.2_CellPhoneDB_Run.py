#####   This script performs CellPhoneDB ligand-receptor analysis   #####

########################
# Run analysis
########################

# Import packages
import cellphonedb   # Database version v5.0.0
import pandas as pd
import sys
import os

# Set base directory path
pd.set_option('display.max_columns', 100)
os.chdir('/path/to/output/CellPhoneDB')

# Specify paths to input files
cpdb_file_path = '/path/to/cellphonedb/database/CellPhoneDB/v5.0.0/cellphonedb.zip'
meta_file_path = '/path/to/metadata/object/GlobalObject_MetaData.txt'
counts_file_path = '/path/to/counts/object/GlobalObject_Counts.txt'

# Specify path for output files
out_path = '/path/to/results'

# Run statistical analysis method using default settings
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method
cpdb_results = cpdb_statistical_analysis_method.call(
    cpdb_file_path = cpdb_file_path,                 # mandatory: CellphoneDB database zip file.
    meta_file_path = meta_file_path,                 # mandatory: tsv file defining barcodes to cell label.
    counts_file_path = counts_file_path,             # mandatory: normalized count matrix - a path to the counts file, or an in-memory AnnData object
    counts_data = 'hgnc_symbol',                     # defines the gene annotation in counts matrix.
    score_interactions = True,                       # optional: whether to score interactions or not. 
    iterations = 1000,                               # denotes the number of shufflings performed in the analysis.
    threshold = 0.1,                                 # defines the min % of cells expressing a gene for this to be employed in the analysis.
    threads = 8,                                     # number of threads to use in the analysis.
    debug_seed = 42,                                 # debug randome seed. To disable >=0.
    result_precision = 3,                            # Sets the rounding for the mean values in significan_means.
    pvalue = 0.05,                                   # P-value threshold to employ for significance.
    subsampling = False,                             # To enable subsampling the data (geometric sketching).
    subsampling_log = False,                         # (mandatory) enable subsampling log1p for non log-transformed data inputs.
    separator = '|',                                 # Sets the string to employ to separate cells in the results dataframes "cellA|CellB".
    debug = False,                                   # Saves all intermediate tables employed during the analysis in pkl format.
    output_path = out_path,                          # Path to save results.
    output_suffix = None                             # Replaces the timestamp in the output files by a user defined string in the  (default: None).
    )
