import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import st_folium
import streamlit.components.v1 as components

# A function that provides user input for the date range and grime type
def user_input(cleaned_data):
    # create a sidebar
    st.sidebar.header("User Input")
    # create a date range slider
    from_date = st.sidebar.date_input('From Date', pd.to_datetime('2014/01/01 00:00:00+00'), min_value=pd.to_datetime('2014/01/01 00:00:00+00'))
    to_date = st.sidebar.date_input('To Date', pd.to_datetime('2015/01/01 00:00:00+00'), min_value=pd.to_datetime('2015/01/01 00:00:00+00'))
    # create a dropdown menu for the grime type
    grime = st.sidebar.selectbox("Grime Type", cleaned_data['Description'].unique())
    return from_date, to_date, grime

from_date, to_date, grime = user_input(cleaned_data)

# Display the data
def display_data(cleaned_data, from_date, to_date, grime):

    # A function that focuses on the rows with 'GrimeDatetime' between the from_date and to_date
    def focus_grime_date_time_rows(data, from_date, to_date):
        # convert the from_date and to_date to str objects
        from_date = str(from_date)
        to_date = str(to_date)

        # focus on the rows with 'GrimeDatetime' between the from_date and to_date
        cleaned_data = data[data['GrimeDateTime'] > from_date]
        cleaned_data = cleaned_data[data['GrimeDateTime'] < to_date]

        return cleaned_data
    cleaned_data = focus_grime_date_time_rows(cleaned_data, from_date, to_date)

    st.write("Cleaned Data and Number of Grimes per Grime Type")
    col1, col2 = st.columns(2)
    col1.dataframe(cleaned_data) 
    col2.bar_chart(cleaned_data['Description'].value_counts(), height=500)

    # A function to display a line chart of the percent of each grime to all grimes per month
    def get_grime_percents():

        # create a DataFrame for each grime description
        waste_data = cleaned_data[cleaned_data['Description'] == 'WASTE']
        waste_management_data = cleaned_data[cleaned_data['Description'] == 'WASTE MANAGEMENT']
        vehicle_data = cleaned_data[cleaned_data['Description'] == 'VEHICLE']
        infrastructure_data = cleaned_data[cleaned_data['Description'] == 'INFRASTRUCTURE']
        animal_data = cleaned_data[cleaned_data['Description'] == 'ANIMAL']
        nature_data = cleaned_data[cleaned_data['Description'] == 'NATURE']
        vandalism_data = cleaned_data[cleaned_data['Description'] == 'VANDALISM']
        finance_data = cleaned_data[cleaned_data['Description'] == 'FINANCE']
        safety_data = cleaned_data[cleaned_data['Description'] == 'SAFETY']

        # convert value_counts() to periodindex
        waste_data['GrimeDateTime'] = pd.to_datetime(waste_data['GrimeDateTime'])
        waste_management_data['GrimeDateTime'] = pd.to_datetime(waste_management_data['GrimeDateTime'])
        vehicle_data['GrimeDateTime'] = pd.to_datetime(vehicle_data['GrimeDateTime'])
        infrastructure_data['GrimeDateTime'] = pd.to_datetime(infrastructure_data['GrimeDateTime'])
        animal_data['GrimeDateTime'] = pd.to_datetime(animal_data['GrimeDateTime'])
        nature_data['GrimeDateTime'] = pd.to_datetime(nature_data['GrimeDateTime'])
        vandalism_data['GrimeDateTime'] = pd.to_datetime(vandalism_data['GrimeDateTime'])
        finance_data['GrimeDateTime'] = pd.to_datetime(finance_data['GrimeDateTime'])
        safety_data['GrimeDateTime'] = pd.to_datetime(safety_data['GrimeDateTime'])

        # group each grime description by day
        waste_data = waste_data['GrimeDateTime'].value_counts().resample('M').sum()
        waste_management_data = waste_management_data['GrimeDateTime'].value_counts().resample('M').sum()
        vehicle_data = vehicle_data['GrimeDateTime'].value_counts().resample('M').sum()
        infrastructure_data = infrastructure_data['GrimeDateTime'].value_counts().resample('M').sum()
        animal_data = animal_data['GrimeDateTime'].value_counts().resample('M').sum()
        nature_data = nature_data['GrimeDateTime'].value_counts().resample('M').sum()
        vandalism_data = vandalism_data['GrimeDateTime'].value_counts().resample('M').sum()
        finance_data = finance_data['GrimeDateTime'].value_counts().resample('M').sum()
        safety_data = safety_data['GrimeDateTime'].value_counts().resample('M').sum()

        # convert value_counts() to periodindex
        cleaned_data['GrimeDateTime'] = pd.to_datetime(cleaned_data['GrimeDateTime'])

        # create a new DataFrame with all grimes and group by month
        all_data = cleaned_data['GrimeDateTime'].value_counts().resample('M').sum()

        # create the percent dataframe each grime to all grimes per month
        waste_percent_data = (waste_data / all_data) * 100
        waste_management_percent_data = (waste_management_data / all_data) * 100
        vehicle_percent_data = (vehicle_data / all_data) * 100
        infrastructure_percent_data = (infrastructure_data / all_data) * 100
        animal_percent_data = (animal_data / all_data) * 100
        nature_percent_data = (nature_data / all_data) * 100
        vandalism_percent_data = (vandalism_data / all_data) * 100
        finance_percent_data = (finance_data / all_data) * 100
        safety_percent_data = (safety_data / all_data) * 100

        # merge all the percent DataFrames into one DataFrame
        merged_data = pd.merge(waste_percent_data, waste_management_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count_x': '1 - Waste', 'count_y': '2 - Waste Management'})
        merged_data = pd.merge(merged_data, vehicle_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '3 - Vehicle'})
        merged_data = pd.merge(merged_data, infrastructure_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '8 - Infastructure'})
        merged_data = pd.merge(merged_data, animal_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '6 - Animal'})
        merged_data = pd.merge(merged_data, nature_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '4 - Nature'})
        merged_data = pd.merge(merged_data, vandalism_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '10 - Vandalism'})
        merged_data = pd.merge(merged_data, finance_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '9 - Finanace'})
        merged_data = pd.merge(merged_data, safety_percent_data, on='GrimeDateTime')
        merged_data = merged_data.rename(columns={'count': '5 - Safety'})
       

        return (merged_data)
    grime_percents = get_grime_percents()

    st.write("Number of Grimes per Month and Percent of Each Grime to All Grimes per Month")
    col1, col2 = st.columns(2)
    col1.area_chart(cleaned_data['GrimeDateTime'].value_counts().resample('M').sum())
    col2.area_chart(grime_percents)

    # create map
    grime_map = folium.Map(location=[cleaned_data['Latitude'].mean(), cleaned_data['Longitude'].mean()], zoom_start=12)

    # Create a MarkerCluster layer
    marker_cluster = plugins.MarkerCluster().add_to(grime_map)

    #used when hovering over popup
    tooltip = 'Click for more info'

    # add markers with popups for each location
    for index, row in cleaned_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"Description: {row['Description']}",
            icon=folium.Icon(color='red' if row['Description'] == grime else 'blue'),
            tooltip=tooltip
        ).add_to(marker_cluster)  # Add to the MarkerCluster layer instead of the grime_map directly

    
    # display and save map as HTML file
    grime_map.save('grime_map_with_clusters.html') 

    HtmlFile = open("grime_map_with_clusters.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=500)