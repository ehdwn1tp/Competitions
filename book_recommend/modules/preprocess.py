import pandas as pd

class Preprocessor:
    def __init__(self, age_lower=0, age_upper=100, year_lower=1991, year_upper=2021):
        self.age_lower = age_lower
        self.age_upper = age_upper
        self.year_lower = year_lower
        self.year_upper = year_upper

    def run(self, df):
        df = self.clip_age(df)
        df = self.clip_pub_year(df)
        return df

    def clip_age(self, df):
        df['Age'] = df['Age'].apply(lambda x: x if x >= self.age_lower else self.age_lower)
        df['Age'] = df['Age'].apply(lambda x: x if x <= self.age_upper else self.age_upper)
        return df

    def clip_pub_year(self, df):
        df['Year-Of-Publication'] = df['Year-Of-Publication'].apply(lambda x: x if x >= self.year_lower else self.year_lower)
        df['Year-Of-Publication'] = df['Year-Of-Publication'].apply(lambda x: x if x <= self.year_upper else self.year_upper)
        return df