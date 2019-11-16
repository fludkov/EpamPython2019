""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt -
в нем содержится таблица переводов кодонов РНК в аминокислоту,
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что,
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
dna = "files/dna.fasta"
rna_file = "files/output/rna.fasta"
codon_file = "files/output/codon.fasta"
rna_codon_table = "files/rna_codon_table.txt"
dna_count = "files/output/dna_count_nucleotides.txt"


def translate_from_dna_to_rna(dna):

    """The function returns dictionary
    of {Gene : RNA Nucleotide Sequence} from DNA file"""

    rna = {}
    dna_dict = create_dict_from_fasta_file(dna)
    # Create RNA dictionary {Gene : RNA Nucleotide Sequence}
    for gene in dna_dict:
        rna[gene] = dna_dict[gene].replace("T", "U")
    # Write RNA to the rna.fasta
    with open(rna_file, "w") as rna_file_op:
        for gene in rna:
            rna_file_op.write(f">{gene}\n")
            rna_file_op.write(f"{rna[gene]}")
    return rna


def count_nucleotides(dna):

    """The function returns dict {Gene:
    list of count its nucleotides}
    And also creates dna_count_nucleotides.txt file"""

    dna_dict = create_dict_from_fasta_file(dna)
    num_of_nucleotides = {}
    # Count of each nucleotide for every gene in DNA
    for gene in dna_dict:
        a_count = dna_dict[gene].count("A")
        c_count = dna_dict[gene].count("C")
        g_count = dna_dict[gene].count("G")
        t_count = dna_dict[gene].count("T")
        num_of_nucleotides[gene] = [f"A - {a_count}", f"C - {c_count}",
                                    f"G - {g_count}", f"T - {t_count}"]
    # Write results to the file
    with open(dna_count, "w") as dna_count_nucleotides_file:
        for gene in num_of_nucleotides:
            dna_count_nucleotides_file.write(f"{gene}\n")
            dna_count_nucleotides_file.\
                write(f"{str(num_of_nucleotides[gene])}\n\n")

    return num_of_nucleotides


def translate_rna_to_protein(rna):

    """The function returns dict {Gene: codon sequence}
    And also creates codon.fasta file"""

    protein = {}
    # Get rna_dict from rna fasta file for each gene
    rna_dict = create_dict_from_fasta_file(rna)
    # Get rna_codon_dict from rna_codon_table
    rna_codon_dict = create_dict_from_codon_table(rna_codon_table)
    for gene in rna_dict:
        protein_value = ""
        nucleotide_consequence = rna_dict[gene].replace("\n", "")
        # Create a list of nucleotide sequence value splitted
        # by chunks of 3 symbols
        gene_chunks_list = split_string_by_chunks(nucleotide_consequence, 3)
        # Iterate each chunk and get new codon sequence
        # with mapping to rna_codon_dict
        for codon in gene_chunks_list:
            if codon in rna_codon_dict:
                protein_value += rna_codon_dict[codon]
            else:
                protein_value += codon
        # Write protein value to the protein for each gene
        protein[gene] = protein_value
    # Create new codon.fasta file from protein
    with open(codon_file, "w") as codon_file_op:
        for gene in protein:
            codon_file_op.write(f">{gene}\n")
            # Create a list of codon sequence value splitted by chunks of 75
            # symbols as fasta file can't contain stings more than 75 symbols
            lines_to_print = split_string_by_chunks(protein[gene], 75)
            for line in lines_to_print:
                codon_file_op.write(f"{line}\n")
    return protein


def create_dict_from_fasta_file(dna):

    """The function returns dictionary of {Gene : DNA/RNA Nucleotide Sequence}
    from DNA/RNA file. NOTE: DNA/RNA may contain any count of gene sequences"""

    indexes = []
    # Get list of indexes where DNA/RNA gene starts
    with open(dna) as fasta_file:
        fasta_file_list = fasta_file.readlines()
    for i, line in enumerate(fasta_file_list):
        if line.startswith(">"):
            indexes.append(i)
    fasta_dict = {}
    # Create DNA/RNA dictionary according to the indexes
    # ZIP indexes for reffering to previous index
    for a, b in zip(indexes, indexes[1:]):
        fasta_dict[fasta_file_list[a].replace("\n", "").replace(">", "")] = \
            ''.join(fasta_file_list[a+1:b])
        # If the last indexe is reached, add the last gene dict pair
        gene = fasta_file_list[b].replace("\n", "").replace(">", "")
        if b == indexes[len(indexes)-1]:
            fasta_dict[gene] = ''.join(fasta_file_list[b + 1:])
    return fasta_dict


def create_dict_from_codon_table(codon_table):

    """This function returns dictionary of mapped {rna sequence: codon}
    from rna_codon_table.txt file"""

    rna_codon_dict = {}
    rna_codon_line_list = []
    # Open rna_codon_table file, read its lines
    # and add to the rna_codon_line_list
    with open(codon_table) as rna_codon_table_file:
        for line in rna_codon_table_file.readlines():
            rna_codon_line_list.append(line.replace("\n", " ").split("      "))
    # Parse each element in the rna_codon_line_list
    for line in rna_codon_line_list:
        for codon_pair in line:
            # Here is exception for elements containing 'Stop' value
            # as it has different format
            if "Stop" in codon_pair:
                temp_list1 = codon_pair.split(" Stop   ")
                temp_list2 = temp_list1[1].split(" ")
                rna_codon_dict[temp_list1[0]] = "Stop"
                rna_codon_dict[temp_list2[0]] = temp_list2[1]
            else:
                rna_codon_dict[codon_pair[:3]] = codon_pair[3:].strip()
    return rna_codon_dict


def split_string_by_chunks(sequence: str, chunk_number: int) -> list:

    """This function returns list of string elements splitted by chunks number
    For instance: split_string_by_chunks('aabbc', 2) will
    return ['aa', 'bb', 'c']"""

    return [sequence[i:i+chunk_number]
            for i in range(0, len(sequence), chunk_number)]


count_nucleotides(dna)
translate_from_dna_to_rna(dna)
translate_rna_to_protein(rna_file)
