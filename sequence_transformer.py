"""
This script transforms a DNA sequence (composed of nucleotides A, T, C, G) 
into its corresponding RNA sequence (U, A, G, C).
"""

def transform_sequence(sequence):
    """Transforms a DNA sequence into an RNA sequence."""
    transformations = {
        'C': 'G',
        'T': 'A',
        'A': 'U',
        'G': 'C'
    }
    
    return ''.join([transformations[nucleotide] for nucleotide in sequence])

if __name__ == "__main__":
    sequence = input("Please enter the DNA sequence: ")

    if all(nucleotide in ['A', 'T', 'C', 'G'] for nucleotide in sequence):
        print("transform sequence: ")
        print(transform_sequence(sequence))
    else:
        print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, and G.")
