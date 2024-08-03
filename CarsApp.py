import streamlit as st
import pickle

model = pickle.load(open('cars.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Second Hand Car Prediction using Machine Learning")


    ## Brand
    brand_display = ('Toyota','Honda','Ford','Maruti','Hyundai','Tata','Mahindra','Volkswagen','Audi','BMW','Mercedes')
    brand_options = list(range(len(brand_display)))
    brands = st.selectbox("Choose Brand",brand_options, format_func=lambda x: brand_display[x])


    ## Model
    model_display = ('Corolla','Civic','Mustang','Swift','Sonata','Nexon','Scorpio','Polo''A4','X1','C-Class','Endeavour','Creta','Harrier','Ertiga','City','Tiguan','Q3','5 Series','GLC','Innova','Figo','Verna','Altroz','Thar','Passat','A6','X3','E-Class','Fortuner','Aspire','Elantra','Safari','Vitara','WR-V','Ameo','A3','7 Series','GLE','Yaris','Ranger','Santro','Tigor','S-Cross','BR-V','T-Roc','Q7','X5','GLA','Camry','Venue','Tiago','XUV300','Vento','A5','3 Series','Innova Crysta','EcoSport')
    model_options = list(range(len(model_display)))
    models = st.selectbox("Choose Model",model_options, format_func=lambda x: model_display[x])

    ## Year
    year_display = ('2016','2017','2018','2019','2020','2021')
    year_options = list(range(len(year_display)))
    years = st.selectbox("Year of Manufacture",year_options, format_func=lambda x: year_display[x])

     ## Kilometres
    km = st.number_input('Enter Kilometres Driven')

    ## For Fuel Type
    fuel_display = ('Petrol','Diesel')
    fuel_options = list(range(len(fuel_display)))
    fuel = st.selectbox("Fuel Type",fuel_options, format_func=lambda x: fuel_display[x])

    ## For Transmission Type
    tt_display = ('Manual','Automatic')
    tt_options = list(range(len(tt_display)))
    tt = st.selectbox("Transmission Type",tt_options, format_func=lambda x: tt_display[x])

    ## For Owner Type
    owner_display = ('First','Second', 'Third')
    owner_options = list(range(len(owner_display)))
    owner = st.selectbox("Owner Type",owner_options, format_func=lambda x: owner_display[x])

     ## Mileage
    mileage = st.number_input('Enter Mileage', value=0)

    ## Engine
    engine = st.number_input("Enter Engine",value=0)

    ## Power
    power= st.number_input("Enter Power",value=0)

    ##Seats
    seats_level = ('4', '5', '7')
    seats_options = list(range(len(seats_level)))
    seats = st.selectbox("Seats",seats_options, format_func=lambda x: seats_level[x])


    if st.button("Submit"):
        features = [[brands, models, years, km, fuel, tt,owner, mileage, engine,power,seats]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = weight
        if ans == 0:
            st.error('Error')
        else:
            st.success(ans)
            

run()