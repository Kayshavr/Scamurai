
from dotenv import load_dotenv
from streamlit_chat import message
from PIL import Image
import os, re, openai, streamlit as st, numpy as np

load_dotenv()

def check_link(web_link):
    # Check if website link is valid
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, web_link) is not None 


st.title("Scamurai System")
st.subheader("Enter input below:")

openai.api_key = os.getenv('OPENAI_API_KEY')

# img_file_buffer = st.file_uploader('Upload a PNG image', type='png')
# if img_file_buffer is not None:
#     image = Image.open(img_file_buffer)
#     img_array = np.array(image)
col1, col2 = st.columns(2)

with st.container():
    with col1:
        st.header("Website Image")
        holder = st.empty()
        top_image = holder.file_uploader('Choose Bottom Glass Image', type='jpg', key=1)
        if top_image is not None:
            # st.write(top_image)
            # st.write({'filename': top_image.name, 'file_type': top_image.type, 'filesize': top_image.size})
            # st.image(top_image, width=200)
            holder.empty()
    with col2:
        st.header("Website Link")
        holder2 = st.empty()
        web_link = holder2.text_input("Enter Website Link", " ")
        
        if check_link(web_link):
            st.text(web_link)
            holder2.empty()
            st.write("Website: ", web_link)
        else:
            web_link = holder2.text_input("Please enter a valid web address",  " ")

# def chat_with_gpt(prompt):

#     client = OpenAI(
#         api_key=os.environ.get("OPENAI_API_KEY"),
#     )

#     response = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Say this is a test",
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )

#     return response.choices[0].message.content.strip()

# if __name__ == "__main__":
    # while True:
    #     user_input = input ("You: ")
    #     if user_input. lower() in ["quit", "exit", "bye"]:
    #         break

    #     response = chat_with_gpt(user_input)
    #     print ("Chatbot: ", response)