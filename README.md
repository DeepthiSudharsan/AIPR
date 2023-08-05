# AIPR - Aiding In Printing References

> **Note**
This project was made for fun and since then has not been actively maintained. Hence, the repo is open for contributors who would like to improve and add functionalities or make any fixes. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> :information_source: **Additional Information**: <br>
To know more about the story of this project, kindly check the respective footnote. [^1].

> 💡**Idea**:
When printing a page or document, there might be certain hyperlinks or references that might also have to be looked at for a better grasp of the contents of the document/page. AIPR will help convert those hyperlink contents into PDF and merge it with the PDF you are planning to print and give you the final merged copy so you don't have to rely on manually searching up those links and can just enjoy with your hard copy. 

> **Important**
The current version has been deployed on Streamlit :
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://printaid.streamlit.app/)

### AIPR Workflow

![image](https://github.com/DeepthiSudharsan/AIPR/assets/59824729/48a87849-1ea0-489c-9f34-f14be0bae9b7)

### File Structure
    .
    ├── app.py                   # Streamlit Application Script
    ├── requirements.txt         # Requirements file (libraries with their versions)
    ├── packages.txt             # Packages.txt file (package requirements to run the application)
    ├── setup.sh                 # Bash script
    ├── Procfile                 # Commands to be executed by Streamlit on startup
    └── README.md                # Supporting Documentation

## Prerequisites

Before running the Streamlit app, you need to have the following installed:
```
- Python 3.9 or later
- pip (Python package manager)
```

## Installation

To set up the app and run it locally, follow these steps:

1. Clone the repository:
```
   ```bash
   git clone https://github.com/your-username/your-repository.gi](https://github.com/DeepthiSudharsan/AIPR.git
   cd AIPR
```
2. Install the requirements dependencies:
```
   pip install -r requirements.txt
```
3. Download the wkhtmltopdf binary:
```
- Download the appropriate wkhtmltopdf binary for your platform.
- Save the binary to the root folder of the repository.
```
4. Once the installation is complete, run the Streamlit app using the following command:
```
streamlit run app.py
```
The app will start running, and you should see a message indicating that the app is available at a specific URL (usually http://localhost:8501).

### TO-DO TASK LIST 
- [ ] Add functionality for input file documents (just like the URL functionality right now)
- [ ] Bug Fix: Add some type of support for the reference links that could not be converted to PDFs (at least just providing the links to these URLs at the end)
- [ ] Improve the overall UI for the application
- [ ]  Transition from Streamlit Deployment to creating a Chrome/Browser extension for the same.
- [x] Feel free to add more tasks and contribute to this project!  
Note: Some of the above tasks (at least 1 - 3) are relatively beginner friendly and easy to do provided you have a good understanding of the code so far.

### CONTRIBUTORS

[//]: contributor-faces
<a href="https://github.com/DeepthiSudharsan"><img src="https://avatars.githubusercontent.com/u/59824729?v=4" title="DeepthiSudharsan" width="80" height="80"></a>

[^1]: This fun little project started off as a joke about my laziness. I had printed one document for studying so I can read it whenever I want and wherever I want but eventually realized that the document consisted of way too many hyperlinks to different references which I need to visit and learn to get a good grasp of the discussion in the document. But this meant that I had to use some device yet again. And this was my 30-minute solution to such a silly thing!
