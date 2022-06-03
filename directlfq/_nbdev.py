# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"run_lfq": "01_lfq_manager.ipynb",
         "save_protein_df": "01_lfq_manager.ipynb",
         "save_ion_df": "01_lfq_manager.ipynb",
         "get_normfacts": "02_normalization.ipynb",
         "set_samples_with_only_single_intensity_to_nan": "02_normalization.ipynb",
         "apply_sampleshifts": "02_normalization.ipynb",
         "get_bestmatch_pair": "02_normalization.ipynb",
         "create_distance_matrix": "02_normalization.ipynb",
         "calc_distance": "02_normalization.ipynb",
         "calc_nanvar": "02_normalization.ipynb",
         "calc_nanmedian": "02_normalization.ipynb",
         "update_distance_matrix": "02_normalization.ipynb",
         "get_fcdistrib": "02_normalization.ipynb",
         "determine_anchor_and_shift_sample": "02_normalization.ipynb",
         "shift_samples": "02_normalization.ipynb",
         "get_total_shift": "02_normalization.ipynb",
         "merge_distribs": "02_normalization.ipynb",
         "normalize_dataframe_between_samples": "02_normalization.ipynb",
         "normalize_ion_profiles": "02_normalization.ipynb",
         "drop_nas_if_possible": "02_normalization.ipynb",
         "calculate_fraction_with_no_NAs": "02_normalization.ipynb",
         "SampleNormalizationManager": "02_normalization.ipynb",
         "SampleShifterLinear": "02_normalization.ipynb",
         "estimate_protein_intensities": "03_protein_intensity_estimation.ipynb",
         "get_protein_profile_from_shifted_peptides": "03_protein_intensity_estimation.ipynb",
         "get_list_with_protein_value_for_each_sample": "03_protein_intensity_estimation.ipynb",
         "ProtvalCutter": "03_protein_intensity_estimation.ipynb",
         "get_samples_used_from_samplemap_file": "04_utils.ipynb",
         "get_samples_used_from_samplemap_df": "04_utils.ipynb",
         "get_all_samples_from_samplemap_df": "04_utils.ipynb",
         "get_samplenames_from_input_df": "04_utils.ipynb",
         "filter_df_to_minrep": "04_utils.ipynb",
         "get_condpairname": "04_utils.ipynb",
         "get_quality_score_column": "04_utils.ipynb",
         "make_dir_w_existcheck": "04_utils.ipynb",
         "get_results_plot_dir_condpair": "04_utils.ipynb",
         "get_middle_elem": "04_utils.ipynb",
         "get_nonna_array": "04_utils.ipynb",
         "get_non_nas_from_pd_df": "04_utils.ipynb",
         "get_ionints_from_pd_df": "04_utils.ipynb",
         "invert_dictionary": "04_utils.ipynb",
         "get_z_from_p_empirical": "04_utils.ipynb",
         "count_fraction_outliers_from_expected_fc": "04_utils.ipynb",
         "create_or_replace_folder": "04_utils.ipynb",
         "write_chunk_to_file": "04_utils.ipynb",
         "index_and_log_transform_input_df": "04_utils.ipynb",
         "get_relevant_columns": "04_utils.ipynb",
         "get_relevant_columns_config_dict": "04_utils.ipynb",
         "get_quant_ids_from_config_dict": "04_utils.ipynb",
         "get_sample_ids_from_config_dict": "04_utils.ipynb",
         "get_channel_ids_from_config_dict": "04_utils.ipynb",
         "load_config": "04_utils.ipynb",
         "get_type2relevant_cols": "04_utils.ipynb",
         "filter_input": "04_utils.ipynb",
         "merge_protein_and_ion_cols": "04_utils.ipynb",
         "merge_protein_cols_and_ion_dict": "04_utils.ipynb",
         "get_quantitative_columns": "04_utils.ipynb",
         "get_ionname_columns": "04_utils.ipynb",
         "adapt_headers_on_extended_df": "04_utils.ipynb",
         "split_extend_df": "04_utils.ipynb",
         "add_merged_ionnames": "04_utils.ipynb",
         "reformat_and_write_longtable_according_to_config": "04_utils.ipynb",
         "adapt_subtable": "04_utils.ipynb",
         "process_with_dask": "04_utils.ipynb",
         "reshape_input_df": "04_utils.ipynb",
         "sort_and_add_columns": "04_utils.ipynb",
         "extend_sample_allcolumns_for_plexdia_case": "04_utils.ipynb",
         "adapt_input_df_columns_in_case_of_plexDIA": "04_utils.ipynb",
         "extend_sampleID_column_for_plexDIA_case": "04_utils.ipynb",
         "set_mtraq_reduced_ion_column_into_dataframe": "04_utils.ipynb",
         "remove_mtraq_modifications_from_ion_ids": "04_utils.ipynb",
         "is_plexDIA_table": "04_utils.ipynb",
         "parse_channel_from_peptide_column": "04_utils.ipynb",
         "merge_sample_id_and_channels": "04_utils.ipynb",
         "merge_channel_and_sample_string": "04_utils.ipynb",
         "reformat_and_write_wideformat_table": "04_utils.ipynb",
         "check_for_processed_runs_in_results_folder": "04_utils.ipynb",
         "import_data": "04_utils.ipynb",
         "reformat_and_save_input_file": "04_utils.ipynb",
         "add_ion_protein_headers_if_applicable": "04_utils.ipynb",
         "get_input_type_and_config_dict": "04_utils.ipynb",
         "get_original_file_from_aq_reformat": "04_utils.ipynb",
         "import_config_dict": "04_utils.ipynb",
         "load_samplemap": "04_utils.ipynb",
         "prepare_loaded_tables": "04_utils.ipynb",
         "LongTableReformater": "04_utils.ipynb",
         "AcquisitionTableHandler": "04_utils.ipynb",
         "AcquisitionTableInfo": "04_utils.ipynb",
         "AcquisitionTableHeaders": "04_utils.ipynb",
         "AcquisitionTableOutputPaths": "04_utils.ipynb",
         "AcquisitionTableReformater": "04_utils.ipynb",
         "AcquisitionTableHeaderFilter": "04_utils.ipynb",
         "merge_acquisition_df_parameter_df": "04_utils.ipynb",
         "plot_withincond_fcs": "04_utils.ipynb",
         "plot_lines": "12_benchmarking.ipynb",
         "plot_points": "12_benchmarking.ipynb",
         "get_tps_fps": "12_benchmarking.ipynb",
         "annotate_dataframe": "12_benchmarking.ipynb",
         "compare_to_reference": "12_benchmarking.ipynb",
         "compare_normalization": "12_benchmarking.ipynb",
         "print_nonref_hits": "12_benchmarking.ipynb",
         "ResultsTable": "12_benchmarking.ipynb",
         "ResultsTableDirectLFQ": "12_benchmarking.ipynb",
         "ResultsTableMaxQuant": "12_benchmarking.ipynb",
         "OrganismAnnotator": "12_benchmarking.ipynb",
         "OrganismAnnotatorMaxQuant": "12_benchmarking.ipynb",
         "OrganismAnnotatorSpectronaut": "12_benchmarking.ipynb",
         "OrganismAnnotatorDIANN": "12_benchmarking.ipynb",
         "PlotConfig": "12_benchmarking.ipynb",
         "MultiOrganismIntensityFCPlotter": "12_benchmarking.ipynb",
         "InputDFCreator": "12_benchmarking.ipynb",
         "TimedLFQRun": "12_benchmarking.ipynb",
         "RuntimeInfo": "12_benchmarking.ipynb",
         "LFQTimer": "12_benchmarking.ipynb",
         "TestFileDownloader": "13_testfile_handling.ipynb",
         "DownloadLinkConverter": "13_testfile_handling.ipynb"}

modules = ["lfq_manager.py",
           "normalization.py",
           "protein_intensity_estimation.py",
           "utils.py",
           "benchmarking.py",
           "testfile_handling.py"]

doc_url = "https://ammarcsj.github.io/directlfq/"

git_url = "https://github.com/ammarcsj/directlfq/tree/master/"

def custom_doc_links(name): return None
