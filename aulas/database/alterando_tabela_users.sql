USE dio_db;

ALTER TABLE users
ADD `street` varchar(100)  NOT NULL COMMENT 'User address street',
ADD `number` varchar(10) NOT NULL COMMENT 'User address number',
ADD `city` varchar(50) NOT NULL COMMENT 'User address city',
ADD `state` varchar(10) NOT NULL COMMENT 'User address state';

SET SQL_SAFE_UPDATES = 0;

UPDATE users
SET street = SUBSTRING_INDEX(SUBSTRING_INDEX(address, ',', 1), ',', -1),
	number = SUBSTRING_INDEX(SUBSTRING_INDEX(address, ',', 2), ',', -1),
    city = SUBSTRING_INDEX(SUBSTRING_INDEX(address, ',', 3), ',', -1),
    state = SUBSTRING_INDEX(address, ',', -1);

ALTER TABLE users
DROP COLUMN address;
