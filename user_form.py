import streamlit as st
import pandas as pd
from PIL import Image

# with st.form("form0", clear_on_submit=True):
#     # Username & Password
#     # Match these to existing list: if no match, then invalid

#     username = st.text_input("Enter Username")
#     password = st.text_input("Enter Password")

#     submit_user = st.form_submit_button()


# https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")

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
            'Username': st.session_state["username"],
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

    # save proof seperately

    #if proof is not None:
    #   file_details = {"FileName":proof.name,"FileType":proof.type}
    #   df  = pd.read_csv(proof)
    #   st.dataframe(df)
    #   save_uploadedfile(proof)



    # st.write(df)


    # export data to storj - https://www.storj.io/blog/reading-and-writing-files-from-to-storj-with-pandas
    # will just save local for now, but update this later

    df.to_csv('new_record.csv')

