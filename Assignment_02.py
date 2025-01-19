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
    parser.add_argument("--gff", "-gff", required=True, help="Input GFF file")
    parser.add_argument("--vcf", "-vcf", required=True, help="Input VCF file")
    parser.add_argument("--var", "-var", required=True, help="Output filtered VCF file")
    parser.add_argument("--rep", "-rep", required=True, help="Output report YAML file")
    parser.add_argument("--ftr", "-ftr", required=True, help="Feature(s) type to analyze (e.g., exon,CDS)")
    args = parser.parse_args()
    #return parser.arg_parse()


class file_reading():
    """
    A class to everything that is input
    """
    def __init__(self, gff_file, vcf_file, ftr_type):
        self.args.gff = gff_file
        self.args.vcf = vcf_file
        self.args.ftr = ftr_type

    def gff_read(self, gff_file):
        self.args.gff = gff_file
        """
        A method to read the GFF file
        """
        #Seqname Source Feature Start End Score Strand Frame Attribute
        features = [] 
        with open(gff_file) as file1:
            for line in file1:
                if line.startswith("#"):
                    continue
                colunas = line.strip().split("\t")
                if colunas[2] == self.ftr_type:  
                    features.append(colunas)
                     
        
        return features()
    def vcf_read(self):
        """

        """
        #CHROM POS   ID    REF  ALT   QUAL FILTER INFO
        variants = []
        with open(self.args.vcf) as file2:
            for line in file2:
                if line.startswith("#"):
                    continue
                colunas = line.strip().split("\t")
                variants.append(colunas)
        return variants()
    
def  gff_vcf_comparison(self, features, variants):
    """

    """
    filtered_vcf = [] 
    self.features = features
    self.variants = variants
    for sequence in features:
        for chrom in variants:
            if features[2] < variants[1] and features[3] > variants[1]:
                filtered_vcf.append(chrom)
            with open(self.rep_file) as file3:
                pass


arg_parse()