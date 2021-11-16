import instaloader
from bs4 import BeautifulSoup
from selenium import webdriver
from instaloader import Post

L = instaloader.Instaloader()
# L.login("yoshlik_media", "112142249Aviator!")
# driver = webdriver.Chrome()
L.load_session_from_file('haminmoshotmi',
                                 '/home/ubuntu/.config/instaloader/session-haminmoshotmi')


def comment_like_list(link, user):



    post = Post.from_shortcode(L.context, link[28:39])
    comment_list = []
    post_com = post.get_comments()
    for comment in post_com:
        comment_list.append(comment.owner.username)

    like_list = []
    post_com = post.get_likes()
    for like in post_com:
        like_list.append(like.username)
    return like_list, comment_list

if __name__=="__main__":
    username = "yoshlik_media"
    like, comment = comment_like_list("https://www.instagram.com/p/CQv6euDN8iL/", "yoshlik_media")

    if username in like:
        print("Like bosmagan")
    else:
        print("Yemadi...")
    if username in comment:
        print("Comment yozmagan")
    else:
        print("Yemadi")
    comment_like_list("https://www.instagram.com/p/CQv6euDN8iL/", "yoshlik_media")