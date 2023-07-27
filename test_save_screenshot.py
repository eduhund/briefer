from selenium import webdriver

webpage = webdriver.Chrome()
webpage.set_window_size(1024,1024)
webpage.get('https://www.suprlance.com/')
webpage.save_screenshot('test_save_screenshot.png')