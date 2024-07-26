-- Use the provided database
USE alx_book_store;

-- Query the information_schema to get the table structure
SELECT 
    COLUMN_NAME AS 'Column Name',
    DATA_TYPE AS 'Data Type',
    CHARACTER_MAXIMUM_LENGTH AS 'Max Length',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value'
FROM 
    information_schema.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'books';
