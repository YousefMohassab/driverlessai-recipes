# Recipes for H2O Driverless AI

 * [data](./data)
   * [taxi_small.csv](./data/taxi_small.csv)
   * [weather_missing.csv](./data/weather_missing.csv)
 * [models](./models)
   * [catboost.py](./models/catboost.py)
   * [h2o-3-models.py](./models/h2o-3-models.py)
   * [historic_mean.py](./models/historic_mean.py)
   * [knearestneighbour.py](./models/knearestneighbour.py)
   * [lightgbm_with_custom_loss.py](./models/lightgbm_with_custom_loss.py)
   * [linear_svm.py](./models/linear_svm.py)
   * [xgboost_with_custom_loss.py](./models/xgboost_with_custom_loss.py)
 * [recipes](./recipes)
   * [amazon.py](./recipes/amazon.py)
 * [scorers](./scorers)
   * [average_mcc.py](./scorers/average_mcc.py)
   * [brier_loss.py](./scorers/brier_loss.py)
   * [cost.py](./scorers/cost.py)
   * [explained_variance.py](./scorers/explained_variance.py)
   * [false_discovery_rate.py](./scorers/false_discovery_rate.py)
   * [hamming_loss.py](./scorers/hamming_loss.py)
   * [huber_loss.py](./scorers/huber_loss.py)
   * [largest_error.py](./scorers/largest_error.py)
   * [mean_absolute_percentage_deviation.py](./scorers/mean_absolute_percentage_deviation.py)
   * [mean_absolute_scaled_error.py](./scorers/mean_absolute_scaled_error.py)
   * [median_absolute_error.py](./scorers/median_absolute_error.py)
   * [pearson_correlation.py](./scorers/pearson_correlation.py)
   * [precision.py](./scorers/precision.py)
   * [quadratic_weighted_kappa.py](./scorers/quadratic_weighted_kappa.py)
   * [recall.py](./scorers/recall.py)
   * [top_decile.py](./scorers/top_decile.py)
 * [transformers](./transformers)
     * [augmentation](./transformers/augmentation)
       * [france_bank_holidays.py](./transformers/augmentation/france_bank_holidays.py)
       * [is_ramadan.py](./transformers/augmentation/is_ramadan.py)
       * [singapore_public_holidays.py](./transformers/augmentation/singapore_public_holidays.py)
     * [datetime](./transformers/datetime)
       * [datetime_diff_transformer.py](./transformers/datetime/datetime_diff_transformer.py)
       * [datetime_encoder_transformer.py](./transformers/datetime/datetime_encoder_transformer.py)
       * [days_until_dec2020.py](./transformers/datetime/days_until_dec2020.py)
       * [parse_excel_date_transformer.py](./transformers/datetime/parse_excel_date_transformer.py)
     * [generic](./transformers/generic)
       * [count_missing_values_transformer.py](./transformers/generic/count_missing_values_transformer.py)
       * [specific_column_transformer.py](./transformers/generic/specific_column_transformer.py)
     * [geospatial](./transformers/geospatial)
       * [geodesic.py](./transformers/geospatial/geodesic.py)
       * [myhaversine.py](./transformers/geospatial/myhaversine.py)
     * [how_to_debug_transformer.py](./transformers/how_to_debug_transformer.py)
     * [how_to_test_from_py_client.py](./transformers/how_to_test_from_py_client.py)
     * [image](./transformers/image)
       * [image_url_transformer.py](./transformers/image/image_url_transformer.py)
     * [nlp](./transformers/nlp)
       * [fuzzy_text_similarity_transformers.py](./transformers/nlp/fuzzy_text_similarity_transformers.py)
       * [text_embedding_similarity_transformers.py](./transformers/nlp/text_embedding_similarity_transformers.py)
       * [text_lang_detect_transformer.py](./transformers/nlp/text_lang_detect_transformer.py)
       * [text_meta_transformers.py](./transformers/nlp/text_meta_transformers.py)
       * [text_sentiment_transformer.py](./transformers/nlp/text_sentiment_transformer.py)
       * [text_similarity_transformers.py](./transformers/nlp/text_similarity_transformers.py)
     * [numeric](./transformers/numeric)
       * [exp_diff_transformer.py](./transformers/numeric/exp_diff_transformer.py)
       * [log_transformer.py](./transformers/numeric/log_transformer.py)
       * [random_transformer.py](./transformers/numeric/random_transformer.py)
       * [round_transformer.py](./transformers/numeric/round_transformer.py)
     * [outliers](./transformers/outliers)
       * [h2o3-dl-anomaly.py](./transformers/outliers/h2o3-dl-anomaly.py)
       * [quantile_winsorizer.py](./transformers/outliers/quantile_winsorizer.py)
       * [twosigma_winsorizer.py](./transformers/outliers/twosigma_winsorizer.py)
     * [string](./transformers/string)
       * [strlen_transformer.py](./transformers/string/strlen_transformer.py)
       * [to_string_transformer.py](./transformers/string/to_string_transformer.py)
     * [targetencoding](./transformers/targetencoding)
       * [leaky_mean_target_encoder.py](./transformers/targetencoding/leaky_mean_target_encoder.py)
     * [timeseries](./transformers/timeseries)
         * [auto_arima_forecast.py](./transformers/timeseries/auto_arima_forecast.py)
         * [general_time_series_transformer.py](./transformers/timeseries/general_time_series_transformer.py)
         * [normalized_macd.py](./transformers/timeseries/normalized_macd.py)
         * [parallel_auto_arima_forecast.py](./transformers/timeseries/parallel_auto_arima_forecast.py)
         * [parallel_prophet_forecast.py](./transformers/timeseries/parallel_prophet_forecast.py)
         * [serial_prophet_forecast.py](./transformers/timeseries/serial_prophet_forecast.py)
         * [time_encoder_transformer.py](./transformers/timeseries/time_encoder_transformer.py)
         * [trading_volatility.py](./transformers/timeseries/trading_volatility.py)