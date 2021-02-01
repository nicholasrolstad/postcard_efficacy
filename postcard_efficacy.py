import arcpy
import keyring
import os
import pandas as pd
from ussolar.zoho import download_zoho_report


creds = {'email':'nicholas.rolstad@us-solar.com', 'password': keyring.get_password('zoho', 'nicholas.rolstad@us-solar.com')}

state= 'IL'
address_list_csv = r'C:/Users/NicholasRolstad/Documents/GitHub/postcard_efficacy/address_lists/Ameren_address_list_2020-12-15.csv'

deals_report_name = 'IL Resi Deals - GIS'
leads_report_name = 'IL Resi Leads - GIS'


deals_df = download_zoho_report(creds, deals_report_name, r'C:\Users\NicholasRolstad\Downloads/{}.csv'.format(deals_report_name), return_df = True)
leads_df = download_zoho_report(creds, leads_report_name, r'C:\Users\NicholasRolstad\Downloads/{}.csv'.format(leads_report_name), return_df = True)
address_list_df = pd.read_csv(address_list_csv)

def join_name(c):
    name = c['NAME']
    name_parts = name.split()



address_list_df['Join Name 1'], address_list_df['Join Name 2'] = address_list_df.apply(join_name, axis=1)


leads_and_deals = []

def get_names(c, field):
    leads_and_deals.append(c[field].upper())
    

deals_df.apply(get_names, axis=1, args=('Deal Name',))
leads_df.apply(get_names, axis=1, args=('Full Name',))


deals_and_leads_df = address_list_df[address_list_df['Join Name'].isin(leads_and_deals)]