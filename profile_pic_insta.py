# il faut installer instaloader : pip install instaloader
import instaloader
 
ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")
 
ig.download_profile(dp , profile_pic_only=True)