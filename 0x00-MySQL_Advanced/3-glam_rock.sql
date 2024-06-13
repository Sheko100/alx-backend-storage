-- lists all bands with "Glam rock" as their main style, ranked by their longevity
-- Selects band_name, the diffrence between split and formed as band and lifespan columns
SELECT band_name, (COALESCE(split, 2022)-formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
