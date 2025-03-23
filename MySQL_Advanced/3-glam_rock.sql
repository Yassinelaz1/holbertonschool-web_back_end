-- SQL script that lists all bands with Glam rock as their main style,
-- ranked by their longevity
SELECT 
    band_name, 
    COALESCE(YEAR(split) - YEAR(formed), YEAR(NOW()) - YEAR(formed)) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;