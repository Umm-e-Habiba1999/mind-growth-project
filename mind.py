import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title = "Data Sweeper" ,layout= 'wide')

#custom css
st.markdown(
    """
    <style>
    .stApp{
    background-color:dark grey;
    color: white;
    }
    <style/>
    """,
    unsafe_allow_html=True
)

#title anddescription
st.title("📈Datasweeper Sterling Integrator By Umm-E-Habiba")
st.write("Transform your files between csv and excel formates with built-in data visualization creating the project for quarter 3!")

#file uploader
uploaded_files = st.file_uploader("upload your files(accepts CSV or Excel):",type=["cvs" , "xlsx"], accept_multiple_files=(True))

if uploaded_files :
    for file in uploaded_files :
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
           df = pd.read_csv(file)
        elif file_ext == "xlsx":
           df = pd.read_excel(file)
    else:
            st.error(f"unsupported files type : {file_ext}")
            continue

            #file details
            st.write("📊preview the head of the Dataframe")
            st.dataframe(df.head())

            #data cleaning options
            st.subheader("🧹Data cleaning option")
            if st.checkbox(f"clean data for {file.name}"):
                  col1, col2 = st.columns(2)

                  with col1:
                    if st.button(f"Remove dublicates from the file {files.name}"):
                        df.drop_duplicates (inplace=True)
                        st.write ("Duplicatesremoved!")

                        with col2:
                            if st.button(f"File missing value for {file.name}"):
                                numeric_cols = df.select_dtypes(include=['number']).columns
                                df[numeric_cols] =df[numeric_cols].filena(df[numeric_cols].mean())
                                st.write("Missing values have been failed!")



                                st.subheader("✔️Select columns to keep")
                                column = st.multiselectsd(f"choose columnfor {file.name}",df.colomn,default=df.coloumn)
                                df = df[columns]


                                #data visualization
                                st.subheader("📀Data visualization")
                                if st.checkbox(f"show visualization for {file.name}"):
                                    st.bar_chart(df.select_dtypes(include= 'number'),iloc[:,:2])
                                    #conversion option
                                    st.subheader("Conversion option")
                                    conversion_type = st.radio(f"convert {file.name} to:" , ["cvs" , "Excel"], key=files.name)
                                    if st.button(f"convert{file.nme}"):
                                        buffer = BytesIO()
                                        if conversion_type == "csv" :
                                             df.to.csv(buffer, index=False)
                                              file_name = file.name.replace(file_ext, ".csv")
                                            mime_type = "text/csv"

                                            elif conversion_type == 'Excel':
                                                df.to_excel(buffer, index=False)
                                                file_name = file.name.replace (file_ext, "xlsx")
                                                main-tye = "application/vnd.openxmlformats-officedocumnt.spreadsheetml.sheet"
                                                buffer.seek(0)

                                                st.download_button(
                                                    label=f"Download {file.name} as {conversion_type}",
                                                    data=buffer,
                                                    file_name=file_name,
                                                    mime=mime_type
                                                )
                                   
                                    st.success("🙌All files processed successfully!")
