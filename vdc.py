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
    Take gff and vcf files as input and returns .vcf and .yml files as output
    Select the type of feature to search
    """
    def __init__(self, gff_file, vcf_file, ftr_type):
        self.gff_file = gff_file
        self.vcf_file = vcf_file
        self.ftr_type = ftr_type.split(",")
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
                    colunas = line.strip().split()
                    if colunas[2] in self.ftr_type:   
                        features.append({ 'seqid': colunas[0],   
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
                    colunas = line.strip().split()
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
        A method to filter the vcf file 
        """
        filtered_variants = []
        for variant in variants:
            for feature in features:
                if feature['seqid'] == variant['chrom'] and feature['start'] <= variant['pos'] <= feature['end']:
                    filtered_variants.append(variant)
                    break
        return filtered_variants
    def calculate_density(self, features, filtered_variants):
        """
        A method to calculate the density  
        """
        density_value = []
        for feature in features:
            length = feature['end'] - feature['start'] + 1
            num_variants = 0
            for variant in filtered_variants:
                if feature['start'] <= variant['pos'] <= feature['end']:
                    num_variants += 1
            density = (num_variants / length) * 1000
            den_values = {
                'FeatureID': feature['attributes'],
                'Length': length,
                'VariantCount': num_variants,
                'Density': density
            }
            density_value.append(den_values)
        return density_value
    def variants_report(self, filtered_variants, vcf_output):
        """
        A method to build the filtered vcf file
        """
        with open(vcf_output, "w") as file3:
            file3.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
            for variant in filtered_variants:
                file3.write(f"{variant['chrom']}\t{variant['pos']}\t{variant['id']}\t{variant['ref']}\t{variant['alt']}\t{variant['qual']}\t{variant['filter']}\t{variant['info']}\n")

    def density_report(self, density_value, features, filtered_variants, output_report):
        """
        A method to print the density report
        """
        with open(output_report, "w") as file4:
            file4.write("FilteringReport:\n")
            file4.write(f"  Feature_Type: {', '.join(self.ftr_type)}\n")
            file4.write(f"  TotalFeatures: {len(features)}\n")
            file4.write(f"  TotalVariants: {len(filtered_variants)}\n")
            file4.write(f"  VariantsPerFeature:\n")
            for den_values in density_value:
                file4.write(f"    - Feature ID: {den_values['FeatureID']}\n")
                file4.write(f"      Length: {den_values['Length']}\n")
                file4.write(f"      Variant Count: {den_values['VariantCount']}\n")
                file4.write(f"      Density: {den_values['Density']}\n")

def main():
    args = arg_parse()
    reader = file_reading(args.gff, args.vcf, args.ftr)
    
    features = reader.gff_read()
    variants = reader.vcf_read()
    filtered_variants = reader.vcf_filtering(features, variants)
    density_value = reader.calculate_density(features, filtered_variants)
    
    reader.variants_report(filtered_variants, args.var)
    reader.density_report(density_value, features, filtered_variants, args.rep)
    
if __name__ == "__main__":
    main()
        
