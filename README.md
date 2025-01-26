# pab2025_Assignment02

## Program description:
- The program is a Variant Density Calculator (VDC)
Takes as Input (matching files):
- GFF (feature info.)
- VCF (variant info.)
Outputs:
- Variant Density Calculation YAML formatted file
- Filtered VCF file containing only variants with selected features (e.g., exon,CDS)

## Program structure:
- One file only program (vdc.py)

## Program usage:

Needs to be run in a SHELL:
Example:
- python vdc.py -gff {gff_file} -vcf {vcf_file} -var {vcf} -rep {yaml_file} -ftr exon,CDS

## Requirements:
- Python with Python Standard Library