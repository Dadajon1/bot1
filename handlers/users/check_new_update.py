import random

import instaloader
from aiogram import types
from bs4 import BeautifulSoup
from instaloader import Post
from selenium import webdriver


L = instaloader.Instaloader()
L.load_session_from_file('haminmoshotmi',
                         '/home/ubuntu/Projects/Instagram-like-comment-checker/session-haminmoshotmi')

driver = webdriver.Chrome()
link = "https://www.instagram.com/p/CQv6euDN8iL/"
user = "yoshlik_media"
driver.get(link)

soup = BeautifulSoup(driver.page_source, 'html.parser')

img = soup.find('img', class_='FFVAD')
img_url = img['src']
# print(img_url)
print(link[28:39])
post = Post.from_shortcode(L.context, link[28:39])
comment_list = []
print(post)
post_com = post.get_likes()
print(post_com)
for comment in post_com:
    print(comment)
    comment_list.append(comment.username)

# print(profile.get_posts()
print(comment_list)