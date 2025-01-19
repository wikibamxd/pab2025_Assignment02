import argparse
def arg_parse():
    """
    Add arguments as inputs for GFF and VCF files
    Add arguments as outputs for filtered VCF file and report YAML file
    Add argument for feature(s) type to analyze
    """
    parser = argparse.ArgumentParser(
                    prog = "Assignment_02", 
                    description = "Calculates the density of variants within specified genomic features")
    parser.add_argument("-gff", required=True, help="Input GFF file")
    parser.add_argument("-vcf", required=True, help="Input VCF file")
    parser.add_argument("-var", required=True, help="Output filtered VCF file")
    parser.add_argument("-rep", required=True, help="Output report YAML file")
    parser.add_argument("-ftr", required=True, help="Feature(s) type to analyze (e.g., exon,CDS)")
    return parser.arg_parse()

class file_reading():
    """
    A class to everything that is input
    """
    def __init__(self, gff_file, vcf_file, ftr_type):
        self.gff_file = gff_file
        self.vcf_file = vcf_file
        self.ftr_type = ftr_type
    def gff_read(self):
        """
        A method to read the GFF file
        """
        with open(self.gff_file) as file1:
            for line in file1:
                if line.startswith("#"):
                    continue
                