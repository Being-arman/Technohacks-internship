SELECT * FROM iris.iris;


-- Step 1: Create a new table to store the distinct values--

CREATE TABLE new_dataset (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    SepalLengthCm FLOAT,
    SepalWidthCm FLOAT,
    PetalLengthCm FLOAT,
    PetalWidthCm FLOAT,
    Species VARCHAR(255)
);

-- The above code created a new table called new_dataset with the same structure as our original dataset--

-- Step 2: Insertd distinct values from our original dataset into the new table.


INSERT INTO new_dataset (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species)
SELECT DISTINCT SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species
FROM iris;

SELECT * FROM iris_perfect;


-- Drop the original table--

DROP TABLE iris;

-- Renamed the new table to replace the original table--

RENAME TABLE new_dataset TO iris_perfect;












