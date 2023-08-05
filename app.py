import streamlit as st
from streamlit_tags import st_tags
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pypdf import PdfMerger
import pdfkit
import tempfile
from streamlit_card import card

st.title("AIPR - AIDING IN PRINTING REFERENCES")
st.info("ℹ Note: This web app was created for fun and not actively maintained. Please feel free to contribute to the Github repository as a collaborator/maintainer!")
st.divider()
with st.sidebar:
    st.info("To Contribute to the Repo, Click the below Info Card")
    hasClicked = card(
            title=" ",
            text=" ",
            image="https://avatars.githubusercontent.com/u/59824729?v=4",
            url="https://github.com/DeepthiSudharsan/AIPR"
        )
    keywords = st_tags(
    label='Libraries/Packages Used',
    text='',
    value=['Streamlit', 'Pdfkit', 'PdfMerger','BeautifulSoup',"urllib","streamlit-card","streamlit-tags"],
    maxtags = 7)

st.header("Provide the URL for the page you would like to print")
site = st.text_input("URL :","")
if site == "":
    st.warning(" Please provide the url")
else:
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = Request(site, headers=hdr)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")

    links = []
    for link in soup.findAll('a'):
        url1 = link.get('href')
        if "https://" in url1:
            links.append(link.get('href'))
    links.insert(0, site)
    merger = PdfMerger()
    for url in links:
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf:
                st.toast(f"Processing url {url}")
                pdfkit.from_url(url, temp_pdf.name)
                st.toast("TEST.......")
                merger.append(temp_pdf)
                st.toast("Converted to PDF...")
        except Exception as e:
            st.toast(f"Cannot generate PDF for {url}")
    
    merged_pdf_path = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False).name
    merger.write(merged_pdf_path)
    merger.close()

    # Provide a download link for the user
    st.success("🎉 Your PDF has been created and ready for download!")
    st.write("Click the button below to download the merged PDF:")
    st.download_button("⬇️ Download PDF", data=open(merged_pdf_path, 'rb').read(), file_name='result.pdf')
