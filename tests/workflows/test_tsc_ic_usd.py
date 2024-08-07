import os
from argparse import Namespace

import pandas as pd

from mawpy.constants import (USER_ID, UNIX_START_T, UNIX_START_DATE, ORIG_LAT, ORIG_LONG, ORIG_UNC, STAY_LAT, STAY_LONG,
                             STAY, STAY_DUR)
from mawpy.workflows.tsc_ic_usd import tsc_ic_usd


def test_tsc_ic_usd(tmp_path):
    input_file = os.path.dirname(__file__) + '/../resources/test_input.csv'
    output_file = os.path.join(tmp_path, 'test_output_workflow_tsc_ic_usd.csv')

    # Run the workflow to be tested and get the output
    actual_output_df = tsc_ic_usd(input_file, output_file, 1, 1, 300, 0, 300)

    # Check if output file was created
    assert os.path.exists(output_file)
    expected_output_df = pd.read_csv(os.path.dirname(__file__)
                                     + '/../resources/tsc_ic_usd_output_for_test_input.csv')

    # Assert if the expected_output_df equal to actual_output_df
    pd.testing.assert_frame_equal(actual_output_df, expected_output_df, check_like=True)

    # List of columns expected in the actual_output_df
    expected_output_columns = [USER_ID, UNIX_START_T, UNIX_START_DATE,
                               ORIG_LAT, ORIG_LONG, ORIG_UNC,
                               STAY_LAT, STAY_LONG,
                               STAY_DUR, STAY]

    # Check if all the expected columns are present in the workflow output columns
    assert len(list(set(expected_output_columns) & set(actual_output_df.columns))) == len(expected_output_columns)

    # Check if output file was written successfully
    assert os.path.exists(output_file)
