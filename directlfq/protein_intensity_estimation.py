# AUTOGENERATED! DO NOT EDIT! File to edit: 03_protein_intensity_estimation.ipynb (unless otherwise specified).

__all__ = ['estimate_protein_intensities', 'get_list_of_tuple_w_protein_profiles_and_shifted_peptides',
           'get_ion_intensity_dataframe_from_list_of_shifted_peptides',
           'get_protein_dataframe_from_list_of_protein_profiles', 'calculate_peptide_and_protein_intensities',
           'get_protein_profile_from_shifted_peptides', 'get_list_with_protein_value_for_each_sample', 'ProtvalCutter']

# Cell
import pandas as pd
import numpy as np
import directlfq.normalization as lfqnorm
import multiprocessing
import functools

def estimate_protein_intensities(normed_df, min_nonan, num_samples_quadratic):
    "derives protein pseudointensities from between-sample normalized data"

    allprots = normed_df.index.get_level_values(0).unique()

    list_of_tuple_w_protein_profiles_and_shifted_peptides = get_list_of_tuple_w_protein_profiles_and_shifted_peptides(allprots, normed_df, num_samples_quadratic, min_nonan)
    protein_df2 = get_protein_dataframe_from_list_of_protein_profiles(allprots=allprots, list_of_tuple_w_protein_profiles_and_shifted_peptides=list_of_tuple_w_protein_profiles_and_shifted_peptides, normed_df= normed_df)
    ion_df2 = get_ion_intensity_dataframe_from_list_of_shifted_peptides(list_of_tuple_w_protein_profiles_and_shifted_peptides)

    return protein_df2, ion_df2



def get_list_of_tuple_w_protein_profiles_and_shifted_peptides(allprots, normed_df, num_samples_quadratic, min_nonan):
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool()
    print(f"using {pool._processes} processes")
    list_of_tuple_w_protein_profiles_and_shifted_peptides = pool.map(functools.partial(calculate_peptide_and_protein_intensities,  allprots = allprots,normed_df = normed_df,
    num_samples_quadratic = num_samples_quadratic, min_nonan = min_nonan),range(len(allprots)))
    pool.close()

    return list_of_tuple_w_protein_profiles_and_shifted_peptides

def get_ion_intensity_dataframe_from_list_of_shifted_peptides(list_of_tuple_w_protein_profiles_and_shifted_peptides):
    ion_ints = [x[1] for x in list_of_tuple_w_protein_profiles_and_shifted_peptides]
    ion_df = 2**pd.concat(ion_ints)
    ion_df = ion_df.replace(np.nan, 0)
    return ion_df


def get_protein_dataframe_from_list_of_protein_profiles(allprots, list_of_tuple_w_protein_profiles_and_shifted_peptides, normed_df):
    index_list = []
    profile_list = []

    list_of_protein_profiles = [x[0] for x in list_of_tuple_w_protein_profiles_and_shifted_peptides]

    for idx in range(len(allprots)):
        if list_of_protein_profiles[idx] is None:
            continue
        index_list.append(allprots[idx])
        profile_list.append(list_of_protein_profiles[idx])

    index_for_protein_df = pd.Index(data=index_list, name="protein")
    protein_df = 2**pd.DataFrame(profile_list, index = index_for_protein_df, columns = normed_df.columns)
    protein_df = protein_df.replace(np.nan, 0)
    return protein_df

def calculate_peptide_and_protein_intensities(idx, allprots,normed_df , num_samples_quadratic, min_nonan):
    if(idx%100 ==0):
        print(f"prot {idx} of {len(allprots)}")
    protein = allprots[idx]
    peptide_intensity_df = pd.DataFrame(normed_df.loc[protein]).copy()#DataFrame definition to avoid pandas Series objects
    peptide_intensity_df = ProtvalCutter(peptide_intensity_df, maximum_df_length=100).get_dataframe()
    summed_pepint = np.nansum(2**peptide_intensity_df)

    if(peptide_intensity_df.shape[1]<2):
        shifted_peptides = peptide_intensity_df
    else:
        shifted_peptides = lfqnorm.NormalizationManagerProtein(peptide_intensity_df, num_samples_quadratic = num_samples_quadratic).complete_dataframe

    protein_profile = get_protein_profile_from_shifted_peptides(shifted_peptides, summed_pepint, min_nonan)

    return protein_profile, shifted_peptides


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

