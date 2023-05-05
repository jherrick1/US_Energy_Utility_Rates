import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px


st.markdown('''
# US Electricity Provider Rates
''')

# Import data
total_indust = pd.read_csv("data/total_indust.csv")
deliver_only = pd.read_csv("data/deliver_only.csv")
energy_only = pd.read_csv("data/energy_only.csv")
full_serve = pd.read_csv("data/full_serve.csv")
competitive = pd.read_csv("data/competitive.csv")

#Dict for provider data
provider_options = {" ":" ","Total Electric Industry":total_indust,"Delivery Only Providers":deliver_only,
                 "Energy Only Providers":energy_only,"Full-Service Providers":full_serve,"Competitive Service Providers":competitive}

#Select provider
provider = st.selectbox("Choose a provider type:", provider_options.keys())
prov_pick = provider_options.get(provider)

states = ' '

if provider != " ":
    #Populate state drop down with unique state lists for each provider
    states = prov_pick['State'].unique()
else:
    #Has all the states
    all_states = provider_options.get("Total Electric Industry")
    states = all_states['State'].unique()


#Sidebar
st.sidebar.header('Graph Settings')
year_select = st.sidebar.slider("Year Range",2010,2021, (2010,2021))
state_select = st.sidebar.multiselect("State(s)", options=states,default=['US'])
type_select = st.sidebar.selectbox("Sector", ('TOTAL','RESIDENTIAL','COMMERCIAL','INDUSTRIAL','TRANSPORTATION'))


tab1, tab2, tab3, tab4 = st.tabs(["Revenues","Sales","Customers","Price"])


if provider != " ":
    #filter the df based on user selection on sidebar
    #year default = 2010-2021
    #state default = US
    #sector default = Total for provider
    filtered_df = prov_pick[(prov_pick['Year'] >= year_select[0]) & (prov_pick['Year'] <= year_select[1]) & 
                            (prov_pick['State'].isin(state_select)) & (prov_pick['Sector'] == type_select)]

    with tab1:
        #Revenue Values
        val_type_df = filtered_df[filtered_df['Count Type'] == 'Revenues']

        fig = px.line(val_type_df,x="Year",y="Value",color="State",
                      labels={
                          "Value":"Revenues (Thousands $$)"
                      })
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        #Sales Values
        val_type_df = filtered_df[filtered_df['Count Type'] == 'Sales']

        fig = px.line(val_type_df,x="Year",y="Value",color="State",
                      labels={
                          "Value":"Sales (Megawatthours)"
                      })
        st.plotly_chart(fig, use_container_width=True)
    with tab3:
        #Customer Counts
        val_type_df = filtered_df[filtered_df['Count Type'] == 'Customers']

        fig = px.line(val_type_df,x="Year",y="Value",color="State",
                      labels={
                          "Value":"Customers (Counts)"
                      })
        st.plotly_chart(fig, use_container_width=True)
    with tab4:
        #Price Values
        val_type_df = filtered_df[filtered_df['Count Type'] == 'Price']

        fig = px.line(val_type_df,x="Year",y="Value",color="State",
                      labels={
                          "Value":"Price (Cents/kWh)"
                      })
        st.plotly_chart(fig, use_container_width=True)
