# Import Libraries to Program
import streamlit as st
import pandas as pd
from PIL import Image

#TODO: Configure Streamlit Page
tab_image = Image.open("Quantcorner_Logo.png")
st.set_page_config(page_title="Quantkorner Team", page_icon=tab_image, initial_sidebar_state='collapsed')



#TODO: All Function use in Web Application 
def highlight_p_values(values):
    if pd.notna(values) and pd.to_numeric(values, errors='coerce') < 0.05:
        return 'background-color: yellow'
    else:
        return ''
def main():
    st.title("Hello from QuantKorner Team")
    menu = ["🏠 Home", "🌎 ESG Knowledge", "📈 Our Projects", "👨‍👦‍👦 Our Team Members"]
    choice = st.sidebar.selectbox("Menu", menu)
#TODO: Home Section
    if choice == "🏠 Home":
        st.subheader("🏠 Home")
        with st.expander("How to เริ่มต้นศึกษา Quant"):
            st.write("How to เริ่มต้นศึกษา Quant")
        with st.expander("esg - ev/ebitda"):
            st.text("Results Linear Regression ESG - EV/EBITDA")
            #TODO: Display Images
            img = Image.open("esg-ev_ebitda.png")
            st.image(img, use_column_width=True)
            if st.button("ESG-Return Datasheet"):
                df1 = pd.read_csv("ESG-Return.csv")
                st.dataframe(df1)
                if st.checkbox("Show Datasheet"):
                    df2 = pd.read_excel("Linear_Regression_Coefficient_ESG_-_EVEbitda.xlsx")
                    st.dataframe(df2)


#TODO: What is ESG Section       
    elif choice == "🌎 ESG Knowledge":
        st.subheader("🌎 ESG Knowledge")
        #TODO: What is ESG? Article
        with st.expander("What is ESG"):
            img_what_is_esg = Image.open("what_is_esg.png")
            st.image(img_what_is_esg, use_column_width=True)
            st.subheader("What is ESG")
            st.write("")
            st.write("ESG is business the operation styles which not only focus just the profit  ")
            st.write("but also focus on the sustainabilyty which have 3 main factors considered  ")
            st.markdown("**1. Environment** - Indicated responsibilities of the enterprise to environment")
            st.write("                 for instance greenhouse gas, wasted and the pollution")
            st.write("2. Social - Measure the relationships management in the enterprise between  ")
            st.write("            employees, customers, stakeholders and also well being and human rights")
            st.write("3. Governance - ")


#TODO: Our Projects Section
    elif choice == "📈 Our Projects":
        st.subheader("📈 Our Projects")
        my_style = ["Select an option", "Causality","Predictive"]
        choice1 = st.selectbox("What is your forecast",my_style)
        if choice1 != "Select an option":
            st.success(f"You Selected {choice1}")
    
        if choice1 == "Causality":
            st.write("Causality Relationships Between ESG-Return and EV/EBITDA")
            img = Image.open("Templates.png")
            st.image(img, use_column_width=True)
            
        elif choice1 == "Predictive":
            predict_types = ["Select an option", "ESG - Return","ESG - EV/EBITDA"]
            choice2 = st.selectbox("What is your  prediction type?",predict_types)
            if choice2 != "Select an option":
                st.success(f"You Selected {choice2}")

            #TODO: When Users Choose ESG - Return
            if choice2 == "ESG - Return":
                return_indicator = ["Select an option", "p values", "coefficient", "varience"]
                choice3 = st.selectbox("Choose variables indicator",return_indicator)
                if choice3 != "Select an option":
                    st.success(f"You Selected {choice3}")
                #TODO: Users Choose ESG - Return => P Values
                if choice3 == "p values":
                    factor_return_p = ["Select an option", "1 Factor","2 Factor","3 Factor","4 Factor","5 Factor","6 Factor", "7 Factor", "8 Factor", "9 Factor", "10 Factor"]
                    choice9 = st.selectbox("How many factor you considered",factor_return_p)
                    if choice9 != "Select an option":
                        st.success(f"You Selected {choice9}")
                    #TODO: Users Choose ESG - Return => P Values => 1 Factor
                    if choice9 == "1 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_1factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - Return => P Values => 2 Factor
                    if choice9 == "2 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_2factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 
                    #TODO: Users Choose ESG - Return => P Values => 3 Factor
                    if choice9 == "3 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_3factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 
                    #TODO: Users Choose ESG - Return => P Values => 4 Factor
                    if choice9 == "4 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_4factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - Return => P Values => 5 Factor
                    if choice9 == "5 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_5factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - Return => P Values => 6 Factor
                    if choice9 == "6 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_6factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 
                    #TODO: Users Choose ESG - Return => P Values => 7 Factor
                    if choice9 == "7 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_7factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 
                    #TODO: Users Choose ESG - Return => P Values => 8 Factor
                    if choice9 == "8 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_8factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - Return => P Values => 9 Factor
                    if choice9 == "9 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_9factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 
                    #TODO: Users Choose ESG - Return => P Values => 10 Factor
                    if choice9 == "10 Factor":
                        df = pd.read_csv("ESG_Return/p_values/Regression_P-Value_ESG_-_Return_10factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df) 

                #TODO: Users Choose ESG - Return => Coefficient
                elif choice3 == "coefficient":
                    factor_return_coefficient = ["Select an option", "1 Factor","2 Factor","3 Factor","4 Factor","5 Factor","6 Factor", "7 Factor", "8 Factor", "9 Factor", "10 Factor"]
                    choice10 = st.selectbox("How many factor you considered",factor_return_coefficient)
                    if choice10 != "Select an option":
                        st.success(f"You Selected {choice10}")
                    #TODO: Users Choose ESG - Return => Coefficient => 1 Factor
                    if choice10 == "1 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_1factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 2 Factor
                    elif choice10 == "2 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_2factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 3 Factor
                    elif choice10 == "3 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_3factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 4 Factor
                    elif choice10 == "4 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_4factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 5 Factor
                    elif choice10 == "5 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_5factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 6 Factor
                    elif choice10 == "6 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_6factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 7 Factor
                    elif choice10 == "7 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_7factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 8 Factor
                    elif choice10 == "8 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_8factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 9 Factor
                    elif choice10 == "9 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_9factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - Return => Coefficient => 10 Factor
                    elif choice10 == "10 Factor":
                        df = pd.read_csv("ESG_Return/coefficient/Regression_Coefficient_ESG_-_Return_10factor.csv")
                        st.dataframe(df)

                
                #TODO: Users Choose ESG - Return => Varience
                elif choice3 == "varience":
                    df = pd.read_csv("ESG_Return/Varience/Regression_R-Squared_ESG_-_Return.csv")
                    st.dataframe(df)

            #TODO: When Users Choose ESG - EV/EBITDA
            elif choice2 == "ESG - EV/EBITDA":
                ebitda_indicator = ["Select an option", "p values", "coefficient", "varience"]
                choice4 = st.selectbox("Choose variables indicator",ebitda_indicator)
                if choice4 != "Select an option":
                    st.success(f"You Selected {choice4}")

                #TODO: Users Choose ESG - EV/EBITDA => P Values
                if choice4 == "p values":
                    factor_ebitda_p = ["Select an option", "1 Factor","2 Factor","3 Factor","4 Factor","5 Factor","6 Factor", "7 Factor", "8 Factor", "9 Factor", "10 Factor"]
                    choice6 = st.selectbox("How many factor you considered",factor_ebitda_p)
                    if choice6 != "Select an option":
                        st.success(f"You Selected {choice6}")
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 1 Factor
                    if choice6 == "1 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_1factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 2 Factor
                    elif choice6 == "2 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_2factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 3 Factor
                    elif choice6 == "3 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_3factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 4 Factor
                    elif choice6 == "4 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_4factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 5 Factor
                    elif choice6 == "5 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_5factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 6 Factor
                    elif choice6 == "6 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_6factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 7 Factor
                    elif choice6 == "7 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_7factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 8 Factor
                    elif choice6 == "8 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_8factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 9 Factor
                    elif choice6 == "9 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_9factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                    #TODO: Users Choose ESG - EV/EBITDA => P Values => 10 Factor
                    elif choice6 == "10 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/p_values/P-Value_ESG_-_EVEbitda_10factor.csv")
                        styled_df = df.style.apply(lambda x: x.map(highlight_p_values))
                        st.dataframe(styled_df)
                        

                #TODO: Users Choose ESG - EV/EBITDA => Coefficient
                elif choice4 == "coefficient":
                    factor_ebitda_coefficient = ["Select an option", "1 Factor","2 Factor","3 Factor","4 Factor","5 Factor","6 Factor", "7 Factor", "8 Factor", "9 Factor", "10 Factor"]
                    choice7 = st.selectbox("How many factor you considered",factor_ebitda_coefficient)
                    if choice7 != "Select an option":
                        st.success(f"You Selected {choice7}")
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 1 Factor
                    if choice7 == "1 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_1factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 2 Factor
                    elif choice7 == "2 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_2factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 3 Factor
                    elif choice7 == "3 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_3factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 4 Factor
                    elif choice7 == "4 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_4factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 5 Factor
                    elif choice7 == "5 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_5factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 6 Factor
                    elif choice7 == "6 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_6factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 7 Factor
                    elif choice7 == "7 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_7factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 8 Factor
                    elif choice7 == "8 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_8factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 9 Factor
                    elif choice7 == "9 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_9factor.csv")
                        st.dataframe(df)
                    #TODO: Users Choose ESG - EV/EBITDA => Coefficient => 10 Factor
                    elif choice7 == "10 Factor":
                        df = pd.read_csv("ESG-EVEBITDA/coefficient/Regression_Coefficient_ESG_-_EVEbitda_10factor.csv")
                        st.dataframe(df)
                        
                
                #TODO: Users Choose ESG - EV/EBITDA => Varience
                elif choice4 == "varience":
                    df = pd.read_csv("ESG-EVEBITDA/Varience/Regression_R-Squared_ESG_-_EVEbitda.csv")
                    st.dataframe(df)

#TODO: Our Team Members Section
    else: 
        st.subheader("👨‍👦‍👦 Our Team Members")
        img_profiles = Image.open("Members.png")
        st.image(img_profiles, use_column_width=True)
        #with st.expander("Name Eakunut"):
            #st.write("Results Linear Regression ESG - EV/EBITDA")
        


if __name__ == '__main__':
    main()

#ยังไม่มี choice 11