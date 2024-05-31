CREATE TABLE ADMIN_T1(User_name Varchar(255) PRIMARY KEY,F_name VARCHAR(255),M_name VARCHAR(255),L_Name VARCHAR(255),password INTEGER ,con_Passwrd INT,address varchar (255),City VARCHAR (30),division varchar(255));
select * from ADMIN_T1; --signup admin 

CREATE OR REPLACE PROCEDURE UPDATE_ADMIN_T1(
    p_User_name VARCHAR,
    p_new_password INTEGER,
    p_new_con_Passwrd INTEGER
)
AS
BEGIN
    -- Update User_name, password, and con_Passwrd
    UPDATE ADMIN_T1
    SET 
        User_name = p_User_name,
        password = p_new_password,
        con_Passwrd = p_new_con_Passwrd
    WHERE User_name = p_User_name;

    COMMIT;
END;

 --- admin forget password 

select * from ADMIN_T1;

CREATE TABLE PASS_ACTIVATION
( Passport_no varchar (255),CNIC_no INTEGER PRIMARY KEY,  First_name VARCHAR(255),Last_name VARCHAR(255),DOB VARCHAR(255),address VARCHAR(255),Nationality VARCHAR(255),Contact_info VARCHAR (255),Disability VARCHAR (30) ,Province VARCHAR (30),City VARCHAR (30) ,Gender VARCHAR (30),Issue_date VARCHAR (255) ,Expiry_date varchar (255) );
select*from PASS_ACTIVATION ; --passport Activation

CREATE OR REPLACE PROCEDURE UPDATE_PERSON_T12(
    p_cnic_no INTEGER, 
    p_new_First_name VARCHAR2 ,
    p_new_Last_name VARCHAR2,
    p_new_dob VARCHAR2,
    p_new_address VARCHAR2,
    p_new_nationality VARCHAR2 ,
    p_new_contact_info VARCHAR2,
    p_new_Disability VARCHAR2 ,
    p_new_Province VARCHAR2 ,
     p_new_City VARCHAR2 ,
    p_new_Gender VARCHAR2
)
AS
BEGIN
    UPDATE PERSON_T12 SET First_name = p_new_First_name WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Last_name = p_new_Last_name WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET DOB = p_new_dob WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET address = p_new_address WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Nationality = p_new_nationality WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Contact_info = p_new_contact_info WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Disability = p_new_Disability WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Province = p_new_Province WHERE CNIC_no = p_cnic_no;
    UPDATE PERSON_T12 SET Province = p_new_City WHERE CNIC_no = p_cnic_no;
    
    UPDATE PERSON_T12 SET Gender = p_new_Gender WHERE CNIC_no = p_cnic_no;

    COMMIT;
END; --update customer data

select*from PERSON_T12;

CREATE OR REPLACE  VIEW customer_data AS
SELECT
    CNIC_no,
    First_name,
    Last_name,
    DOB,
    address,
    Nationality,
    Contact_info,
    Disability,
    Province,
    City,
    Gender
FROM
    PERSON_T12; --view customer data


CREATE OR REPLACE PROCEDURE DELETE_PERSON_T12_BY_CNIC1(
    p_cnic_no INTEGER,
    p_first_name VARCHAR,
    p_last_name VARCHAR
)
AS
BEGIN
    DELETE FROM PERSON_T12
    WHERE CNIC_no = p_cnic_no
      AND First_name = p_first_name
      AND Last_name = p_last_name;

    COMMIT;
END;


select*from PERSON_T12;

