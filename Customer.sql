CREATE TABLE PERSON_T10(User_name Varchar(255) PRIMARY KEY,F_name VARCHAR(255),M_name VARCHAR(255),L_Name VARCHAR(255),password INTEGER ,con_Passwrd INT,address varchar (255),City VARCHAR (30),division varchar(255));
select * from PERSON_T10; --customer create an account/signup

CREATE OR REPLACE PROCEDURE UPDATE_PERSON_T10(
    p_User_name VARCHAR, 
    p_new_password INTEGER,
    p_new_con_Passwrd INTEGER
)
AS
BEGIN
    -- Update User_name
    UPDATE PERSON_T10
    SET User_name = p_User_name
    WHERE User_name = p_User_name;
   
    -- Update password
    UPDATE PERSON_T10
    SET password = p_new_password
    WHERE User_name = p_User_name;

    -- Update con_Passwrd
    UPDATE PERSON_T10
    SET con_Passwrd = p_new_con_Passwrd
    WHERE User_name = p_User_name;

    COMMIT;
END;
  --froget password 

select * from PERSON_T10;


CREATE TABLE PERSON_T12
(CNIC_no INTEGER PRIMARY KEY,First_name VARCHAR(255),Last_name VARCHAR(255),DOB VARCHAR(255),address VARCHAR(255),Nationality VARCHAR(255),Contact_info VARCHAR (255),Disability VARCHAR (30) ,Province VARCHAR (30),City VARCHAR (30) ,Gender VARCHAR (30) );
select*from PERSON_T12;--customer application submission

CREATE TABLE TRANS_FEE_PASS(Atm_pin INTEGER  PRIMARY KEY, Atm_card varchar (255) ,CNIC_no INTEGER, CONSTRAINT fk_cnic2 FOREIGN KEY (CNIC_no) REFERENCES PERSON_T12(CNIC_no));
  select* from  TRANS_FEE_PASS; --passport fee 
  
  CREATE TABLE FEED_BACK ( First_name VARCHAR(255)  ,Last_name VARCHAR(255),description varchar (255),CNIC_no INTEGER, CONSTRAINT fk_cnic3 FOREIGN KEY (CNIC_no) REFERENCES PERSON_T12(CNIC_no) );
  select * from FEED_BACK; --customer feedback
  
  
  
  
  CREATE TABLE INSERT_DATA (
    CNIC_no INTEGER PRIMARY KEY,
    First_name VARCHAR(255),
    Last_name VARCHAR(255),
    DOB VARCHAR(255),
    address VARCHAR(255),
    Nationality VARCHAR(255),
    Contact_info VARCHAR(255),
    Disability VARCHAR(30),
    Province VARCHAR(30),
    City VARCHAR(30),
    Gender VARCHAR(30)
); --table for trigger value store

  
  CREATE OR REPLACE TRIGGER INERST_INTO_PERSON_T12
AFTER INSERT ON PERSON_T12
FOR EACH ROW
BEGIN
    INSERT INTO INSERT_DATA (
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
    )
    VALUES (
        :new.CNIC_no,
        :new.First_name,
        :new.Last_name,
        :new.DOB,
        :new.address,
        :new.Nationality,
        :new.Contact_info,
        :new.Disability,
        :new.Province,
        :new.City,
        :new.Gender
    );
END;

select * from  INSERT_DATA;


  