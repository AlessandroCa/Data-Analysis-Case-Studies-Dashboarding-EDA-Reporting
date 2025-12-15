# Project03_Telecom_Call_Data_Analysis_and_Billing

This repository presents an end-to-end analysis of mobile phone call records, aimed at transforming raw operational data into meaningful metrics for billing and network monitoring.

The dataset consists of call logs stored in CSV format and includes deliberately imperfect records, reflecting common real-world data quality issues. Invalid entries are identified and removed through a set of business and temporal validation rules, such as incorrect timestamps, self-calls, and calls exceeding realistic duration limits.

After the cleaning phase, call durations are computed by converting date and time information into a unified minute-based representation. The processed data is then aggregated to calculate monthly customer charges, applying pricing rules that include per-minute costs and free usage thresholds.

Finally, call volumes are analyzed at the cellular area level to identify congested cells. A cell is considered congested when its number of outgoing calls exceeds the average, illustrating how aggregated indicators can be used to support infrastructure and operational decisions.

The focus of this work is on data validation, time-based transformations, aggregation logic, and the clear translation of raw data into actionable insights using Python.
