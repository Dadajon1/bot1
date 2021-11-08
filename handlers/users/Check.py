import instaloader
from bs4 import BeautifulSoup
from selenium import webdriver

L = instaloader.Instaloader()
L.login("haminmoshotmi", "parolnibermayman")
driver = webdriver.Chrome()


def comment_like_list(link, user):
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img = soup.find('img', class_='FFVAD')
    try:
        img_url = img['src']
        print(img_url)
    except Exception as ex:
        print(ex)


    profile = instaloader.Profile.from_username(L.context, user)
    print(profile.get_posts())

    for post in profile.get_posts():
        like_list = []
        comment_list = []
        print(post.url)
        if post.url[:160] == img_url[:160]:
            post_likes = post.get_likes()
            post_comments = post.get_comments()

            for likee in post_likes:
                # print(likee.username)
                like_list.append(likee.username)

            for comment in post_comments:
                # print(comment.owner.username)
                comment_list.append(comment.owner.username)
            print("=" * 50)
            break

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
    L.save_session_to_file()