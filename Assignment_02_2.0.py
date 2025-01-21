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
    return parser.parse_args()

class file_reading:
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
        features = []
        try:
            with open(self.gff_file) as file1:
                for line in file1:
                    if line.startswith("#"):
                        continue
                    colunas = line.strip().split("\t")
                    if colunas[2] == self.ftr_type:   # o self.ftr vai ser o que metes no terminal (gene ou exon) e adicionar á lista sempre que encontrar
                        features.append({ 'seqid': colunas[0],   #se a coluna 2 tiver a feature escolhida adiciona um dicionário a features com as caracterias das colunas todas
                                          'source': colunas[1],
                                            'type': colunas[2],
                                              'start': int(colunas[3]),
                                                'end': int(colunas[4]),
                                                  'score': colunas[5],
                                                    'strand': colunas[6],
                                                      'phase': colunas[7],
                                                        'attributes': colunas[8] })
            if not features:
                raise ValueError(f"No features of the type {self.ftr_type} found in the GFF file")
        except FileNotFoundError:
            raise ValueError(f"{self.gff_file} not found")
        return features
    def vcf_read(self):
        """
        A method to read the VCF file
        """
        variants = []
        try:
            with open(self.vcf_file) as file2:
                for line in file2:
                    if line.startswith("#"):
                        continue
                    colunas = line.strip().split("\t")
                    variants.append({ 'chrom': colunas[0],
                                      'pos': int(colunas[1]),
                                        'id': colunas[2],
                                          'ref': colunas[3],
                                            'alt': colunas[4],
                                              'qual': colunas[5],
                                                'filter': colunas[6],
                                                  'info': colunas[7] })
            if not variants:
                raise ValueError(f"No variants found on the VCF file")
        except FileNotFoundError:
            raise ValueError(f"{self.vcf_file} not found")
        return variants
    def vcf_filtering(self, features, variants):
        """
        A method to filter the vcf file and give -var as output
        """
        filtered_variants = []
        for variant in variants:
            for feature in features:
                if feature['seqid'] == variant['chrom'] and feature['start'] <= variant['pos'] <= feature['end']:
                    filtered_variants.append(variant)
                    break
    def calculate_density(self, features, variants):
        """
        A method to calculate the density  
        densidade vai ser o numero de posição final - inicial, depois vês quantas variantes tens e divides pela diferença e multiplicar por 1000
        """
