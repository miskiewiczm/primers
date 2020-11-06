import pandas as pd

data = pd.read_csv("primers.csv")

data_sort = data.sort_values(by=["any_th","3p_th","hairpin_th","gc_per","tm"])

data_sort.to_csv("primers_sorted.csv")

