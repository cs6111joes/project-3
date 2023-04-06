import pandas as pd
import sys

# Get file name, minimum support, and minimum confidence
FILE = sys.argv[1]     
MIN_SUP = sys.argv[2]
MIN_CONF = sys.argv[3]


# takes as an argument Lk-1
# the set of all large (k-1) itemsets
def generate_apriori_candidates():

    print('Apriori Candidate Generation')

    # join Lk-1 with Lk-1
    
    # INSERT into Ck 
    # SELECT p.item1, p.item2 ... p.itemk-1, q.itemk-1
    # FROM Lk-1 P, Lk-1 Q
    # WHERE p.item1 = q.item1, ... p.itemk-2 = q.itemk-2
    # p.itemk-1 < q.itemk-1
     
def prune_apriori_candidates():

    print('Pruning')

    # delete all itemsets such that some (k-1) subset of C
    # is not in Lk-1


def clean_file(df):

    # Assuming we will need to do some cleaning on the data
    print('Cleaning dataframe')

def apriori_algorithm(L1, df):

    generate_apriori_candidates()
    prune_apriori_candidates()

# generate L1, the large 1-itemset
def generate_L1(df):

    L1 = []

    for column in df.columns:

        L1.extend(df[column].unique())

    return L1

def main():

    # Read CSV info dataframe
    df = pd.read_csv(FILE)
    clean_file(df)

    L1 = generate_L1(df)
    print('L1: \n', L1)
    apriori_algorithm(L1, df)



main()