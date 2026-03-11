from re import M
import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    matches_df = anon_df.merge(aux_df, on=["age", "gender", "zip3"], how="inner")
    new_df = matches_df[["anon_id", "name"]]
    new_df.columns = [["anon_id", "matched_name"]]
    new_df.drop_duplicates(inplace=True)
    return new_df

def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    print(len(matches_df), len(anon_df))
    counts = matches_df['anon_id'].value_counts()
    unique_matches = (counts == 1).sum()
    return unique_matches / len(anon_df)