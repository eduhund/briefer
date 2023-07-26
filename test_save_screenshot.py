from selenium import webdriver

webpage = webdriver.Safari()
webpage.set_window_size(1440,1440)
webpage.get('https://www.sobakapav.ru')
webpage.save_screenshot('sobakapav.png')