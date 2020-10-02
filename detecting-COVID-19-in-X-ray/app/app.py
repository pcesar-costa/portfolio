import os
import time
import webbrowser
import streamlit as st
from PIL import Image

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from model.predict import predict

st.beta_set_page_config(page_title='Detecting COVID-19 in X-ray')
st.set_option('deprecation.showfileUploaderEncoding', False)
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def markdown_primary(text, kind):
    return st.markdown(f"<{kind} style='text-align: center; color: #C14953;'>{text}</{kind}>", unsafe_allow_html=True)

def markdown_secondary(text, kind):
    return st.markdown(f"<{kind} style='text-align: center; color: #374648;'>{text}</{kind}>", unsafe_allow_html=True)

def h1_by_color(text, color):
    return st.markdown(f"<h1 style='text-align: center; color:{color};'>{text}</h1>", unsafe_allow_html=True)

def disclaimer():
    st.error('Disclaimer: The methods and techniques used by the model, and the analysis provided is only for educational purposes. It is not meant to be a COVID-19 diagnosis system.')

def normal_center(text, color):
    return st.markdown(f"<p style='text-align: center; color:{color};'>{text}</p>", unsafe_allow_html=True)


def main():
    sidebar = st.sidebar
    sidebar.title('Navigation')
    options = ['Home', 'Model diagnostic']
    radio = st.sidebar.radio(label="", options=options)

    if radio == options[1]:
        markdown_primary('DETECTING COVID-19 IN X-RAY', 'h1')
        disclaimer()

        markdown_secondary('Upload a chest X-ray image', 'h2')
        uploaded_file = st.file_uploader('', type=['jpeg', 'png', 'jpg'])   

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, width=350, caption='Uploaded image.')

            markdown_secondary('Analyzing...', 'h2')
            progress_bar = st.progress(0)
            t = 5
            for perc in range(100):
                time.sleep(t/100)
                progress_bar.progress(perc + 1)

            label_pred = predict(image)
            if label_pred == 0:
                h1_by_color('NEGATIVE', 'green')
                text = 'A negative result means the algorithm did not find coronavirus.'
                normal_center(text, 'green')
            elif label_pred == 1:
                h1_by_color('POSITIVE', 'red')
                text = 'A positive result means that the patient had coronavirus when the X-ray was taken.'
                normal_center(text, 'red')

    else:
        disclaimer()
        markdown_primary('CONTEXT', 'h1')
        st.write('__Quasix__ is a company that had your contracts canceled after the pandemic and decided to turn your attention to fighting the new coronavirus. The company already worked in the medical field with Artificial Intelligence, assisting in the prognosis of lung diseases and various types of pneumonia.')
        st.write('Because of the change in the landscape, the company wants to create a model to detect coronavirus infections, identifying signs of the disease from chest X-rays that will provide savings in the use of test kits and made use of typical resources in hospitals: the machines X-ray.')
        st.write('For the detection of infected patients, the company relies on your team of data scientists to provide a reliable model for early detection in COVID-19 diagnostics.')

        markdown_primary('ABOUT', 'h2')
        st.write('This website uses the model of context above that provides a primary "diagnostics" for COVID-19 through chest X-ray images.')
        st.info('The context presented and the company are fictitious and exist only for the elaboration of a problem.')
        st.write('More about the developer and the project steps you can find on:')

        git_url = 'https://github.com/pcesar-costa/portfolio'
        linkedin_url = 'https://www.linkedin.com/in/pcesarcosta'

        if st.button('LinkedIn'):
            webbrowser.open_new_tab(linkedin_url)

        if st.button('Github     '):
            webbrowser.open_new_tab(git_url)

        disclaimer()

if __name__ == "__main__":
    main()