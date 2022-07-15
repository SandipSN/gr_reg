import streamlit as st
import pandas as pd
from PIL import Image

st.title("Form")
st.subheader("Enter details of case")

with st.form("form1", clear_on_submit=True):
    
    st.write("Case Details")

    case_id = st.text_input("Enter caseID (Use same ID for linked cases, otherwise leave blank)")

    offence_type = st.selectbox(
                    "Enter Offence Type",
                    ("Grooming", "Pedo", "Other")
                    )

    offender_forname = st.text_input("Enter Offender's First Name")
    offender_surname = st.text_input("Enter Offender's Last Name")
    entity_type = st.selectbox(
                    "Enter Entity Type",
                    ("Individual", "Business")
                    )
    # may need to use dropdown for this as well, standardise
    location = st.text_input("Enter Location")


    st.write("""Proof
    \n Proof must be ... (list requirements)
    
    """)
    proof = st.file_uploader("Upload Proof", type=['png', 'jpg', 'pdf'])
    # https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
    # OR
    
    proof_link =  st.text_input("Paste URL")

    submit = st.form_submit_button()

    if submit == True:
        st.success("Submitted for review")

# GET DATE
date = '0'
id_ = '0'
status = "to be set"
level = "to be set"

data = {
        'ID': id_, 
        'Case ID': case_id, 
        'Offence Type': offence_type, 
        'Entitiy Type': entity_type,
        'Offender Forname': offender_forname, 
        'Ofender Surname': offender_surname, 
        'Location': location, 
        'Proof Link': proof_link, 
        'Date': date, 
        'Status': status, 
        'Level': level
    }

# make dataframe
df = pd.DataFrame(data, index=[0])

st.download_button('download as csv', df, file_name="record.csv")

# save proof seperately

#if proof is not None:
#   file_details = {"FileName":proof.name,"FileType":proof.type}
#   df  = pd.read_csv(proof)
#   st.dataframe(df)
#   save_uploadedfile(proof)


# st.write(df)


# export data to storj - https://www.storj.io/blog/reading-and-writing-files-from-to-storj-with-pandas
# will just save local for now, but update this later

#df.to_csv('new_record.csv')

