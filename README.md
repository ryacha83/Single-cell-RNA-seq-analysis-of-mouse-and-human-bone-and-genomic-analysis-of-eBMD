# Analysis code for the mouse scRNA-seq data of "Multiscale analysis and functional validation of the cellular and genetic determinants of skeletal disease" by Chai et al.



# Scripts

* 01_Preprocessing_QC_clustering.Rmd is an R-script that contains functions used in the preprocessing, QC and clustering of all cells from the mouse scRNA-seq data
* 02_Preprocessing_QC_clustering_of_non_haematopoietic_cells.Rmd is the R-script that contains functions used in the preprocessing, QC and clustering of non-haematopoietic cells from the mouse scRNA-seq data
* 03_Monocle2_pseudotime_osteoblasts_and_chondrocytes.Rmd is the R-script used to run Monocle 2 pseudotime analysis of osteoblast and chondrocyte cells of the mouse scRNA-seq data
* 04_GeneSpeciesConversion.Rmd is the R-script used to convert mouse gene names to human orthologues
* 05_CalculateRestrictionScores.Rmd is the R-script used to calculate how restricted the genes in the cluster of interest vs other clusters
* 06_Enrichment_MonogenicDysplasias.Rmd is the R-script used for running hypergeometric test to assess enrichment of genes involved in monogenic skeletal diseases in gene programs
* 07_Enrichment_MGI.Rmd is is the R-script used for running hypergeometric test to assess enrichment of genes with abnormal skeletal phenotypes in the MGI database 
* 08.1_CellPhoneDB_DataPreparation.Rmd is the R-script used to prepare data for cell-cell interaction analysis using CellPhoneDB
* 08.2_CellPhoneDB_Run.py is the python script used to run cell-cell interaction analysis using CellPhoneDB
* 08.3_CellPhoneDB_Analysis.Rmd is the R script used to run cell-cell interaction analysis using CellPhoneDB
* 09_snATACSeqAnalysis.Rmd is the R script used to run the mouse snATACseq data using Signac and Seurat
* 010_Preprocessing_QC_clustering_human.Rmd is an R-script that contains functions used in the preprocessing, QC and clustering of all cells from the human scRNA-seq data
* 011_Label_transfer_mouse_and_human.Rmd is the R-script that contains functions used in the analysis to compare mouse and human scRNA-seq data
* 012-Chai-et-al-Genomics-Code.txt is the script that contains functions used in the analysis of GWAS eBMD data
