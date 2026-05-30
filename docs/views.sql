CREATE VIEW view_no2_classification_features AS
SELECT 
    m.measurement_id,
    m.start_time AS start_time,
    EXTRACT(MONTH FROM m.start_time) AS month,
    EXTRACT(HOUR FROM m.start_time) AS hour,  
    WEEKDAY(m.start_time) AS weekday,
    m.value AS value,
    
    -- Label for the exercise baseline model.
    CASE 
        WHEN m.value >= 40 THEN 1
        ELSE 0 
    END AS target_elevated_no2,
    
    CASE
        WHEN m.data_capture IS NULL THEN 1
        ELSE 0
    END AS data_capture_missing,
    
    val.validity_code AS validity,
    ver.verification_code AS verification,
    sp.sampling_point_code AS samplingpoint
FROM 
    measurements m
JOIN 
    sampling_points sp ON m.sampling_point_id = sp.sampling_point_id
JOIN 
    pollutants p ON m.pollutant_id = p.pollutant_id
JOIN
    validity_flags val ON m.validity_id = val.validity_id
JOIN
    verification_flags ver ON m.verification_id = ver.verification_id
WHERE 
    p.pollutant_name = 'NO2';
