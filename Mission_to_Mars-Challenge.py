#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[5]:


## Aslways you use this code
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'http://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1) 
#1. searching for elements with a specific combination of tag "div" and att "list_text"
#2. make the browser wait one second befores searching for components


# In[4]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') #look for the <div /> tag and its descendent
# Using select_one, the first matching element returned will be a <li />


# In[5]:


# Assing the title and summary text to variables we'll reference later

slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## Scrape Mars Data: Featured Image

# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0] #Specifically searches for and returns a list of tables found in the HTML
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[16]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[17]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[18]:


slide_elem.find('div', class_='content_title')


# In[19]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[20]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[21]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[22]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[23]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[24]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[25]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[26]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[27]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[28]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[6]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)



# 2. Create a list to hold the jpg images and titles.
hemisphere_image_urls = []



# 3. Write code to retrieve the image urls and titles for each hemisphere.
#//*[@id="product-section"]/div[2]/div[1]/a/img
#//*[@id="product-section"]/div[2]/div[2]/a/img
for i in range(4):
    
    #browser.find_by_css('a.itemLink img')[i].click()
    xpath = '//*[@id="product-section"]/div[2]/div['  + str(i+1) +   ']/a/img'
    browser.find_by_xpath(xpath).click()
    
    #image_url = browser.find_by_text('Sample')['href']
    image_url = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a')['href']
    #print(image_url)
    #title = browser.find_by_css('h2.title').text
    title = browser.find_by_xpath('//*[@id="results"]/div[1]/div/div[3]/h2').text
    #print(title)
    
    hemi = {}
    hemi['img_url']=image_url
    hemi['title']=title
    
    hemisphere_image_urls.append(hemi)
    browser.back()

hemisphere_image_urls
#browser.quit()


# In[36]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()

