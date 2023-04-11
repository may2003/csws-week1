import pandas as pd
import matplotlib.pyplot as plt

# Load the hotel reservation data into a DataFrame
df = pd.read_csv(r'C:\\Users\mayta\OneDrive - Liverpool John Moores University\csws-week1\HotelReservations.csv')


def reservations_season():
    # remove cancelled bookings
    booking = df.loc[df['booking_status'] != 'Cancelled']

    # Extract the columns we need for the visualization
    data = df[['arrival_month', 'arrival_year']]

    # data by season and arrival year
    seasons = {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter'
    }
    data['season'] = data['arrival_month'].map(seasons)

    # Calculate the total number of bookings for each season and arrival year
    season_counts = data.groupby(['season', 'arrival_year']).size().unstack()

    # Create a bar chart to visualize the number of bookings for each season and arrival year
    season_counts.plot(kind='bar')
    plt.title('Hotel Reservations by Season and Arrival Year')
    plt.xlabel('Season')
    plt.ylabel('Number of Bookings')
    plt.legend(title='Arrival Year')
    plt.show()
reservations_season()
