-- VIEW 1: Primary Feature Table (Flattens 3NF into ML Input)
CREATE VIEW view_no2_classification_features AS
SELECT 
    m.measurement_id,
    m.start_time AS measurement_timestamp,
    EXTRACT(MONTH FROM m.start_time) AS feature_month,
    EXTRACT(HOUR FROM m.start_time) AS feature_hour,  
    m.value AS no2_value,
    
    -- Label for the exercise baseline model.
    CASE 
        WHEN m.value >= 40 THEN 1
        ELSE 0 
    END AS elevated_no2_label,
    
    sp.station_code,
    sp.sampling_point_code,
    sp.country_code
FROM 
    measurements m
JOIN 
    sampling_points sp ON m.sampling_point_id = sp.sampling_point_id
JOIN 
    pollutants p ON m.pollutant_id = p.pollutant_id
WHERE 
    p.pollutant_name = 'NO2';


-- VIEW 2: Class-Balanced Samples (Addressing Imbalance)
CREATE VIEW view_balanced_pollution_samples AS
(
    SELECT * FROM view_no2_classification_features
    WHERE elevated_no2_label = 0
    ORDER BY measurement_timestamp DESC
    LIMIT 5000
)
UNION ALL
(
    SELECT * FROM view_no2_classification_features
    WHERE elevated_no2_label = 1
    ORDER BY measurement_timestamp DESC 
);


-- VIEW 3: Regional Daily Aggregates (Engineered Trend Features)
CREATE VIEW view_regional_daily_aggregates AS
SELECT 
    DATE_FORMAT(m.start_time, '%Y-%m-%d') AS measurement_date, 
    sp.station_code,
    sp.sampling_point_code AS station_identifier,
    AVG(m.value) AS daily_avg_no2,
    MAX(m.value) AS daily_max_no2,
    MIN(m.value) AS daily_min_no2
FROM
    measurements m
JOIN
    sampling_points sp ON m.sampling_point_id = sp.sampling_point_id
JOIN
    pollutants p ON m.pollutant_id = p.pollutant_id
WHERE
    p.pollutant_name = 'NO2'
GROUP BY 
    DATE_FORMAT(m.start_time, '%Y-%m-%d'), 
    sp.station_code,
    sp.sampling_point_code;
