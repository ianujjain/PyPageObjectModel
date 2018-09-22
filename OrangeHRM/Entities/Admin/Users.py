from selenium.webdriver.common.by import By


class Users(object):
    UserName        =   (By.CSS_SELECTOR,   "#searchSystemUser_userName")
    UserRole        =   (By.CSS_SELECTOR,   "#searchSystemUser_userType")
    EmployeeName    =   (By.CSS_SELECTOR,   "#searchSystemUser_employeeName_empName");
    Status          =   (By.CSS_SELECTOR,   "#searchSystemUser_status");
    Search          =   (By.CSS_SELECTOR,   "#searchBtn");
    Reset           =   (By.CSS_SELECTOR,   "#resetBtn");
    Add             =   (By.CSS_SELECTOR,   "#btnAdd")
    Delete          =   (By.CSS_SELECTOR,   "#btnDelete")
    SelectAll       =   (By.CSS_SELECTOR,   "#ohrmList_chkSelectAll")
    SelectRecord    =   (By.CSS_SELECTOR,   "#resultTable tr:nth-child(POS) > td:nth-child(1)")