# AUTOGENERATED! DO NOT EDIT! File to edit: 03_protein_intensity_estimation.ipynb (unless otherwise specified).

__all__ = ['estimate_protein_intensities', 'get_protein_profile_from_shifted_peptides',
           'get_list_with_protein_value_for_each_sample', 'ProtvalCutter']

# Cell
import pandas as pd
import numpy as np
import directlfq.normalization as lfqnorm

def estimate_protein_intensities(normed_df, min_nonan, maximum_df_length):
    "derives protein pseudointensities from between-sample normalized data"
    prot_ints = []
    ion_ints = []

    count_prots = 1
    allprots = normed_df.index.get_level_values(0).unique()
    quantified_prots = []

    for protein in allprots:
        if(count_prots%100 ==0):
            print(f"prot {count_prots} of {len(allprots)}")
        count_prots+=1

        protvals = pd.DataFrame(normed_df.loc[protein]).copy()#DataFrame definition to avoid pandas Series objects
        protvals = ProtvalCutter(protvals, maximum_df_length=maximum_df_length).get_dataframe()
        summed_pepint = np.nansum(2**protvals)

        if(protvals.shape[1]<2):
            normed_protvals = protvals
        else:
            normed_protvals = lfqnorm.normalize_ion_profiles(protvals)

        ion_ints.append(normed_protvals)
        scaled_vec = get_protein_profile_from_shifted_peptides(normed_protvals, summed_pepint, min_nonan)
        if scaled_vec is not None:
            prot_ints.append(scaled_vec)
            quantified_prots.append(protein)


    index_for_protein_df = pd.Index(data=quantified_prots, name="protein")
    protein_df = 2**pd.DataFrame(prot_ints, index = index_for_protein_df, columns = normed_df.columns)
    protein_df = protein_df.replace(np.nan, 0)

    ion_df = 2**pd.concat(ion_ints)
    ion_df = ion_df.replace(np.nan, 0)
    return protein_df, ion_df

# Cell
def get_protein_profile_from_shifted_peptides(normalized_peptide_profile_df, summed_pepints, min_nonan):
    intens_vec = get_list_with_protein_value_for_each_sample(normalized_peptide_profile_df, min_nonan)
    intens_vec = np.array(intens_vec)
    summed_intensity = np.nansum(2**intens_vec)
    if summed_intensity == 0: #this means all elements in intens vec are nans
        return None
    intens_conversion_factor = summed_pepints/summed_intensity
    scaled_vec = intens_vec+np.log2(intens_conversion_factor)
    return scaled_vec

def get_list_with_protein_value_for_each_sample(normalized_peptide_profile_df, min_nonan):
    intens_vec = []
    for sample in normalized_peptide_profile_df.columns:
        reps = normalized_peptide_profile_df.loc[:,sample].to_numpy()
        nonan_elems = sum(~np.isnan(reps))
        if(nonan_elems>=min_nonan):
            intens_vec.append(np.nanmedian(reps))
        else:
            intens_vec.append(np.nan)
    return intens_vec


# Cell
import pandas as pd

class ProtvalCutter():
    def __init__(self, protvals_df, maximum_df_length = 100):
        self._protvals_df = protvals_df
        self._maximum_df_length = maximum_df_length
        self._dataframe_too_long = None
        self._sorted_idx = None
        self._check_if_df_too_long_and_sort_index_if_so()


    def _check_if_df_too_long_and_sort_index_if_so(self):
        self._dataframe_too_long =len(self._protvals_df.index)>self._maximum_df_length
        if self._dataframe_too_long:
            self._determine_nansorted_df_index()

    def _determine_nansorted_df_index(self):
        idxs = self._protvals_df.index
        self._sorted_idx =  sorted(idxs, key= lambda idx : self._get_num_nas_in_row(self._protvals_df.loc[idx]))

    @staticmethod
    def _get_num_nas_in_row(row):
        return sum(np.isnan(row.to_numpy()))


    def get_dataframe(self):
        if self._dataframe_too_long:
            return self._get_shortened_dataframe()
        else:
            return self._protvals_df

    def _get_shortened_dataframe(self):
        shortened_index = self._sorted_idx[:self._maximum_df_length]
        return self._protvals_df.loc[shortened_index]

