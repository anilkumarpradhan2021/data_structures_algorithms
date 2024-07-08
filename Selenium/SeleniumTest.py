'''
Created on 18-Jul-2016

@author: anpradha
'''
from selenium import webdriver
def is_element_visiable(element):
    try :
        if element.is_displayed():
            return True
        else:
            return False
    except:
        return False



# button, text , select , link , check box, drop down , radio, slider 
# find all element
# give proper name to them 
# add basic test case 

def find_all_element_by_tag():
    test = driver.find_elements_by_tag_name("input")
    for c in range(len(test)):
            print("Count : " + str(c))
            print("id " + test[c].get_attribute("id"))
            print("name : " + test[c].get_attribute("name"))
            print("title :" + test[c].get_attribute("title"))
            print("value :" + test[c].get_attribute("value"))
            print("type :" + test[c].get_attribute("type"))            
            store_valid_xpath(test[c], "input", elements)
            print("***************")
    test = driver.find_elements_by_tag_name("a")
    for c in range(len(test)):
            print("Count : " + str(c))
            print("id " + test[c].get_attribute("id"))
            print("name : " + test[c].get_attribute("name"))
            print("title :" + test[c].get_attribute("title"))
            print("type :" + test[c].get_attribute("type"))  
            print("text :" + test[c].text)
            store_valid_xpath(test[c], "a", elements)
            print("***************")

    
def store_valid_xpath(element, element_type, elements):
    if len(element.get_attribute("id")) > 0 or len(element.get_attribute("name")) > 0 or len(element.get_attribute("title")) > 0 or len(element.text) > 0 :
        if len(element.get_attribute("id")) > 0 :
            value = element.get_attribute("id")
            temp = "//" + element_type + "[@id='" + value + "']"
        elif len(element.get_attribute("name")) > 0 :
            value = element.get_attribute("name")
            temp = "//" + element_type + "[@name='" + value + "']"
    
        elif len(element.get_attribute("title")) > 0 :
            value = element.get_attribute("title")
            temp = "//" + element_type + "[@title='" + value + "']"
        
        elif len(element.text) > 0 :
            value = element.text
            temp = "//" + element_type + "[contains(.,'" + value + "')]"
        
        id = element.get_attribute("id")
        name = element.get_attribute("name")
        title = element.get_attribute("title")
        value = element.get_attribute("value")
        type = element.get_attribute("type")
        text = element.text
        if len(type) > 0 :     
            if type == "submit":
                element_name = "button_"
            if type == "text":
                element_name = "text_"
            if type == "checkbox":
                element_name = "checkbox_"
            if type == "radio":
                element_name = "radio_"
            if type == "select":
                element_name = "select_"
            if type == "hidden":
                element_name = "select_"
            if type == "a":
                element_name = "link_"
        elif element_type == "a":
                element_name = "link_"    
        else:
            element_name = "no_type_"       
        
        if id is not None and len(id) > 0:
            element_name = element_name + id    
        elif name is not None and len(name) > 0:
            element_name = element_name + name    
        elif title is not None and len(title) > 0:
            element_name = element_name + title    
        elif value is not None and len(value) > 0:
            element_name = element_name + value
        elif text is not None and len(text) > 0:
            element_name = element_name + text
        else:
            element_name = element_name + "no_value_title_text"        

        elements[element_name] = temp
    
          
if __name__ == '__main__':
    elements = {}
    driver = webdriver.Firefox()
    driver.get("http://google.com")
    find_all_element_by_tag()
    print(elements)
    driver.close()
