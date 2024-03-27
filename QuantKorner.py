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
        st.markdown("Please Select Section In The Sidebar")


#TODO: What is ESG Section       
    elif choice == "🌎 ESG Knowledge":
        st.subheader("🌎 ESG Knowledge")
        #TODO: What is ESG? Article
        with st.expander("📈 What is ESG"):
            img_what_is_esg = Image.open("what_is_esg.png")
            st.image(img_what_is_esg, use_column_width=True)
            st.subheader("What is ESG")
            st.write("")
            st.markdown("ESG is a business operation style that not only focuses on profit but also on sustainability, considering three main factors:")
            st.markdown("**1. Environment** - This involves the responsibilities of the enterprise towards the environment, such as greenhouse gas emissions, waste management, and pollution.")
            st.markdown("**2. Social** - This measures the management of relationships within the enterprise, including those with employees, customers, stakeholders, as well as considerations for well-being and human rights.")
            st.markdown("**3. Governance** - This indicates the management system within the company to ensure that operations are efficient and transparent.")
            st.markdown("In conclusion, ESG helps to build trust in the business by reflecting the duties of enterprises and outlining operation plans for long-term business development.")
        #TODO: How to เริ่มต้นศึกษา Qaunt Article
        with st.expander("💸 How to เริ่มต้นศึกษา Quant (09/03/2024)"):
            img_study_quant = Image.open("study_quant.jpg")
            st.image(img_study_quant, use_column_width=True)
            st.subheader("How to เริ่มต้นศึกษา Quant")
            st.write("")
            st.markdown("ตั้งแต่เดือนธันวาปี 2023 เราได้ join งาน Hackathon ของ QuantCorner จนตอนนี้ก็ทำงานกันมาได้จะครบ 3 เดือนแล้ว โพสต์นี้เราเลยอยากเล่า journey การศึกษา quant จาก 0 ในช่วง 3 เดือนที่ผ่านมาของพวกเราครับ")
            st.markdown("เรื่องราวเริ่มที่เนม นิสิตจบใหม่จากคณะเศรษฐศาสตร์ เจอกับนท นิสิตวิศวะบังเอิญนั่งข้างกันตอนไปเรียนการ optimize พอร์ดลงทุนด้วย python กับอาจารย์เอ็ม เพราะสนใจการใช้ math ในการลงทุน")
            st.markdown("แล้ววันสุดท้ายของการเรียน พี่ ๆ QuantCorner ที่จัดคลาส ก็มีเกริ่น ๆ ให้ทุกคนฟัง ว่า เฮ้ย จริง ๆ เราใส่ esg (เอาเป็นว่าเป็นค่าที่ไว้บอกว่าบริษัทนั้นบริษัทนี้ยั่งยืนขนาดไหน) + ลงไปตอนทำใน portfolio optimization ด้วยก็ได้ปะ (เช่น อาจจะใส่เป็น constraint เป็นต้น) และก็ชวนว่าถ้าใครอยากลุยต่อ เรามี hackathon ให้ลงนะ")
            st.markdown("ก่อนกลับบ้านวันนั้นเนมเลยชวนนทลง hackathon เลย (ก็มันต่อเนื่องมาจากคลาสเลยอะเนอะ) แล้วไม่กี่วันหลังจากนั้นก็ลากพี เพื่อนที่กำลังเรียนวิศวะไฟฟ้าเข้าทีมมาอีกคนด้วย เป็นอันครบ party")
            st.markdown("เราตั้งชื่อทีมของพวกเราว่าทีม QuantKorner (ที่ไม่มีตัว C)")
            st.markdown("โจทย์ของ Hackathon นี้คือ the quest for sustainable alpha ****โดยสิ่งที่ได้มาก็คือชุดข้อมูลที่เกี่ยวกับความยั่งยืนของบริษัทในไทย ตั้งแต่เรื่องสิ่งแวดล้อม การจัดการ ไปจนคะแนนสังคมในบริษัท ส่วนสิ่งที่เราต้องทำคือการเอาข้อมูลพวกนี้มาเป็นส่วนหนึ่งของการละเลงโมเดลให้นำไปสู่ผลตอบแทน (รอบ proposal มีโจทย์คือจะทำอะไรก็ทำเลย ลองส่งมา ขอแค่โยงค่าความยั่งยืนเข้ามาในโมเดลด้วยก็คือโอเคแล้ว)")
            st.markdown("แต่พอมาถกกันในทีม เราก็มีความแคลงใจเกี่ยวกับค่าความยั่งยืนกันนิดนึง เพราะเมื่อส่วนนึงของค่าความยั่งยืนมันประเมินมาจากความรักโลก แต่คำถามคือเอาจริง ๆ บริษัทที่รักโลกมากมันน่าจะทำตังค์ได้น้อยกว่าบริษัทปกติ ๆ รึเปล่า (คิดแบบเร็ว ๆ เราคิดว่าเรื่องยั่งยืน ๆ มันดูจะเป็น constraint ที่ทำให้ได้ผลตอบแทนน้อยลง มากกว่าจะเป็นตัวใส่โมเดลแล้วพาไปหาผลตอบแทน) แต่เราก็ทำงานต่อมาเรื่อย ๆ โดยเชื่อว่าสุดท้ายแล้วเดี๋ยวข้อมูลมันก็ตอบเราเอง ว่าค่าความยั่งยืนมันเวิร์กจริงรึเปล่า")
            st.markdown("ตอนแรกทีมเราก็ยังหลง ๆ กันอยู่ สิ่งที่เราทำก็เลยเป็นการหยิบความรู้ portfolio opt ที่พึ่งเรียนจบมาใช้ โดยลองเอาค่าไส้ในของคะแนนความยั่งยืนมาแบ่งหุ้นไทยออกเป็น 2 กลุ่ม คือกลุ่มที่มีค่านั้นสูง กับกลุ่มที่มีค่านั้นต่ำ จากนั้นก็เอาแต่ละกลุ่มไปทำ optimization แล้วลองเทียบค่าความเสี่ยง (ทีมใช้ variance) ว่าจากการลองพล็อต variance ของทุกค่ากลุ่มสูงกับกลุ่มต่ำ มันแตกต่างกันมากน้อยขนาดไหน สิ่งที่เจอคือมันก็ไม่ได้แตกต่างกันมากเท่าที่เราคิด")
            st.markdown("จากนั้นทีมก็เริ่มคิดกันว่า เอ แล้วเราจะทำยังไงดีนะให้งานของเรามีกิมมิคอะไรบ้างอย่าง ตอนนั้นเนมที่จบเศรษฐศาสตร์ก็เลยเสนอว่างั้นเราเอาพวกตัวแปรเศรษฐศาสตร์ทั้งหลายมาโยงไว้ในโมเดลสำหรับจัดพอร์ตด้วยไหม จนไป ๆ มา ๆ ต่อมาเราก็ได้รู้ว่า อ๋อ จริง ๆ การทำแบบนี้มันมีชื่อเรียกอยู่แล้ว คือการทำ factor model")
            st.markdown("จากการคุยกับพี่ย้วย ที่ปรึกษาของทีม พี่ย้วยก็แนะนำว่าถ้าจะเลือกทำ factor model ก็ไม่ควรทำ port opt แบบที่เราทำตอนพึ่งเริ่มทำงานใหม่ ๆ ไปด้วย เพราะ port opt อาจกลายเป็นตัว dominate ผลลัพธ์ (ค่า beta) ของ factor model ไป ถ้าเลือกจะลุย factor model แล้วก็มุ่งทางนี้ไปเลยดีกว่า")
            st.markdown("factor model จริง ๆ แล้วคณิตศาสตร์มันก็คือการทำ regression เลย แต่ประเด็นคือการจะโยงความสัมพันธ์ระหว่างตัวแปรต้นกับตัวแปรตามที่เราสนใจได้ ก่อนอื่นเราก็ต้องรู้ก่อนว่าแล้วตัวแปรต้นตัวไหนบ้างล่ะที่เวิร์ก ก็จะมีเซ็ตตัวแปรต้น standard อยู่ อย่าง fama french บ้าง, q-factor บ้าง ซึ่งได้รับการพิสูจน์มาแล้วว่าชนะตลาดในระยะยาว")
            st.markdown("สรุปก็คือตอนนี้ทีมเรากำลังเล่นกับความสัมพันธ์ของค่าความยั่งยืนกับผลตอบแทน แล้วจากนั้นจะก็จะลองโยงเซ็ตตัวแปรต้น standard เข้ามาเล่นด้วย")
            st.markdown("ตัวงานของกลุ่มเรา จะออกมาในรูปแบบของงานวิจัย และ dashboard ตอนนี้สมาชิกทีมทุกคนก็กำลังอ่านหนังสือ งานวิจัย ลองเล่นกับข้อมูล ศึกษาเกี่ยวกับความยั่งยืน และ factor model พยายามสร้างชิ้นงานที่มีคุณภาพออกมาอยู่ โดยเมื่องานของเราเสร็จสมบูรณ์แล้ว เราจะขอกลับมาเล่าสิ่งที่เราเจอ และที่มาที่ไปของงานเราให้ทุกคนฟังกันอีกหนนะครับ")
            st.markdown("ไว้เจอกันนะ")
            st.markdown("เนม พี นท - QuantKorne")
        with st.expander("🌳ESG Predictive Power Thailand"):
            img_conclusion = Image.open("esg_predictive.png")
            st.image(img_conclusion, use_column_width=True)
            st.subheader("ESG Predictive Power Thailand")
            st.write("")
            st.markdown("Businesses with good ESG (Environmental, Social, and Governance) practices reflect their ability to compete and potential for long-term growth.")
            st.markdown("Since business is about solving problems, increasing positive impacts, and reducing negative impacts, it is the responsibility of businesses to be concerned with ESG.")
            st.markdown("The source of funds in the business sector comes from investments in finance. This leads to the question of whether businesses with good ESG performance benefit investors.")
            st.markdown("We specifically focus on two aspects: returns and investor sentiment, using EV/EBITDA (Enterprise Value to Earnings Before Interest, Taxes, Depreciation, and Amortization) as a proxy for stock premium.")
            st.markdown("Before starting the research, we hypothesized that ESG would have a positive relationship with return rates, as sustainable growth should be reflected in returns. Additionally, we hypothesized that ESG would have a positive relationship with EV/EBITDA, as companies with good ESG scores should receive a premium valuation due to their impact on consumer choices.")
            st.markdown("We began by running a simple linear regression, using ESG Factors (data from LSEG, using 2022 data as it was the most complete and closest to the current year, 2024) as the independent variables, and returns and EV/EBITDA as the dependent variables.")
            st.markdown("Since linear regression assumes no multicollinearity among independent variables, we used the Variance Inflation Factor (VIF) to filter out correlated variables, removing those with a VIF greater than 10, leaving us with 10 independent variables.")
            st.markdown("Additionally, we ran multiple linear regressions, varying the number of independent variables from 1 to 10, to gain insights into how the model's behavior changes.For the return linear regression, we found two significant variables: Emissions Score and Workforce Score, which remained significant in many cases as we added more variables. These variables had a positive relationship with returns, aligning with our hypothesis. Therefore, focusing on Emission Score and Workforce Score could increase the chances of higher returns.")
            st.markdown("For the EV/EBITDA linear regression, we found four significant variables: Human Rights Score, Resource Use Score, CSR Strategy Score (which captures the communication of ESG practices), and Emission Score. The first three had a negative relationship, contrary to our hypothesis, while Emission Score had a positive relationship.")
            st.markdown("Furthermore, when running a single-variable linear regression, the only significant ESG variable for EV/EBITDA was Human Rights Score. The researcher attributes this to the lack of interaction terms in the model, which could explain why some variables became significant when combined but not when isolated.")
            st.write("")
            st.markdown("**Number of grandslam final played by Roger Federe is highly correlate to the number of electrical engineer in the mexico.**")
            


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