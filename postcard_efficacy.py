import arcpy
import keyring
import selenium
from ussolar.zoho import download_zoho_report


creds = {'email':'nicholas.rolstad@us-solar.com', 'password': keyring.get_password('zoho', 'nicholas.rolstad@us-solar.com')}

state= 'IL'

deals_report_name = 'IL Resi Deals - GIS'
leads_report_name = 'IL Resi Leads - GIS'


deals = download_zoho_report(creds, deals_report_name, 'C:/Users/NicholasRolstad/Desktop/{}.csv'.format(deals_report_name), return_df = True)