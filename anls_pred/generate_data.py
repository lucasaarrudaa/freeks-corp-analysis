import random
import numpy as np
import pandas as pd
from IPython.display import display

campaigns = ['A', 'B', 'C', 'D']
cpc = [0.05, 0.1, 0.15, 0.1]
impressions_per_day = [12484395, 2884615, 6920415, 3885004]
ctr = [0.0089, 0.0120, 0.0102, 0.0198]
cvr = [0.0090, 0.0260, 0.0170, 0.0130]
roi = [1.0, 1.5, 0.8, 0.5]
daily_sales = [1000, 900, 1200, 1000]
cpa = [5.56, 3.85, 8.82, 7.69]
rpa = [11.11, 9.62, 15.88, 13.08]
monthly_profit = [166666.67, 155769.21, 254117.64, 161538.47]


class Campaign:

    def __init__(self, name, cpc, impressions_per_day, ctr, cvr, roi, daily_sales, cpa, rpa, monthly_profit):
        self.name = name
        self.cpc = cpc
        self.impressions_per_day = impressions_per_day
        self.ctr = ctr
        self.cvr = cvr
        self.roi = roi
        self.daily_sales = daily_sales
        self.cpa = cpa
        self.rpa = rpa
        self.monthly_profit = monthly_profit

    def update_historical_data(self):

        var_cpc = min(
            max(self.ctr * random.uniform(-0.5, 0.5), 0.01), 0.5)
        var_impressions_per_day = self.impressions_per_day * \
            random.uniform(-0.5, 0.5)
        var_ctr = min(max(self.ctr * random.uniform(-0.5, 0.5), 0.01), 5)
        var_cvr = self.cvr * random.uniform(-0.5, 0.5)
        var_roi = min(max(self.ctr * random.uniform(-0.5, 0.3), 0.01), 4)
        var_daily_sales = self.daily_sales * random.uniform(-0.5, 0.5)
        var_cpa = self.cpa * random.uniform(-0.5, 0.3)
        var_rpa = self.rpa * random.uniform(-0.5, 0.3)
        var_monthly_profit = self.monthly_profit * random.uniform(-0.5, 0.5)

        self.cpc += var_cpc
        self.impressions_per_day += var_impressions_per_day
        self.ctr += var_ctr
        self.cvr += var_cvr
        self.roi += var_roi
        self.daily_sales += var_daily_sales
        self.cpa += var_cpa
        self.rpa += var_rpa
        self.monthly_profit += var_monthly_profit


def generate_year_data(campaigns, months):
    monthly_data = []
    for month in range(1, months + 1):
        monthly_data_per_campaign = {}
        for campaign in campaigns:
            campaign.update_historical_data()
            monthly_data_per_campaign[campaign.name] = {
                'cpc': round(campaign.cpc, 2),
                'impressions_per_day': round(campaign.impressions_per_day, 2),
                'ctr': round(campaign.ctr, 4),
                'cvr': round(campaign.cvr, 4),
                'roi': round(campaign.roi, 3),
                'daily_sales': round(campaign.daily_sales, 2),
                'cpa': round(campaign.cpa, 2),
                'rpa': round(campaign.rpa, 2),
                'monthly_profit': round(campaign.monthly_profit, 2)
            }
        monthly_data.append(monthly_data_per_campaign)
    return monthly_data


all_years = []

for year in range(1800, 2100):

    campaign_A = Campaign(campaigns[0], cpc[0], impressions_per_day[0], ctr[0],
                          cvr[0], roi[0], daily_sales[0], cpa[0], rpa[0], monthly_profit[0])
    campaign_B = Campaign(campaigns[1], cpc[1], impressions_per_day[1], ctr[1],
                          cvr[1], roi[1], daily_sales[1], cpa[1], rpa[1], monthly_profit[1])
    campaign_C = Campaign(campaigns[2], cpc[2], impressions_per_day[2], ctr[2],
                          cvr[2], roi[2], daily_sales[2], cpa[2], rpa[2], monthly_profit[2])
    campaign_D = Campaign(campaigns[3], cpc[3], impressions_per_day[3], ctr[3],
                          cvr[3], roi[3], daily_sales[3], cpa[3], rpa[3], monthly_profit[3])

    campaigns = [campaign_A, campaign_B, campaign_C, campaign_D]

    months = 12

    year_data = generate_year_data(campaigns, months)

    all_years.append(year_data)


def create_month_df(var_month, month, year):

    df = pd.DataFrame.from_dict(var_month, orient='index')

    df['month'] = [f'{month}'] * len(df)
    df['year'] = [f'{year}'] * len(df)
    df['campaign'] = df.index

    columns = ['year', 'month', 'campaign', 'cpc', 'impressions_per_day',
               'ctr', 'cvr', 'roi', 'daily_sales', 'cpa', 'rpa', 'monthly_profit']
    df = df[columns]

    return df


all_years_df = []

# Loop to cycle through years and months
for year, year_data in enumerate(all_years, start=1950):
    for month, month_data in enumerate(year_data, start=1):
        year_df = create_month_df(month_data, month, year)
        all_years_df.append(year_df)

campaign_data_df = pd.concat(all_years_df, ignore_index=True)
campaings_name = ['A', 'B', 'C', 'D']
num_repeticoes = len(campaign_data_df) // len(campaings_name)
new_column = campaings_name * num_repeticoes
campaign_data_df['campaign'] = new_column[:len(campaign_data_df)]
print(campaign_data_df)

campaign_data_df.to_csv('campaigns_data.csv', index=False)
