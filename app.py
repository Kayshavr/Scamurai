
from dotenv import load_dotenv
from streamlit_chat import message
from PIL import Image
import os, re, openai as OpenAI, streamlit as st, numpy as np

load_dotenv()

def chatgpt_connection(prompt):

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content.strip()

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

def chat_with_gpt(web_img, web_link):
    st.header("Chatbot: ")
    prompt = st.chat_input("Please Enter Text input")
    if prompt:
        response = chatgpt_connection(prompt)
        st.write(f"User has sent the following prompt: {prompt}")
        st.write(f"Response:: {response}")

def submit():
    if not check_link(st.session_state.web_link):
        st.session_state.web_link = st.session_state.link
        st.session_state.link = ""

def show_result(flag1, flag2):
    # Copy info from widgets into a different key in session state to avoid 
    # deletion when the widgets disappear
    if flag1 and flag2:
        st.session_state.result = (st.session_state.image, st.session_state.link)
        st.session_state.input = False

def reset():
    st.session_state.input = True

def main():
    st.title("Scamurai System")
    col1, col2 = st.columns(2)

    holder = st.empty()
    flag1 = False
    flag2 = False

    if 'input' not in st.session_state:
        st.session_state.input = True

    if st.session_state.input:
        # Show input widgets if in input mode
        with st.container():
            with col1:
                st.header("Website Image")
                holder1 = st.empty()
                top_image = holder1.file_uploader('Please Input Website Image', key="image", type='jpg')
                if top_image is not None:
                    # st.write(top_image)
                    # st.write({'filename': top_image.name, 'file_type': top_image.type, 'filesize': top_image.size})
                    st.image(top_image, width=100)
                    holder1.empty()
                    flag1 = True
            with col2:
                st.header("Website Link")
                holder2 = st.empty()
                if "web_link" not in st.session_state:
                    st.session_state.web_link = ""

                holder2.text_input("Enter Website Link", key="link", on_change=submit)

                web_link = st.session_state.web_link
                
                if check_link(web_link):
                    st.text(web_link)
                    holder2.empty()
                    st.write("Website: ", web_link)
                    flag2 = True
                elif web_link != "":
                    st.text("Please input a valid web link")

        st.button('Start', on_click=show_result(flag1,flag2)) # Callback changes it to result mode
        
    else:
    # Otherwise, not in input mode, so show result   
        st.button('Reset', on_click=reset) # Callback changes it to input mode
        chat_with_gpt(st.session_state.result[0],st.session_state.result[1])

if __name__ == "__main__":
    while True:
        user_input = input ("You: ")
        if user_input. lower() in ["quit", "exit", "bye"]:
            break

        response = chatgpt_connection(user_input)
        print ("Chatbot: ", response)