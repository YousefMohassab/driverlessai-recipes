"""
Pull data >1Gb from GCP Bigquery using sharding functionality.
Based on:
    https://cloud.google.com/bigquery/docs/exporting-data#exporting_table_data
    https://cloud.google.com/storage/docs/reference/libraries#using_the_client_library

Author: Travis Couture
Created: 03/18/2020
Last Updated: 03/18/2020
"""

import datatable as dt
import os
from h2oaicore.data import CustomData
from h2oaicore.systemutils import config
from google.cloud import bigquery
from google.cloud import storage
from functools import reduce


# Please fill before usage
# Note that this information is logged in Driverless AI logs.

# GCP Storage bucket name
BUCKET_NAME = ''
# GCP project name
PROJECT = ''
# Dataset ID/name in GCP Bigquery without project and table prefixes
DATASET_ID = ''
# Table ID in GCP Bigquery without project prefix
TABLE_ID = ''
# Pattern to use to shard data from Bigquery into GCP Storage e.g. 'my-big-data/shard-pattern-*.csv'
WILDCARD_NAME = ''
# GCP region e.g. 'US'
LOCATION = ''
# Data directory for Driverless AI e.g. '/data'
DAI_DATA_PATH = ''


class BqShardData(CustomData):

    @staticmethod
    def create_data(X: dt.Frame = None) -> dt.Frame:
        if not BUCKET_NAME:
            return []

        sa_json = config.gcs_path_to_service_account_json

        if sa_json.split('.')[-1] == 'json':
            s_client = storage.Client.from_service_account_json(sa_json)
            bq_client = bigquery.Client.from_service_account_json(sa_json)
        else:
            s_client = storage.Client()
            bq_client = bigquery.Client()

        destination_uri = 'gs://{}/{}'.format(BUCKET_NAME, WILDCARD_NAME)
        dataset_ref = bq_client.dataset(DATASET_ID, project=PROJECT)
        table_ref = dataset_ref.table(TABLE_ID)

        extract_job = bq_client.extract_table(table_ref,
                                              destination_uri,
                                              location=LOCATION)

        extract_job.result()

        shard_count = extract_job.destination_uri_file_counts[0]
        shard_name_prefix = WILDCARD_NAME.split('*')[0]
        shard_filetype = WILDCARD_NAME.split('*')[-1]
        shard_list = [shard_name_prefix + str(i).zfill(12) + shard_filetype for i in range(0, shard_count)]

        shard_dts = []

        for shard_name in shard_list:
            shard_file_path = os.path.join(DAI_DATA_PATH, shard_name.split('/')[-1])
            bucket = s_client.bucket(BUCKET_NAME)
            blob = bucket.blob(shard_name)
            blob.download_to_filename(shard_file_path)
            shard_dts.append(dt.fread(shard_file_path))
            os.remove(shard_file_path)

        shard_dts[0].rbind(shard_dts[1:])

        X = shard_dts[0]

        return X
