import pymysql
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver=webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    try:
        con=pymysql.connect(
            host="localhost",
            user="root",
            password="Parkhi@1326",
            database="login"
        )
        curs=con.cursor()
        print(f"connected to database: {con}")
        curs.execute("select * from login1")

        log_in = driver.find_element(By.ID, "login2").click()
        for row in curs:
            pname=row[0]
            ppassword=row[1]

            driver.find_element(By.ID,"loginusername").clear()
            driver.find_element(By.ID,"loginusername").send_keys(pname)
            driver.find_element(By.ID,"loginpassword").clear()
            driver.find_element(By.ID,"loginpassword").send_keys(ppassword)

            login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
            time.sleep(2)
            try:
                alert=driver.switch_to.alert
                alert.accept()
                time.sleep(2)
            except:
                print("No alert available")

            logout=driver.find_element(By.ID,"logout2").click()
            time.sleep(2)
            try:
                alert=driver.switch_to.alert
                alert.accept()
                time.sleep(2)
            except:
                print("No alert avilable....")

            log_in = driver.find_element(By.ID, "login2").click()
            time.sleep(2)

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error while interacting with the database: {e}")
    finally:
        if con:
            con.close()
            print("database connection closed")
except Exception as e:
    print(f"webdriver error: {e}")
finally:
    driver.quit()
    print("Browser closed")