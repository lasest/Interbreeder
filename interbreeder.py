#!/usr/bin/python3

from typing import List, Tuple
import sys

def get_genes(genotype: str) -> List[str]:
    """Returns a list of genes, present in a given genotype by splitting it at every second character"""
    
    genes = list()
    
    for i in range(int(len(genotype) / 2)):
        gene = genotype[i * 2: i*2 + 2]
        genes.append(gene)  
    
    return genes

def get_alleles(genes: List[str]) -> List[Tuple[str]]:
    """Splits genes into alleles. Returns a list of tuples. Each tuple has two elements, corresponding to the unique alleles of the gene. If only one allele is present in the genotype, the second element of the tuple will be None"""
    
    alleles = list()    
    for gene in genes:
        allele_1 = gene[0]
        allele_2 = None
        
        if gene[1] != allele_1:
            allele_2 = gene[1]
        
        alleles.append((allele_1, allele_2))
    
    return alleles

def get_gametes(alleles: List[Tuple[str]], index: int, chosen: str, gametes: List[str]) -> None:
    """Recursively generates a list of all gametes that will be obtained from a given set of alleles"""
    
    if index == len(alleles):
        gametes.append(chosen)
        return
    
    chosen1 = chosen + alleles[index][0]
    get_gametes(alleles, index + 1, chosen1, gametes)
    
    if alleles[index][1]:
        chosen2 = chosen + alleles[index][1]
        get_gametes(alleles, index + 1, chosen2, gametes)

def combine_gametes(gamete_1: str, gamete_2: str) -> str:
    """Combines two given gametes to form a string representing the resulting genotype"""
    
    genotype = ""
    for index in range(len(gamete_1)):
        gene = gamete_1[index] + gamete_2[index]
        genotype += "".join(sorted(gene))
    
    return genotype

def get_gamete_combinations(gametes_1: List[str], gametes_2: List[str]) -> List[str]:
    """Returns all gamete combinations that can be obtained from two given sets of gametes"""
    
    genotypes = list()
    
    for index_1 in range(len(gametes_1)):
        for index_2 in range(len(gametes_2)):
            genotype = combine_gametes(gametes_1[index_1], gametes_2[index_2])
            genotypes.append(genotype)
    
    return genotypes

def get_unique_genotypes(genotypes: List[str]) -> dict:
    """Takes a list of genotypes and counts how many times each genotype is present in the list. Returns a dictionary in the form {genotype: number_of_occurences}"""
    
    unique_genotypes = dict()
    
    for genotype in genotypes:
        if genotype in unique_genotypes:
            unique_genotypes[genotype] += 1
        else:
            unique_genotypes[genotype] = 1
    
    return unique_genotypes

def print_unique_genotypes(unique_genotypes: dict):
    """Prints a dictionary of unique genotypes in a form <Number of occurences> Genotype : ..."""
    
    output = "Unique genotypes: "
    for genotype, count in unique_genotypes.items():
        output += f"{count}{genotype} : "
        
    output = output[:-3]
    print(output)

def breed(genotype_1: str, genotype_2: str):
    """Prints the results of breeding two genotypes to the screen"""
    
    def process_genotype(genotype: str) -> List[str]:
        """Processes the genotype, printing its genes, alleles and gametes to the screen. Returns the list of gametes"""
    
        print(f"Genotype: {genotype}")

        genes = get_genes(genotype)
        alleles = get_alleles(genes)

        gametes = list()
        get_gametes(alleles, 0, "", gametes)

        print(f"Genes: {genes}")
        print(f"Alleles: {alleles}")
        print(f"Gametes: {gametes}")
        print()
        
        return gametes
    
    gametes_1 = process_genotype(genotype_1)
    gametes_2 = process_genotype(genotype_2)
    
    children_genotypes = get_gamete_combinations(gametes_1, gametes_2)
    print(f"Children genotypes: {children_genotypes}")
    
    unique_genotypes = get_unique_genotypes(children_genotypes)
    print_unique_genotypes(unique_genotypes)

if sys.argv[1] in {"-h", "--help"}:
    print("USAGE: interbreeder.py <Genome1> <Genome2>")
else:
    genotypes = sys.argv[1], sys.argv[2]
    breed(*genotypes)
