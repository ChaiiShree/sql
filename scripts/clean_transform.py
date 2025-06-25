import pandas as pd

def clean_accident_data(input_csv):
    df = pd.read_csv(input_csv, low_memory=False)

    df = df[['ID', 'Severity', 'Start_Time', 'End_Time', 'City', 'State',
             'Temperature(F)', 'Humidity(%)', 'Weather_Condition',
             'Visibility(mi)', 'Wind_Speed(mph)']]

    df.columns = ['id', 'severity', 'start_time', 'end_time', 'city', 'state',
                  'temperature', 'humidity', 'weather_condition',
                  'visibility', 'wind_speed']

    df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce', format='%Y-%m-%d %H:%M:%S.%f')
    df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce', format='%Y-%m-%d %H:%M:%S.%f')
    df['accident_duration'] = df['end_time'] - df['start_time']

    df.dropna(subset=['start_time', 'end_time'], inplace=True)

    return df