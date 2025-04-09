DROP SCHEMA period_data CASCADE;
CREATE SCHEMA period_data;

CREATE TABLE period_data.menstrual_phase (
    startDate VARCHAR(20) NOT NULL,
    endDate VARCHAR(20) NOT NULL,
    length INT, 
    description VARCHAR(255),
    PRIMARY KEY (startDate, endDate)
)

CREATE TABLE period_data.follicular_phase (
    startDate VARCHAR(20) NOT NULL,
    endDate VARCHAR(20) NOT NULL,
    length INT,
    PRIMARY KEY (startDate, endDate)
);
CREATE TABLE period_data.luteal_phase (
    startDate VARCHAR(20) NOT NULL,
    endDate VARCHAR(20) NOT NULL,
    length INT,
    PRIMARY KEY (startDate, endDate)
);
CREATE TABLE period_data.ovulation_phase (
    startDate VARCHAR(20) NOT NULL,
    endDate VARCHAR(20) NOT NULL,
    length INT,
    PRIMARY KEY (startDate, endDate)
);