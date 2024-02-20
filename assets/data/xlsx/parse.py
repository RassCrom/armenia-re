import pandas as pd

# Assuming your CSV file is named 'your_file.csv'
df = pd.read_csv(r"D:\projects\web\armenia_re\armenia-re\assets\data\xlsx\amenia-energy.csv")

# Extracting data for the required years (1991 to 2022)
df_selected_years = df.iloc[:, :33]
years = [str(year) for year in range(1991, 2023)]

# Removing commas and converting to numeric for 'Generation' and 'Fossil fuels' columns
for i in df.head():
    df_selected_years[i] = pd.to_numeric(df_selected_years[i].str.replace(',', '.'), errors='coerce')

# Creating the dataset in the desired format
data_set =[
            {
                'name': year,
                'children': [
                    {'name': 'Generation', 'value': float(row['Generation'])},
                    {'name': 'Nuclear', 'value': float(row['Nuclear'])},
                    {'name': 'Fossil fuels', 'value': float(row['Fossil fuels'])},
                    {'name': 'Renewables', 'value': float(row['Renewables'])},
                    {'name': 'Hydroelectricity', 'value': float(row['Hydroelectricity'])},
                    {'name': 'Non-hydroelectric renewables', 'value': float(row['Non-hydroelectric renewables'])},
                    {'name': 'Geothermal', 'value': float(row['Geothermal'])},
                    {'name': 'Solar, tide, wave, fuel cell', 'value': float(row['Solar, tide, wave, fuel cell'])},
                    {'name': 'Tide and wave', 'value': float(row['Tide and wave'])},
                    {'name': 'Solar', 'value': float(row['Solar'])},
                    {'name': 'Wind', 'value': float(row['Wind'])},
                    {'name': 'Biomass and waste', 'value': float(row['Biomass and waste'])},
                    {'name': 'Hydroelectric pumped storage', 'value': float(row['Hydroelectric pumped storage'])},
                    {'name': 'Consumption', 'value': float(row['Consumption'])},
                    {'name': 'Imports', 'value': float(row['Imports'])},
                    {'name': 'Exports', 'value': float(row['Exports'])},
                    {'name': 'Distribution losses', 'value': float(row['Distribution losses'])},
                ]
            } for year, row in zip(years, df_selected_years.to_dict('records'))
]

# Creating the final dataset
final_dataset = f"var dataSet = [{{children: {data_set}}}];"

# Printing the result
print(final_dataset)
