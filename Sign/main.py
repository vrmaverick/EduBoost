# import streamlit as st
# from streamlit_option_menu import option_menu

import streamlit as st

from streamlit_option_menu import option_menu
# import os
# from dotenv import load_dotenv
# load_dotenv()

import home, account, about, your_posts
st.set_page_config(
        page_title="EduBoost",
)


# st.markdown(
#     """
#         <!-- Global site tag (gtag.js) - Google Analytics -->
#         <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
#         <script>
#             window.dataLayer = window.dataLayer || [];
#             function gtag(){dataLayer.push(arguments);}
#             gtag('js', new Date());
#             gtag('config', os.getenv('analytics_tag'));
#         </script>
#     """, unsafe_allow_html=True)
# print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='EduBoost ',
                options=['Home','Account','Your Posts','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        # if app == "Trending":
        #     trending.app()        
        if app == 'Your Posts':
            your_posts.app()
        if app == 'about':
            about.app()    
     
             
          
             
    run()            
         