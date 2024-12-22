# Bioinformatics Analysis of Proteins in Various Species

This program allows the analysis of protein data from multiple species, focusing on evaluating characteristics such as protein length, amino acid composition, and their relationship with genes and organisms. It is designed to process files in TSV format that contain relevant columns such as Organism, Sequence, Gene Names

This program is useful for:

Performing comparative analysis between species.
Identifying patterns in protein composition and length.
Generating clear and useful visualizations for scientific publications or reports.

Main Features:
- **Protein length distribution**: Histogram showing how protein lengths are distributed in the data set.
- **Amino acid frequency**: Calculation and visualization of the frequency of amino acids in the analyzed sequences.
- **Comparison between species**: Analysis of the average protein length per species, using clear and detailed graphics.
- **Gene-length relationship**: Visualization of the relationship between specific genes and the average length of the proteins they encode.
- **Amino acid composition by species**: Use of a heatmap to show differences in average amino acid composition between species.
**Requirements**
1) TSV files containing at least the columns:
- Organism
- Sequence
- Gene Names
2) Required libraries**
- pandas
- seaborn
- matplotlib
