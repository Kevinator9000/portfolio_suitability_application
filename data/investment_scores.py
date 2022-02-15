import pandas as pd

def score_calculator(investment_amount, annual_income, annual_expenses, investing_experience, income_stability, risk_level, investment_length, investment_strategy):
        risk_score = 0
        time_score = 0

        investment_percent = investment_amount / annual_income
        disposible_income = annual_income - annual_expenses
        investment_ratio = disposible_income / investment_amount

        if investment_percent < .40:
            risk_score += 10
        elif investment_percent > .40 and investment_percent < .80:
            risk_score -= -10
        else:
            risk_score += 0

        if investing_experience < 4:
            risk_score -= 10
        elif investing_experience > 4 and investing_experience < 9:
            risk_score += 0
        else:
            risk_score += 10

        if income_stability == 'Yes':
            risk_score += 0
        else:
            risk_score -= 40

        if risk_level == "Low":
            risk_score += 0
        elif risk_level == "Moderate":
            risk_score += 25
        elif risk_level == "High":
            risk_score += 50


        if investment_strategy == "Income":
            risk_score += 0
        elif investment_strategy == "Income/Value":
            risk_score += 20
        elif investment_strategy == "Income/Growth":
            risk_score += 20
        elif investment_strategy == "Income/Growth/Value":
            risk_score += 25
        elif investment_strategy == "Growth":
            risk_score += 30
        elif investment_strategy == "Value":
            risk_score += 30
        elif investment_strategy == "Growth/Value":
            risk_score += 30

        return risk_score, time_score


def get_client_portfolio(risk_score, time_score):
    fixed_income = [.02, .38, .45, .04, .11]
    profile_1 = [.02, .30, .36, .03, .09, .12, .08]
    profile_2 = [.02, .19, .23, .04, .08, .04, .18, .06, .16]
    profile_3 = [.02, .09, .23, .04, .08, .04, .24, .09, .03, .20, .04]
    profile_4 = [.02, .03, .06, .03, .03, .03, .32, .10, .06, .26, .06]
    profile_5 = [.02, .38, .13, .07, .33, .07]

    # portfolio_list = [fixed_income, profile_1, profile_2, profile_3, profile_4 ,profile_5]
    # portfolio = []
    
    if risk_score in range(0, 11):
        client_portfolio = fixed_income
        port_profile = "Fixed Income"
    elif risk_score in range(11, 21):
        client_portfolio = profile_1
        port_profile = "Profile 1"
    elif risk_score in range(21, 41):
        client_portfolio = profile_2
        port_profile = "Profile 2"
    elif risk_score in range(41, 61):
        client_portfolio = profile_3
        port_profile = "Profile 3"
    elif risk_score in range(61, 81):
        client_portfolio = profile_4
        port_profile = "Profile 4"
    elif risk_score:
        client_portfolio = profile_5
        port_profile = "Profile 5"

    return client_portfolio, port_profile, risk_score

def get_MC_end_date(investment_length):
    MC_end_date = []
    if investment_length == "0-1":
        MC_end_date = pd.Timestamp("2021-02-01", tz="America/New_York").isoformat()
    if investment_length == "2-4":
        MC_end_date = pd.Timestamp("2020-02-01", tz="America/New_York").isoformat()
    if investment_length == "5-9":
        MC_end_date = pd.Timestamp("2019-02-01", tz="America/New_York").isoformat()
    if investment_length == "10+":
        MC_end_date = pd.Timestamp("2019-02-01", tz="America/New_York").isoformat()
    return MC_end_date