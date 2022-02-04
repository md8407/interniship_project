import instaloader

m=instaloader.Instaloader()

name=input("enetr your insta profile:")

m.download_profile(name,profile_pic_only=True)
