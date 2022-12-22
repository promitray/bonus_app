import pandas as pd
from sqlalchemy import create_engine
from bonus_sql import return_query
import bonus_rates
import streamlit as st

target_berlin_cons = st.sidebar.number_input('Berlin Consulting: Target', value = 20000)
target_london_cons = st.sidebar.number_input('London Consulting: Target', value = 20000)
target_munich_cons = st.sidebar.number_input('Munich Consulting: Target', value = 20000)
target_newyork_cons = st.sidebar.number_input('New York Consulting: Target', value = 20000)
target_sf_cons = st.sidebar.number_input('San Francisco Consulting: Target', value = 20000)
target_santiago_cons = st.sidebar.number_input('Santiago Consulting: Target', value = 20000)
target_seoul_cons = st.sidebar.number_input('Seoul Consulting: Target', value = 20000)
target_shanghai_cons = st.sidebar.number_input('Shanghai Consulting: Target', value = 20000)
target_tokyo_cons = st.sidebar.number_input('Tokyo Consulting: Target', value = 20000)
target_lahore_cons = st.sidebar.number_input('Lahore Consulting: Target', value = 20000)

target_berlin_ls = st.sidebar.number_input('Berlin LS: Target', value = 28000)
target_london_ls = st.sidebar.number_input('London LS: Target', value = 28000)
target_newyork_ls = st.sidebar.number_input('New York LS: Target', value = 28000)
target_sf_ls = st.sidebar.number_input('San Francisco LS: Target', value = 28000)
target_seoul_ls = st.sidebar.number_input('Seoul LS: Target', value = 18000)
target_shanghai_ls = st.sidebar.number_input('Shanghai LS: Target', value = 16000)
target_tokyo_ls = st.sidebar.number_input('Tokyo LS: Target', value = 14500)
target_santiago_ls = st.sidebar.number_input('Santiago LS: Target', value = 28000)


bonus_rates_2023 = {'verticals': {
                            'Consulting': { 'costs': {
                                           70: {'Berlin': 1.0,
                                               'London': 1.0,
                                               'Munich': 1.0,
                                               'New York': 1.0,
                                               'San Francisco': 1.0,
                                               'Santiago': 1.0,
                                               'Seoul': 1.0,
                                               'Shanghai': 1.0,
                                               'Tokyo': 1.0,
                                               'Lahore': 1.0},
                                           80: {
                                                'Berlin' : 4.0,
                                                'London': 4.0,
                                                'Munich': 4.0,
                                                'New York': 4.0,
                                                'San Francisco': 4.0,
                                                'Santiago': 4.0,
                                                'Seoul': 4.0,
                                                'Shanghai': 4.0,
                                                'Tokyo': 4.0,
                                                'Lahore': 1.5
                                               },
                                           90: {
                                                'Berlin': 6.0,
                                                'London': 6.0,
                                                'Munich': 6.0,
                                                'New York': 6.0,
                                                'San Francisco': 6.0,
                                                'Santiago': 6.0,
                                                'Seoul': 6.0,
                                                'Shanghai': 6.0,
                                                'Tokyo': 6.0,
                                                'Lahore': 2.0
                                                },
                                           100: {
                                                'Berlin': 8.0,
                                                'London': 8.0,
                                                'Munich': 8.0,
                                                'New York': 8.0,
                                                'San Francisco': 8.0,
                                                'Santiago': 8.0,
                                                'Seoul': 8.0,
                                                'Shanghai': 8.0,
                                                'Tokyo': 8.0,
                                                'Lahore': 2.3 
                                           },
                                           110: {
                                                'Berlin': 8.3,
                                                'London': 8.3,
                                                'Munich': 8.3,
                                                'New York': 8.3,
                                                'San Francisco': 8.3,
                                                'Santiago': 8.3,
                                                'Seoul': 8.3,
                                                'Shanghai': 8.3,
                                                'Tokyo': 8.3,
                                                'Lahore': 2.5 
                                           },
                                           120: {
                                                'Berlin': 8.7,
                                                'London': 8.7,
                                                'Munich': 8.7,
                                                'New York': 8.7,
                                                'San Francisco': 8.7,
                                                'Santiago': 8.7,
                                                'Seoul': 8.7,
                                                'Shanghai': 8.7,
                                                'Tokyo': 8.7,
                                                'Lahore': 2.7 
                                           },
                                           140: {
                                                'Berlin': 9.0,
                                                'London': 9.0,
                                                'Munich': 9.0,
                                                'New York': 9.0,
                                                'San Francisco': 9.0,
                                                'Santiago': 9.0,
                                                'Seoul': 9.0,
                                                'Shanghai': 9.0,
                                                'Tokyo': 9.0,
                                                'Lahore': 3.0
                                           }
                            },
                                         'targets' : {
                                             'Berlin': target_berlin_cons,
                                             'London': target_london_cons,
                                             'Munich': target_munich_cons,
                                             'New York': target_newyork_cons,
                                             'San Francisco': target_sf_cons,
                                             'Santiago': target_santiago_cons,
                                             'Seoul': target_seoul_cons,
                                             'Shanghai': target_shanghai_cons,
                                             'Tokyo': target_tokyo_cons,
                                             'Lahore': target_lahore_cons

                                         }
                                          },
                            'Life Sciences': {'costs': {
                                           70: {'Berlin' : 1.5,
                                                'London': 1.5,
                                                'Munich': 1.5,
                                                'New York': 1.5,
                                                'San Francisco': 1.5,
                                                'Santiago': 1.5,
                                                'Seoul': 1.5,
                                                'Shanghai': 1.5,
                                                'Tokyo': 1.5,
                                                'Lahore': 1.5},
                                           80: {
                                                'Berlin' : 3.0,
                                                'London': 3.0,
                                                'Munich': 3.0,
                                                'New York': 3.0,
                                                'San Francisco': 3.0,
                                                'Santiago': 3.0,
                                                'Seoul': 3.0,
                                                'Shanghai': 3.0,
                                                'Tokyo': 3.0,
                                                'Lahore': 3.0
                                               },
                                           90: {
                                                'Berlin': 5.0,
                                                'London': 5.0,
                                                'Munich': 5.0,
                                                'New York': 5.0,
                                                'San Francisco': 5.0,
                                                'Santiago': 5.0,
                                                'Seoul': 5.0,
                                                'Shanghai': 5.0,
                                                'Tokyo': 5.0,
                                                'Lahore': 5.0
                                                },
                                           100: {
                                                'Berlin': 7.0,
                                                'London': 7.0,
                                                'Munich': 7.0,
                                                'New York': 7.0,
                                                'San Francisco': 7.0,
                                                'Santiago': 7.0,
                                                'Seoul': 7.0,
                                                'Shanghai': 7.0,
                                                'Tokyo': 7.0,
                                                'Lahore': 2.3 
                                           },
                                           110: {
                                                'Berlin': 7.3,
                                                'London': 7.3,
                                                'Munich': 7.3,
                                                'New York': 7.3,
                                                'San Francisco': 7.3,
                                                'Santiago': 7.3,
                                                'Seoul': 7.3,
                                                'Shanghai': 7.3,
                                                'Tokyo': 7.3,
                                                'Lahore': 2.5 
                                           },
                                           120: {
                                                'Berlin': 7.7,
                                                'London': 7.7,
                                                'Munich': 7.7,
                                                'New York': 7.7,
                                                'San Francisco': 7.7,
                                                'Santiago': 7.7,
                                                'Seoul': 7.7,
                                                'Shanghai': 7.7,
                                                'Tokyo': 7.7,
                                                'Lahore': 2.7 
                                           },
                                           140: {
                                                'Berlin': 8.0,
                                                'London': 8.0,
                                                'Munich': 8.0,
                                                'New York': 8.0,
                                                'San Francisco': 8.0,
                                                'Santiago': 8.0,
                                                'Seoul': 8.0,
                                                'Shanghai': 8.0,
                                                'Tokyo': 8.0,
                                                'Lahore': 3.0
                                           } 
                                          },
                                          'targets' : {
                                             'Berlin': target_berlin_ls,
                                             'London': target_london_ls,
                                             'Munich': 0,
                                             'New York': target_newyork_ls,
                                             'San Francisco': target_sf_ls,
                                             'Santiago': target_santiago_ls,
                                             'Seoul': target_seoul_ls,
                                             'Shanghai': target_shanghai_ls,
                                             'Tokyo': target_tokyo_ls,
                                             'Lahore': 0

                                         }
                                          }
                            }
                            } 

def bonus_calculator(df, bonus_rates, target_margin, bonus):
 df.loc[df['employee_atheneum_office'] == 'Lahore', 'bonus_office'] = 'Lahore'
 df.loc[df['employee_atheneum_office'] == 'Berlin', 'bonus_office'] = 'Berlin'
 df.loc[df['employee_atheneum_office'] == 'London', 'bonus_office'] = 'London'
 df.loc[df['employee_atheneum_office'] == 'Munich', 'bonus_office'] = 'Munich'
 df.loc[df['employee_atheneum_office'] == 'New York', 'bonus_office'] = 'New York'
 df.loc[df['employee_atheneum_office'] == 'San Francisco', 'bonus_office'] = 'San Francisco'
 df.loc[df['employee_atheneum_office'] == 'Santiago', 'bonus_office'] = 'Santiago'
 df.loc[df['employee_atheneum_office'] == 'Seoul', 'bonus_office'] = 'Seoul'
 df.loc[df['employee_atheneum_office'] == 'Tokyo', 'bonus_office'] = 'Tokyo'
 df.loc[df['employee_atheneum_office'] == 'Shanghai', 'bonus_office'] = 'Shanghai'


 df['margin_performance_pcent'] = (df['margin']/ df[target_margin]) * 100
 
 df.loc[(df['margin_performance_pcent'] >= 99.50), 'margin_performance_pcent'] = 100.0
 

 df['bonus_multiplier'] = 0
 
 for vertical in bonus_rates['verticals']:
        bonus_intervals = list(bonus_rates['verticals'][vertical]['costs'])
        v = 0
        for achievement_lower in bonus_intervals:
          #print (achievement_lower, bonus_intervals[-1])
          if achievement_lower != bonus_intervals[-1]:
           for location in bonus_rates['verticals'][vertical]['costs'][achievement_lower]:
             achievement_higher = bonus_intervals[1 + v]
             bonus_multiplier = bonus_rates['verticals'][vertical]['costs'][achievement_lower][location]
             df.loc[(df['team_vertical'] == vertical) & (df['margin_performance_pcent'] >= achievement_lower) & (df['margin_performance_pcent'] < achievement_higher) & (df['bonus_office'] == location), 'bonus_multiplier'] = bonus_multiplier * 0.01
          else:
             for location in bonus_rates['verticals'][vertical]['costs'][achievement_lower]:
              bonus_multiplier = bonus_rates['verticals'][vertical]['costs'][achievement_lower][location]
              df.loc[(df['team_vertical'] == vertical) & (df['margin_performance_pcent'] >= achievement_lower) & (df['bonus_office'] == location), 'bonus_multiplier'] = bonus_multiplier * 0.01
          v = v + 1 
  

 df[bonus] = df['bonus_multiplier'] * df['margin']
 return df


#### Main Program Start #####################


#engine = create_engine('postgresql://promitray:s2ChPGiqedLRXAxjc9MAGkUODfMKfDHS09NhE1YX@dwh.czxnn9fmc6d9.eu-central-1.redshift.amazonaws.com:5439/ard')
#query = return_query()
#engine.execute(query)

#dates = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01']
dates = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01']

overview_list = []
margins_overview_list = []

for ref_date in dates:
  
  df = pd.read_csv('%s.csv'%ref_date)

  df['target_margin_2023'] = 0
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Berlin'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Berlin']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'London'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['London']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Munich'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Munich']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'New York'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['New York']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'San Francisco'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['San Francisco']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Santiago'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Santiago']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Seoul'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Seoul']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Shanghai'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Shanghai']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Tokyo'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Tokyo']
  df.loc[(df['team_vertical'] == 'Consulting') & (df['employee_atheneum_office'] == 'Lahore'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Consulting']['targets']['Lahore']

  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Berlin'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Berlin']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'London'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['London']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Munich'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Munich']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'New York'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['New York']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'San Francisco'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['San Francisco']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Santiago'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Santiago']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Seoul'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Seoul']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Shanghai'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Shanghai']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Tokyo'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Tokyo']
  df.loc[(df['team_vertical'] == 'Life Sciences') & (df['employee_atheneum_office'] == 'Lahore'), 'target_margin_2023'] = bonus_rates_2023['verticals']['Life Sciences']['targets']['Lahore']

  df = df[df['target_margin_2023'] != 0]


  df = bonus_calculator(df, bonus_rates_2023, 'target_margin_2023', 'bonus_2023')

  del df['margin_performance_pcent']
  del df['bonus_multiplier']


  df = bonus_calculator(df, bonus_rates.bonus_rates_2022, 'target_margin', 'bonus_2022')

 #print (df[['margin', 'target_margin', 'target_margin_2023', 'bonus_2023', 'bonus_2022', 'employee_atheneum_office', 'team_vertical']])

  df['bonus_difference'] = df['bonus_2023'] - df['bonus_2022']
  df['achievement % (old)'] = (df['margin']/df['target_margin']) * 100
  df['achievement % (new)'] = (df['margin']/df['target_margin_2023']) * 100

  df_positive = df[df['bonus_2023'] > df['bonus_2022']]
  df_negative  = df[df['bonus_2023'] < df['bonus_2022']]

 
  #df[['margin', 'target_margin', 'bonus_2022', 'achievement % (old)', 'target_margin_2023', 'bonus_2023', 'achievement % (new)', 'bonus_difference', 'employee_atheneum_office', 'team_vertical', 'bamboo_id', 'employee_name']].to_excel(writer,sheet_name = 'bonus' + ' _' + ref_date)
  #df_positive[['margin', 'target_margin', 'bonus_2022', 'achievement % (old)', 'target_margin_2023', 'bonus_2023', 'achievement % (new)','bonus_difference', 'employee_atheneum_office', 'team_vertical', 'bamboo_id', 'employee_name']].to_excel(writer, sheet_name = 'bonus_pos' + ' _' + ref_date)
  #df_negative[['margin', 'target_margin', 'bonus_2022', 'achievement % (old)', 'target_margin_2023', 'bonus_2023',  'achievement % (new)', 'bonus_difference', 'employee_atheneum_office', 'team_vertical', 'bamboo_id', 'employee_name']].to_excel(writer, sheet_name = 'bonus_neg'+ ' _' + ref_date)

  consulting_ass_2022 = df[df['team_vertical'] == 'Consulting']['bonus_2022'].sum()
  consulting_ass_2023 = df[df['team_vertical'] == 'Consulting']['bonus_2023'].sum()
  ls_ass_2022 = df[df['team_vertical'] == 'Life Sciences']['bonus_2022'].sum()
  ls_ass_2023 = df[df['team_vertical'] == 'Life Sciences']['bonus_2023'].sum()
  total_ass_2022 = df['bonus_2022'].sum()
  total_ass_2023 = df['bonus_2023'].sum()

  df_consulting = df[df['team_vertical'] == 'Consulting']
  df_ls = df[df['team_vertical'] == 'Life Sciences']

  print (df_ls)

  n_consulting_2022 = df_consulting[df_consulting['bonus_2022'] > 0].shape[0]
  n_consulting_2023 = df_consulting[df_consulting['bonus_2023'] > 0].shape[0]
  n_ls_2022 = df_ls[df_ls['bonus_2022'] > 0].shape[0]
  n_ls_2023 =  df_ls[df_ls['bonus_2023'] > 0].shape[0]
  n_total_2022 =  df[df['bonus_2022'] > 0].shape[0]
  n_total_2023 =  df[df['bonus_2023'] > 0].shape[0]


  #### achievement percentages #####

  margin_0_70_2022 = (df[df['achievement % (old)'] < 70].shape[0]/df.shape[0]) * 100
  margin_0_70_2023 = (df[df['achievement % (new)'] < 70].shape[0]/df.shape[0]) * 100
  margin_70_80_2022 = (df[(df['achievement % (old)'] > 70) & (df['achievement % (old)'] < 80)].shape[0]/df.shape[0]) * 100
  margin_70_80_2023 = (df[(df['achievement % (new)'] > 70) & (df['achievement % (new)'] < 80)].shape[0]/df.shape[0]) * 100
  margin_80_90_2022 = (df[(df['achievement % (old)'] > 80) & (df['achievement % (old)'] < 90)].shape[0]/df.shape[0]) * 100
  margin_80_90_2023 = (df[(df['achievement % (new)'] > 80) & (df['achievement % (new)'] < 90)].shape[0]/df.shape[0]) * 100
  margin_90_100_2022 = (df[(df['achievement % (old)'] > 90) & (df['achievement % (old)'] < 100)].shape[0]/df.shape[0]) * 100
  margin_90_100_2023 = (df[(df['achievement % (new)'] > 90) & (df['achievement % (new)'] < 100)].shape[0]/df.shape[0]) * 100
  margin_100_110_2022 = (df[(df['achievement % (old)'] > 100) & (df['achievement % (old)'] < 110)].shape[0]/df.shape[0]) * 100
  margin_100_110_2023 = (df[(df['achievement % (new)'] > 100) & (df['achievement % (new)'] < 110)].shape[0]/df.shape[0]) * 100
  margin_110_120_2022 = (df[(df['achievement % (old)'] > 110) & (df['achievement % (old)'] < 120)].shape[0]/df.shape[0]) * 100
  margin_110_120_2023 = (df[(df['achievement % (new)'] > 110) & (df['achievement % (new)'] < 120)].shape[0]/df.shape[0]) * 100
  margin_120_140_2022 = (df[(df['achievement % (old)'] > 120) & (df['achievement % (old)'] < 140)].shape[0]/df.shape[0]) * 100
  margin_120_140_2023 = (df[(df['achievement % (new)'] > 120) & (df['achievement % (new)'] < 140)].shape[0]/df.shape[0]) * 100
  margin_140_plus_2022 = (df[df['achievement % (old)'] > 140].shape[0]/df.shape[0]) * 100
  margin_140_plus_2023 = (df[df['achievement % (new)'] > 140].shape[0]/df.shape[0]) * 100



  margins_overview = {
                       'reference_date': ref_date,
                       '<70 % Margin (old)': margin_0_70_2022,
                       '<70 % Margin (new)': margin_0_70_2023,
                       '70-80 % (old)': margin_70_80_2022,
                       '70-80 % (new)': margin_70_80_2023,
                       '80-90 % (old)': margin_80_90_2022,
                       '80-90 % (new)': margin_80_90_2023,
                       '90-100 % (old)': margin_90_100_2022,
                       '90-100 % (new)': margin_90_100_2023,
                       '100-110 % (old)': margin_100_110_2022,
                       '100-110 % (new)': margin_100_110_2023,
                       '110-120 % (old)': margin_110_120_2022,
                       '110-120 % (new)': margin_110_120_2023,
                       '120-140 % (old)': margin_120_140_2022,
                       '120-140 % (new)': margin_120_140_2023,
                       '>140 % Margin (old)': margin_140_plus_2022,
                       '>140 % Margin (new)': margin_140_plus_2023
  }

  margins_overview_list.append(margins_overview)


  overview = { 'reference_date': ref_date,
               'Ass_consulting_2022' : consulting_ass_2022,
               'n_consulting_2022': n_consulting_2022,
               'Ass_consulting_2023' : consulting_ass_2023,
               'n_consulting_2023': n_consulting_2023,
               'Ass_LS_2022' : ls_ass_2022,
               'n_LS_2022': n_ls_2022,
               'Ass_LS_2023' : ls_ass_2023,
               'n_LS_2023': n_ls_2023,
               'Ass_total_2022': total_ass_2022,
               'n_total_2022': n_total_2022,
               'Ass_total_2023': total_ass_2023,
               'n_total_2023': n_total_2023
  }
  overview_list.append(overview)

df = pd.DataFrame(overview_list)

df_margin = pd.DataFrame(margins_overview_list)

print (df_margin)

st.title('Margin Distribution Analysis', anchor=None)

st.dataframe(df_margin)
st.title('Bonus Statistics Analysis', anchor=None)
st.dataframe (df)

df['Ass_consulting_diff'] = df['Ass_consulting_2023'] - df['Ass_consulting_2022']
df['Ass_LS_diff'] = df['Ass_LS_2023'] - df['Ass_LS_2022']
df['Ass_total_diff'] = df['Ass_total_2023'] - df['Ass_total_2022']

st.title('Cost Difference Analysis', anchor=None)
st.dataframe (df[['reference_date', 'Ass_consulting_diff', 'Ass_LS_diff', 'Ass_total_diff']])



#with pd.ExcelWriter('summary_stats.xlsx') as writer:

#df.to_excel(writer, sheet_name = 'statistics') 



#df[['reference_date', 'Ass_consulting_diff', 'Ass_LS_diff', 'Ass_total_diff']].to_excel(writer, sheet_name = 'cost_differences')
#df_margin.to_excel(writer, sheet_name = 'margin_analysis')





  


     
            
          
          
        



















