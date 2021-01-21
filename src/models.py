from config import Config


import requests

class InstaGet():

    def __init__(self, username):
        self.username     = username
        self.full_profile = self.__init__profile__(username=username)
    
    @staticmethod
    def __init__profile__(username):
        """
        return instagram profile from unofficial api
        ---
        parameters:
            - name: username
              type: str
              description: instagram username
              example: justinbieber
        response:
            - type: JSON
        """
        s = requests.Session()
        s.cookies.set("sessionid", Config.SESSION_ID, domain="instagram.com")

        insta_url = Config.API_PROFILE(username)
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-GPC': '1'
        }
        
        response = s.request("GET", insta_url, headers=headers)
        return response.json()

    def get_profile(self):
        # init profile root variables
        graphql = self.full_profile.get('graphql', {})
        user    = graphql.get('user', {})

        # init profile data
        username  = self.username
        full_name = user.get('full_name', '')
        biography = user.get('biography', '')
        external_url = user.get('external_url', '')
        followers = user.get('edge_followed_by', {}).get('count', 0)
        following = user.get('edge_follow', {}).get('count', 0)
        is_business_account = user.get('is_business_account', False)
        is_joined_recently = user.get('is_joined_recently', True)
        business_category_name = user.get('business_category_name')
        is_private = user.get('is_private', False)
        is_verified = user.get('is_verified', False)
        profile_pic_url_hd = user.get('profile_pic_url_hd')
        posts = user.get('edge_owner_to_timeline_media', {}).get('count', 0)

        payload = {
            'username':username,
            'full_name':full_name,
            'biography':biography,
            'external_url':external_url,
            'followers':followers,
            'following':following,
            'is_business_account':is_business_account,
            'is_joined_recently':is_joined_recently,
            'business_category_name':business_category_name,
            'is_private':is_private,
            'is_verified':is_verified,
            'profile_pic_url_hd':profile_pic_url_hd,
            'posts':posts
        }
        return payload
    
    def get_last_pictures(self):
        """
        return 12 last pictures
        ---
        """
        pass
    