from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import Sudoku

start0 = time.time() 

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)

driver.get("http://www.websudoku.com/?level=4")

editor_frame = driver.find_element_by_css_selector('html > frameset > frame')
driver.switch_to.frame(editor_frame)

print("Page loaded in {:.3f}second".format(time.time() - start0))

start1 = time.time() 

input = list(range(81))

for y in range(9):
    for x in range(9):
        temp = driver.find_element_by_css_selector('#f'+str(x)+str(y)).get_attribute('class')
        if temp == 's0':
            tempval = driver.find_element_by_css_selector('#f'+str(x)+str(y)).get_attribute('value')
            input[9*y+x]=int(tempval)
        else:
            input[9*y+x] = 0

print("Question read in {:.3f}second".format(time.time() - start1))

start2 = time.time()

aws =  Sudoku.solve(input)

print("Solved in :{:.3f}second".format(time.time() - start2))

start3 = time.time() 

for y in range(9):
    for x in range(9):
        temp = driver.find_element_by_css_selector('#f'+str(x)+str(y)).get_attribute('class')
        if temp == 'hidden':
            pass
        else:
            driver.find_element_by_css_selector('#f'+str(x)+str(y)).send_keys(str(aws[9*y+x]))
            
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[3]/table/tbody/tr[2]/td/form/p[4]/input[1]').click()

print("Answer checked in {:.3f}second".format(time.time() - start3))

print("Total time : {:.3f}second".format(time.time() - start0))

time.sleep(10)

driver.quit()