# CorEvol

CorEvol is a lightweight Python pipeline to calculate ω (dN/dS) values for the core genome of multiple genomic CDS sequences of closely related micro-organisms. The general workflow is described in the flowchart below.

## Table of Contents
- [General Info](#general-info)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## General Info
CorEvol processes a folder of your genomic CDS files and outputs the ω (dN/dS) values of the core, non-redundant, non-recombinant sequences, along with other useful files and folders. See [Usage](#usage) for more details.

```mermaid
graph LR
    subgraph Input Files
        A[seq1.fna, seq2.fna, ..., seqN.fna]
    end
    A --> B((Clustering<br/>&<br/>Redundancy removal))
    B --> C[Core Clusters]
    C --> X((Alignment))
    X --> Y[Aligned Core Clusters]
    Y --> D((Recombination<br/>Detection))
    D --> E[Recombinant Seqs.]
    D --> F[Non Recombinant Seqs.]
    F --> G[ω of core,<br/>non-redundant,<br/>non-recombinant<br/>clusters]
```


## Installation
The latest version of CorEvol is available [here](https://github.com/AbhishakeL/CorEvol)


1. Create a conda environment.
```
conda create -n CorEvol -c conda-forge h5py==3.8.0 numpy scipy python=3.10
conda activate CorEvol
```
2. Install OpenRDP in the said environment. Find details [here](https://github.com/PoonLab/OpenRDP/tree/master)
```
git clone https://github.com/PoonLab/OpenRDP
cd OpenRDP/
pip3 install -e .
cd ..
```
3. Install SPYDER in the said environment.
```
conda install anaconda::spyder
```
5. Install CorEvol.
```
conda install abhishakel::corevol
```
## Usage
To use CorEvol, run the following command to get to know of all the available parameters and options:
```
python CorEvol.py -h
```
Usage options:
```
python CorEvol.py -h
usage: CorEvol.py [-h] -i DIRECTORY -o OUTPUT [-p PATH] [-c IDENTITY]
                  [-d LENGTH_DIFF] [-sc LENGTH_CUTOFF] [-aL ALIGN_COV_LONG]
                  [-aS ALIGN_COV_SHORT] [-g MEMORY] [-n WORD_LENGTH]
                  [-pC PHYLOGENY_CUTOFF] [-r RDP_CONFIG] [-x COUNTS]
                  [-t THREADS]

Pipeline for running CorEvol.

options:
  -h, --help            show this help message and exit
  -i DIRECTORY, --directory DIRECTORY
                        Directory containing the FASTA files
  -o OUTPUT, --output OUTPUT
                        Directory containing the output files
  -p PATH, --path PATH  Path where the cdhit program is located
  -c IDENTITY, --identity IDENTITY
                        Sequence identity threshold (default: 0.9)
  -d LENGTH_DIFF, --length_diff LENGTH_DIFF
                        Length difference cutoff (default: 0)
  -sc LENGTH_CUTOFF, --length_cutoff LENGTH_CUTOFF
                        Length difference cutoff in amino acid (default: 1)
  -aL ALIGN_COV_LONG, --align_cov_long ALIGN_COV_LONG
                        Alignment coverage for longer sequence (default: 0.9)
  -aS ALIGN_COV_SHORT, --align_cov_short ALIGN_COV_SHORT
                        Alignment coverage for shorter sequence (default: 0.9)
  -g MEMORY, --memory MEMORY
                        Maximum available memory in GB (default: 1)
  -n WORD_LENGTH, --word_length WORD_LENGTH
                        Word length (default: 9)
  -pC PHYLOGENY_CUTOFF, --phylogeny_cutoff PHYLOGENY_CUTOFF
                        Minimum length of nucleotides prior to alignment
                        (default : 300)
  -r RDP_CONFIG, --rdp_config RDP_CONFIG
                        Path where internal parameters of RDP scanner is saved
  -x COUNTS, --counts COUNTS
                        Number of different RDP testing methodology used to
                        confidently conclude a sequence to be recombinant
                        (default: 4, max: 6)
  -t THREADS, --threads THREADS
                        Number of threads (default: 4)
```
### Typical Usage
We strongy recommend running `CorEvol.py` from SPYDER Ipython terminal. This recommendation is mostly to circumnavigate a bug in the `codeml` package.
```
%run CorEvol.py -i ./Test -o ~/Out
```
The output folder contains the following files and folders.
| Name|Type|Content |
| --- | --- | --- |
| Neutral_Selection| Directory | A directory containing all the cluster of sequences that have undergone neutral selection event|
| NonRecombination_files | Directory | A directory containing `_results.csv : Recombination detection output file`, `_formatted.phy` and `_tree.nwk` files needed to run `codeml` for each of the clusters where recombination is not detected|
| Positive_Selection | Directory | A directory containing all the cluster of sequences that have undergone positive selection event|
| Purifying_Selection | Directory | A directory containing all the cluster of sequences that have undergone negative selection event|
| Recombination_Clusters | Directory | A directory containing `_results.csv : Recombination detection output file` for each of the clusters where recombination is detected|
| concatenated_seq.aln | File | ClustalW format alignment file for all the core, non-redundant, non-recombinant sequences, joined end to end | 
| concatenated_seq.fas | File | FASTA format alignment file for all the core, non-redundant, non-recombinant sequences, joined end to end | 
| Pan_matrix.xlsx | File | CD-HIT output, generated in a matrix format such that each row represent Cluster number and each column represent each sample. Background color of each row selected such that green represent ω >= 1,blue represent ω = 0, red represent ω < 1. Those without color are non-core/recombinant clusters|
| RDP_error.tsv | File | Cluster numbers for which Recombination could not be detected because there were less than three unique sequences in the cluster |
| Selection_table.tsv | File | A matrix with ω value for the clusters |

## License
This project is licensed under the GNU GPLv3 License. See the LICENSE file for details.
```
This README file includes more detailed instructions for installation and usage, and it ensures that the content is well-organized and easy to follow.
```
