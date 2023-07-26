import streamlit as st
import pickle
import base64

recommendation = pickle.load(open('Recommendation.pkl', 'rb'))
production=pickle.load(open('Production.pkl','rb'))

crops=['apple','banana','blackgram','chickpea','coconut','coffee','cotton','grapes','jute','kidneybeans','lentil',
       'maize','mango','mothbeans','mungbean','muskmelon','orange','papaya','pigeonpeas','pomegranate','rice','watermelon']

seasons=['Autumn','Kharif','Rabi','Summer','Whole Year','Winter']

def product(response):
    return "Your Yield for this crop is approximately : ",response[0]

def recommend(answer):
    
    return answer[0] + " is the best crop for cultivation here."

def set_background_image(image_path):
    image_base64 = base64.b64encode(open(image_path, 'rb').read()).decode()
    background_image_style = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{image_base64}");
            background-size: cover;
        }}
        </style>
    '''
    st.markdown(background_image_style, unsafe_allow_html=True)

def main():
    st.title("EasyFarm")
    option=st.sidebar.selectbox("Select Season ",seasons)
    #st.subheader(option)
    if (option=='Autumn'):
        season=0
    elif (option=='Kharif'):
        season=1
    elif (option=='Rabi'):
        season=2
    elif (option=='Summer'):
        season=3
    elif (option=='Winter'):
        season=5
    else :
        season=4
    background_image_path = "C:/Users/DEVI SRI PRASAD/FarmEasy/bg.jpg"
    set_background_image(background_image_path)
    year=st.text_input("Year : ",'')
    area=st.text_input('Area : ','')
    sn = st.text_input('Nitogen (N) : ','')
    sp = st.text_input('Phosphorous (P) : ','')
    pk = st.text_input('Potassium (K) : ','')
    pt = st.text_input('Temperature : ','')
    phu = st.text_input('Humidity : ','')
    pPh = st.text_input('pH Level : ','')
    pr = st.text_input('RainFall : ','')
    inputs = [[sn, sp, pk, pt, phu, pPh, pr]]
    if st.button('Recommend Crop'):
        x=recommendation.predict(inputs)
        crop=crops.index(x[0])
        inputs1=[[year,season,crop,area]]
        st.success(recommend(x))
        st.success(product(production.predict(inputs1)))
    
if __name__ == '__main__':
    main()