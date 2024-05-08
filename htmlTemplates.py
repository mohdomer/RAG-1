# # css = '''
# # <style>
# # .chat-message {
# #     padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
# # }
# # .chat-message.user {
# #     background-color: #2b313e
# # }
# # .chat-message.bot {
# #     background-color: #475063
# # }
# # .chat-message .avatar {
# #   width: 20%;
# # }
# # .chat-message .avatar img {
# #   max-width: 78px;
# #   max-height: 78px;
# #   border-radius: 50%;
# #   object-fit: cover;
# # }
# # .chat-message .message {
# #   width: 80%;
# #   padding: 0 1.5rem;
# #   color: #fff;
# # }
# # '''

# # bot_template = '''
# # <div class="chat-message bot">
# #     <div class="avatar">
# #         <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
# #     </div>
# #     <div class="message">{{MSG}}</div>
# # </div>
# # '''

# # user_template = '''
# # <div class="chat-message user">
# #     <div class="avatar">
# #         <img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500">
# #     </div>    
# #     <div class="message">{{MSG}}</div>
# # </div>
# # '''


# # css = '''
# # <style>
# # body {
# #     background-color: #556B2F;
# # }

# # .container {
# #     background-color: #4B5320;
# #     padding: 20px;
# #     border-radius: 10px;
# # }

# # .chat-message {
# #     padding: 1rem; 
# #     margin-bottom: 1rem; 
# #     display: flex;
# #     align-items: center;
# # }

# # .chat-message.user {
# #     background-color: #FFA07A;
# # }

# # .chat-message.bot {
# #     background-color: #ADD8E6;
# # }

# # .chat-message .avatar {
# #     width: 50px;
# #     height: 50px;
# #     margin-right: 10px;
# # }

# # .chat-message .avatar img {
# #     width: 100%;
# #     height: 100%;
# #     border-radius: 50%;
# #     object-fit: cover;
# # }

# # .chat-message .message {
# #     flex: 1;
# #     color: black;
# # }

# # .text-input {
# #     position: fixed;
# #     bottom: 20px;
# #     width: 80%;
# #     margin-left: 10%;
# # }

# # </style>
# # '''

# # bot_template = '''
# # <div class="chat-message bot">
# #     <div class="avatar">
# #         <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
# #     </div>
# #     <div class="message">{{MSG}}</div>
# # </div>
# # '''

# # user_template = '''
# # <div class="chat-message user">
# #     <div class="avatar">
# #         <img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500">
# #     </div>    
# #     <div class="message">{{MSG}}</div>
# # </div>
# # '''

# css = '''
# <style>
# body {
#     background-color: #556B2F;
# }

# .container {
#     background-color: #4B5320;
#     padding: 20px;
#     border-radius: 10px;
# }

# .chat-message {
#     padding: 1rem; 
#     margin-bottom: 1rem; 
#     display: flex;
# }

# .chat-message.user .message {
#     background-color: #FFA07A;
#     border-radius: 10px;
#     padding: 10px;
#     color: black;
# }

# .chat-message.bot .message {
#     background-color: #ADD8E6;
#     border-radius: 10px;
#     padding: 10px;
#     color: black;
# }

# .chat-message .message {
#     flex: 1;
#     margin-left: 10px;
# }

# .text-input {
#     position: fixed;
#     bottom: 20px;
#     width: 80%;
#     margin-left: 10%;
# }

# </style>
# '''

# # Define your HTML templates
# bot_template = '''
# <div class="chat-message bot">
#     <div class="message">{{MSG}}</div>
# </div>
# '''

# user_template = '''
# <div class="chat-message user">
#     <div class="message">{{MSG}}</div>
# </div>
# '''

css = '''
<style>
body {
    background-color: #556B2F;
}

.container {
    background-color: #263318;
    padding: 20px;
    border-radius: 10px;
}

.chat-message {
    padding: 1rem; 
   

.chat-message.user .message {
    
    border-radius: 10px;
    padding: 10px;
    color: black;
}

.chat-message.bot .message {
    
    border-radius: 10px;
    padding: 10px;
    color: black;
}

.chat-message .message {
    flex: 1;
    margin-left: 10px;
}

.text-input {
    position: fixed;
    bottom: 20px;
    width: 80%;
    margin-left: 10%;
}

</style>
'''

# Define your HTML templates
bot_template = '''
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
</div>
'''

