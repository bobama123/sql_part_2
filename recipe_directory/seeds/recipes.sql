DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    average_cooking_time INTERVAL MINUTE,
    rating INT CHECK (rating > 0 AND rating < 6)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Burger', INTERVAL '30 minutes', 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Pasta', INTERVAL '25 minutes', 1);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Chips', INTERVAL '60 minutes', 3);
