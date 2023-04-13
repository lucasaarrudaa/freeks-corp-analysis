class Campaign:
    '''
    Parameters:
        campaign = STR     ex: (a, b, c)
        cpc = FLOAT        ex: (0.05)
        impressions = INT  ex: (1234324)
        ctr = FLOAT        ex: (0.89)
        cvr =  FLOAT       ex: (0.90)
        ROI = FLOAT/INT    ex: (12.5) or (50)
        sales = INT        ex: (1000)
    '''

    def __init__(self, campaign, cpc, impressions, ctr, cvr, roi, sales):

        self.name = campaign.upper()
        self.cpc = float(cpc)
        self.daily_impressions = float(impressions)
        self.ctr = float(ctr)/100
        self.cvr = float(cvr)/100
        self.roi = float(roi)/100
        self.daily_sales = float(sales)
        self.daily_clicks = self.daily_impressions * self.ctr
        self.daily_cost = self.daily_clicks * self.cpc
        self.daily_profit = self.roi * self.daily_cost
        self._cpa = self.daily_cost / self.daily_sales
        self.daily_revenue = self.daily_profit + (self._cpa*self.daily_sales)
        self.monthly_revenue = self.daily_revenue * 30
        self._rpa = self.daily_revenue / self.daily_sales
        self.monthly_profit = self.daily_profit * 30

    def crisis(self):

        self.new_roi = 1
        self.new_rpa = 10
        self.new_daily_revenue = (self.new_rpa * self.daily_sales)
        self.new_daily_cost = self.new_daily_revenue / 2
        self.new_cpc = self.new_daily_cost / \
            (self.daily_impressions * self.ctr)
        self.new_monthly_profit = (
            self.new_daily_revenue - self.new_daily_cost) * 30
        return print(f'\n\
                        \nNew CPC for campaign *{self.name}* should be ${self.new_cpc:,.2f}\
                        \nNew monthly profit should be $ {self.new_monthly_profit:,.2f}')

    def __str__(self):

        self.data = f'\n\
                    \nThe data for campaign *{self.name}* is:\
                    \nCpa: $ {self._cpa:,.2f}; \
                    \nRpa: $ {self._rpa:,.2f};\
                    \nDaily Clicks: {self.daily_clicks:,.0f};\
                    \nDaily Profit: $ {self.daily_profit:,.2f};\
                    \nMonthly Profit: $ {self.monthly_profit:,.2f};\
                    \nDaily Revenue: $ {self.daily_revenue:,.2f}\
                    \nMonthly Revenue: $ {self.monthly_revenue:,.2f};'
        return self.data
