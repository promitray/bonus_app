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
target_shanghai_cons = st.sidebar.number_input('Shanghai Consulting: Target', value = 18000)
target_tokyo_cons = st.sidebar.number_input('Tokyo Consulting: Target', value = 18000)
target_lahore_cons = st.sidebar.number_input('Lahore Consulting: Target', value = 13000)

target_berlin_ls = st.sidebar.number_input('Berlin LS: Target', value = 28000)
target_london_ls = st.sidebar.number_input('London LS: Target', value = 28000)
target_newyork_ls = st.sidebar.number_input('New York LS: Target', value = 28000)
target_sf_ls = st.sidebar.number_input('San Francisco LS: Target', value = 28000)
target_seoul_ls = st.sidebar.number_input('Seoul LS: Target', value = 18000)
target_shanghai_ls = st.sidebar.number_input('Shanghai LS: Target', value = 16000)
target_tokyo_ls = st.sidebar.number_input('Tokyo LS: Target', value = 14500)
target_santiago_ls = st.sidebar.number_input('Santiago LS: Target', value = 28000)

#### Consulting

berlin_cons_70 = st.sidebar.number_input('Berlin Bonus %: Consulting 70-80 %', value = 1.0)
berlin_cons_80 = st.sidebar.number_input('Berlin Bonus %: Consulting 80-90 %', value = 4.0)
berlin_cons_90 = st.sidebar.number_input('Berlin Bonus %: Consulting 90-100 %', value = 6.0)
berlin_cons_100 = st.sidebar.number_input('Berlin Bonus %: Consulting 100-110 %', value = 8.0)
berlin_cons_110 = st.sidebar.number_input('Berlin Bonus %: Consulting 110-120 %', value = 8.3)
berlin_cons_120 = st.sidebar.number_input('Berlin Bonus %: Consulting 120-140 %', value = 8.7)
berlin_cons_140 = st.sidebar.number_input('Berlin Bonus %: Consulting > 140 %', value = 9.0)

london_cons_70 = st.sidebar.number_input('London Bonus %: Consulting 70-80 %', value = 1.0)
london_cons_80 = st.sidebar.number_input('London Bonus %: Consulting 80-90 %', value = 4.0)
london_cons_90 = st.sidebar.number_input('London Bonus %: Consulting 90-100 %', value = 6.0)
london_cons_100 = st.sidebar.number_input('London Bonus %: Consulting 100-110 %', value = 8.0)
london_cons_110 = st.sidebar.number_input('London Bonus %: Consulting 110-120 %', value = 8.3)
london_cons_120 = st.sidebar.number_input('London Bonus %: Consulting 120-140 %', value = 8.7)
london_cons_140 = st.sidebar.number_input('London Bonus %: Consulting > 140 %', value = 9.0)

munich_cons_70 = st.sidebar.number_input('Munich Bonus %: Consulting 70-80 %', value = 1.0)
munich_cons_80 = st.sidebar.number_input('Munich Bonus %: Consulting 80-90 %', value = 4.0)
munich_cons_90 = st.sidebar.number_input('Munich Bonus %: Consulting 90-100 %', value = 6.0)
munich_cons_100 = st.sidebar.number_input('Munich Bonus %: Consulting 100-110 %', value = 8.0)
munich_cons_110 = st.sidebar.number_input('Munich Bonus %: Consulting 110-120 %', value = 8.3)
munich_cons_120 = st.sidebar.number_input('Munich Bonus %: Consulting 120-140 %', value = 8.7)
munich_cons_140 = st.sidebar.number_input('Munich Bonus %: Consulting > 140 %', value = 9.0)

newyork_cons_70 = st.sidebar.number_input('New York Bonus %: Consulting 70-80 %', value = 1.0)
newyork_cons_80 = st.sidebar.number_input('New York Bonus %: Consulting 80-90 %', value = 4.0)
newyork_cons_90 = st.sidebar.number_input('New York Bonus %: Consulting 90-100 %', value = 6.0)
newyork_cons_100 = st.sidebar.number_input('New York Bonus %: Consulting 100-110 %', value = 8.0)
newyork_cons_110 = st.sidebar.number_input('New York Bonus %: Consulting 110-120 %', value = 8.3)
newyork_cons_120 = st.sidebar.number_input('New York Bonus %: Consulting 120-140 %', value = 8.7)
newyork_cons_140 = st.sidebar.number_input('New York Bonus %: Consulting > 140 %', value = 9.0)

sf_cons_70 = st.sidebar.number_input('San Francisco Bonus %: Consulting 70-80 %', value = 1.0)
sf_cons_80 = st.sidebar.number_input('San Francisco Bonus %: Consulting 80-90 %', value = 4.0)
sf_cons_90 = st.sidebar.number_input('San Francisco Bonus %: Consulting 90-100 %', value = 6.0)
sf_cons_100 = st.sidebar.number_input('San Francisco Bonus %: Consulting 100-110 %', value = 8.0)
sf_cons_110 = st.sidebar.number_input('San Francisco Bonus %: Consulting 110-120 %', value = 8.3)
sf_cons_120 = st.sidebar.number_input('San Francisco Bonus %: Consulting 120-140 %', value = 8.7)
sf_cons_140 = st.sidebar.number_input('San Francisco Bonus %: Consulting > 140 %', value = 9.0)

santiago_cons_70 = st.sidebar.number_input('Santiago Bonus %: Consulting 70-80 %', value = 1.0)
santiago_cons_80 = st.sidebar.number_input('Santiago Bonus %: Consulting 80-90 %', value = 4.0)
santiago_cons_90 = st.sidebar.number_input('Santiago Bonus %: Consulting 90-100 %', value = 6.0)
santiago_cons_100 = st.sidebar.number_input('Santiago Bonus %: Consulting 100-110 %', value = 8.0)
santiago_cons_110 = st.sidebar.number_input('Santiago Bonus %: Consulting 110-120 %', value = 8.3)
santiago_cons_120 = st.sidebar.number_input('Santiago Bonus %: Consulting 120-140 %', value = 8.7)
santiago_cons_140 = st.sidebar.number_input('Santiago Bonus %: Consulting > 140 %', value = 9.0)

seoul_cons_70 = st.sidebar.number_input('Seoul Bonus %: Consulting 70-80 %', value = 1.0)
seoul_cons_80 = st.sidebar.number_input('Seoul Bonus %: Consulting 80-90 %', value = 4.0)
seoul_cons_90 = st.sidebar.number_input('Seoul Bonus %: Consulting 90-100 %', value = 6.0)
seoul_cons_100 = st.sidebar.number_input('Seoul Bonus %: Consulting 100-110 %', value = 8.0)
seoul_cons_110 = st.sidebar.number_input('Seoul Bonus %: Consulting 110-120 %', value = 8.3)
seoul_cons_120 = st.sidebar.number_input('Seoul Bonus %: Consulting 120-140 %', value = 8.7)
seoul_cons_140 = st.sidebar.number_input('Seoul Bonus %: Consulting > 140 %', value = 9.0)

shanghai_cons_70 = st.sidebar.number_input('Shanghai Bonus %: Consulting 70-80 %', value = 1.0)
shanghai_cons_80 = st.sidebar.number_input('Shanghai Bonus %: Consulting 80-90 %', value = 4.0)
shanghai_cons_90 = st.sidebar.number_input('Shanghai Bonus %: Consulting 90-100 %', value = 6.0)
shanghai_cons_100 = st.sidebar.number_input('Shanghai Bonus %: Consulting 100-110 %', value = 8.0)
shanghai_cons_110 = st.sidebar.number_input('Shanghai Bonus %: Consulting 110-120 %', value = 8.3)
shanghai_cons_120 = st.sidebar.number_input('Shangai Bonus %: Consulting 120-140 %', value = 8.7)
shanghai_cons_140 = st.sidebar.number_input('Shanghai Bonus %: Consulting > 140 %', value = 9.0)

tokyo_cons_70 = st.sidebar.number_input('Tokyo Bonus %: Consulting 70-80 %', value = 1.0)
tokyo_cons_80 = st.sidebar.number_input('Tokyo Bonus %: Consulting 80-90 %', value = 4.0)
tokyo_cons_90 = st.sidebar.number_input('Tokyo Bonus %: Consulting 90-100 %', value = 6.0)
tokyo_cons_100 = st.sidebar.number_input('Tokyo Bonus %: Consulting 100-110 %', value = 8.0)
tokyo_cons_110 = st.sidebar.number_input('Tokyo Bonus %: Consulting 110-120 %', value = 8.3)
tokyo_cons_120 = st.sidebar.number_input('Tokyo Bonus %: Consulting 120-140 %', value = 8.7)
tokyo_cons_140 = st.sidebar.number_input('Tokyo Bonus %: Consulting > 140 %', value = 9.0)

lahore_cons_70 = st.sidebar.number_input('Lahore Bonus %: Consulting 70-80 %', value = 1.0)
lahore_cons_80 = st.sidebar.number_input('Tokyo Bonus %: Consulting 80-90 %', value = 1.5)
lahore_cons_90 = st.sidebar.number_input('Tokyo Bonus %: Consulting 90-100 %', value = 2.0)
lahore_cons_100 = st.sidebar.number_input('Tokyo Bonus %: Consulting 100-110 %', value = 2.3)
lahore_cons_110 = st.sidebar.number_input('Tokyo Bonus %: Consulting 110-120 %', value = 2.5)
lahore_cons_120 = st.sidebar.number_input('Tokyo Bonus %: Consulting 120-140 %', value = 2.7)
lahore_cons_140 = st.sidebar.number_input('Tokyo Bonus %: Consulting > 140 %', value = 3.0)

##### Life Sciences
berlin_ls_70 = st.sidebar.number_input('Berlin Bonus %: LS 70-80 %', value = 1.0)
berlin_ls_80 = st.sidebar.number_input('Berlin Bonus %: LS 80-90 %', value = 3.0)
berlin_ls_90 = st.sidebar.number_input('Berlin Bonus %: LS 90-100 %', value = 5.0)
berlin_ls_100 = st.sidebar.number_input('Berlin Bonus %: LS 100-110 %', value = 7.0)
berlin_ls_110 = st.sidebar.number_input('Berlin Bonus %: LS 110-120 %', value = 7.3)
berlin_ls_120 = st.sidebar.number_input('Berlin Bonus %: LS 120-140 %', value = 7.7)
berlin_ls_140 = st.sidebar.number_input('Berlin Bonus %: LS > 140 %', value = 8.0)

london_ls_70 = st.sidebar.number_input('London Bonus %: LS 70-80 %', value = 1.0)
london_ls_80 = st.sidebar.number_input('London Bonus %: LS 80-90 %', value = 3.0)
london_ls_90 = st.sidebar.number_input('London Bonus %: LS 90-100 %', value = 5.0)
london_ls_100 = st.sidebar.number_input('London Bonus %: LS 100-110 %', value = 7.0)
london_ls_110 = st.sidebar.number_input('London Bonus %: LS 110-120 %', value = 7.3)
london_ls_120 = st.sidebar.number_input('London Bonus %: LS 120-140 %', value = 7.7)
london_ls_140 = st.sidebar.number_input('London Bonus %: LS > 140 %', value = 8.0)

munich_ls_70 = st.sidebar.number_input('Munich Bonus %: LS 70-80 %', value = 1.0)
munich_ls_80 = st.sidebar.number_input('Munich Bonus %: LS 80-90 %', value = 3.0)
munich_ls_90 = st.sidebar.number_input('Munich Bonus %: LS 90-100 %', value = 5.0)
munich_ls_100 = st.sidebar.number_input('Munich Bonus %: LS 100-110 %', value = 7.0)
munich_ls_110 = st.sidebar.number_input('Munich Bonus %: LS 110-120 %', value = 7.3)
munich_ls_120 = st.sidebar.number_input('Munich Bonus %: LS 120-140 %', value = 7.7)
munich_ls_140 = st.sidebar.number_input('Munich Bonus %: LS > 140 %', value = 8.0)

newyork_ls_70 = st.sidebar.number_input('New York Bonus %: LS 70-80 %', value = 1.0)
newyork_ls_80 = st.sidebar.number_input('New York Bonus %: LS 80-90 %', value = 3.0)
newyork_ls_90 = st.sidebar.number_input('New York Bonus %: LS 90-100 %', value = 5.0)
newyork_ls_100 = st.sidebar.number_input('New York Bonus %: LS 100-110 %', value = 7.0)
newyork_ls_110 = st.sidebar.number_input('New York Bonus %: LS 110-120 %', value = 7.3)
newyork_ls_120 = st.sidebar.number_input('New York Bonus %: LS 120-140 %', value = 7.7)
newyork_ls_140 = st.sidebar.number_input('New York Bonus %: LS > 140 %', value = 8.0)

sf_ls_70 = st.sidebar.number_input('San Francisco Bonus %: LS 70-80 %', value = 1.0)
sf_ls_80 = st.sidebar.number_input('San Francisco Bonus %: LS 80-90 %', value = 3.0)
sf_ls_90 = st.sidebar.number_input('San Francisco Bonus %: LS 90-100 %', value = 5.0)
sf_ls_100 = st.sidebar.number_input('San Francisco Bonus %: LS 100-110 %', value = 7.0)
sf_ls_110 = st.sidebar.number_input('San Francisco Bonus %: LS 110-120 %', value = 7.3)
sf_ls_120 = st.sidebar.number_input('San Francisco Bonus %: LS 120-140 %', value = 7.7)
sf_ls_140 = st.sidebar.number_input('San Francisco Bonus %: LS > 140 %', value = 8.0)

santiago_ls_70 = st.sidebar.number_input('Santiago Bonus %: LS 70-80 %', value = 1.0)
santiago_ls_80 = st.sidebar.number_input('Santiago Bonus %: LS 80-90 %', value = 3.0)
santiago_ls_90 = st.sidebar.number_input('Santiago Bonus %: LS 90-100 %', value = 5.0)
santiago_ls_100 = st.sidebar.number_input('Santiago Bonus %: LS 100-110 %', value = 7.0)
santiago_ls_110 = st.sidebar.number_input('Santiago Bonus %: LS 110-120 %', value = 7.3)
santiago_ls_120 = st.sidebar.number_input('Santiago Bonus %: LS 120-140 %', value = 7.7)
santiago_ls_140 = st.sidebar.number_input('Santiago Bonus %: LS > 140 %', value = 8.0)

seoul_ls_70 = st.sidebar.number_input('Seoul Bonus %: LS 70-80 %', value = 1.5)
seoul_ls_80 = st.sidebar.number_input('Seoul Bonus %: LS 80-90 %', value = 3.0)
seoul_ls_90 = st.sidebar.number_input('Seoul Bonus %: LS 90-100 %', value = 5.0)
seoul_ls_100 = st.sidebar.number_input('Seoul Bonus %: LS 100-110 %', value = 7.0)
seoul_ls_110 = st.sidebar.number_input('Seoul Bonus %: LS 110-120 %', value = 7.3)
seoul_ls_120 = st.sidebar.number_input('Seoul Bonus %: LS 120-140 %', value = 7.7)
seoul_ls_140 = st.sidebar.number_input('Seoul Bonus %: LS > 140 %', value = 8.0)

shanghai_ls_70 = st.sidebar.number_input('Shanghai Bonus %: LS 70-80 %', value = 1.5)
shanghai_ls_80 = st.sidebar.number_input('Shanghai Bonus %: LS 80-90 %', value = 3.0)
shanghai_ls_90 = st.sidebar.number_input('Shanghai Bonus %: LS 90-100 %', value = 5.0)
shanghai_ls_100 = st.sidebar.number_input('Shanghai Bonus %: LS 100-110 %', value = 7.0)
shanghai_ls_110 = st.sidebar.number_input('Shanghai Bonus %: LS 110-120 %', value = 7.3)
shanghai_ls_120 = st.sidebar.number_input('Shangai Bonus %: LS 120-140 %', value = 7.7)
shanghai_ls_140 = st.sidebar.number_input('Shanghai Bonus %: LS > 140 %', value = 8.0)

tokyo_ls_70 = st.sidebar.number_input('Tokyo Bonus %: LS 70-80 %', value = 1.5)
tokyo_ls_80 = st.sidebar.number_input('Tokyo Bonus %: LS 80-90 %', value = 3.0)
tokyo_ls_90 = st.sidebar.number_input('Tokyo Bonus %: LS 90-100 %', value = 5.0)
tokyo_ls_100 = st.sidebar.number_input('Tokyo Bonus %: LS 100-110 %', value = 7.0)
tokyo_ls_110 = st.sidebar.number_input('Tokyo Bonus %: LS 110-120 %', value = 7.3)
tokyo_ls_120 = st.sidebar.number_input('Tokyo Bonus %: LS 120-140 %', value = 7.7)
tokyo_ls_140 = st.sidebar.number_input('Tokyo Bonus %: LS > 140 %', value = 8.0)

lahore_ls_70 = st.sidebar.number_input('Lahore Bonus %: LS 70-80 %', value = 1.0)
lahore_ls_80 = st.sidebar.number_input('Lahore Bonus %: LS 80-90 %', value = 1.5)
lahore_ls_90 = st.sidebar.number_input('Lahore Bonus %: LS 90-100 %', value = 2.0)
lahore_ls_100 = st.sidebar.number_input('Lahore Bonus %: LS 100-110 %', value = 2.3)
lahore_ls_110 = st.sidebar.number_input('Lahore Bonus %: LS 110-120 %', value = 2.5)
lahore_ls_120 = st.sidebar.number_input('Lahore Bonus %: LS 120-140 %', value = 2.7)
lahore_ls_140 = st.sidebar.number_input('Lahore Bonus %: LS > 140 %', value = 3.0)





bonus_rates_2023 = {'verticals': {
                            'Consulting': { 'costs': {
                                           70: {'Berlin': berlin_cons_70,
                                               'London': london_cons_70,
                                               'Munich': munich_cons_70,
                                               'New York': newyork_cons_70,
                                               'San Francisco': sf_cons_70,
                                               'Santiago': santiago_cons_70,
                                               'Seoul': seoul_cons_70,
                                               'Shanghai': shanghai_cons_70,
                                               'Tokyo': tokyo_cons_70,
                                               'Lahore': lahore_cons_70},
                                           80: {
                                                'Berlin' : berlin_cons_80,
                                                'London': london_cons_80,
                                                'Munich': munich_cons_80,
                                                'New York': newyork_cons_80,
                                                'San Francisco': sf_cons_80,
                                                'Santiago': santiago_cons_80,
                                                'Seoul': seoul_cons_80,
                                                'Shanghai': shanghai_cons_80,
                                                'Tokyo': tokyo_cons_80,
                                                'Lahore': lahore_cons_80
                                               },
                                           90: {
                                                'Berlin': berlin_cons_90,
                                                'London': london_cons_90,
                                                'Munich': munich_cons_90,
                                                'New York': newyork_cons_90,
                                                'San Francisco': sf_cons_90,
                                                'Santiago': santiago_cons_90,
                                                'Seoul': seoul_cons_90,
                                                'Shanghai': shanghai_cons_90,
                                                'Tokyo': tokyo_cons_90,
                                                'Lahore': lahore_cons_90
                                                },
                                           100: {
                                                'Berlin': berlin_cons_100,
                                                'London': london_cons_100,
                                                'Munich': munich_cons_100,
                                                'New York': newyork_cons_100,
                                                'San Francisco': sf_cons_100,
                                                'Santiago': santiago_cons_100,
                                                'Seoul': seoul_cons_100,
                                                'Shanghai': shanghai_cons_100,
                                                'Tokyo': tokyo_cons_100,
                                                'Lahore': lahore_cons_100 
                                           },
                                           110: {
                                                'Berlin': berlin_cons_110,
                                                'London': london_cons_110,
                                                'Munich': munich_cons_110,
                                                'New York': newyork_cons_110,
                                                'San Francisco': sf_cons_110,
                                                'Santiago': santiago_cons_110,
                                                'Seoul': seoul_cons_110,
                                                'Shanghai': shanghai_cons_110,
                                                'Tokyo': tokyo_cons_110,
                                                'Lahore': lahore_cons_110 
                                           },
                                           120: {
                                                'Berlin': berlin_cons_120,
                                                'London': london_cons_120,
                                                'Munich': munich_cons_120,
                                                'New York': newyork_cons_120,
                                                'San Francisco': sf_cons_120,
                                                'Santiago': santiago_cons_120,
                                                'Seoul': seoul_cons_120,
                                                'Shanghai': shanghai_cons_120,
                                                'Tokyo': tokyo_cons_120,
                                                'Lahore': lahore_cons_120 
                                           },
                                           140: {
                                                'Berlin': berlin_cons_140,
                                                'London': london_cons_140,
                                                'Munich': munich_cons_140,
                                                'New York': newyork_cons_140,
                                                'San Francisco': sf_cons_140,
                                                'Santiago': santiago_cons_140,
                                                'Seoul': seoul_cons_140,
                                                'Shanghai': shanghai_cons_140,
                                                'Tokyo': tokyo_cons_140,
                                                'Lahore': lahore_cons_140
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
                                           70: {'Berlin' : berlin_ls_70,
                                                'London': london_ls_70,
                                                'Munich': munich_ls_70,
                                                'New York': newyork_ls_70,
                                                'San Francisco': sf_ls_70,
                                                'Santiago': santiago_ls_70,
                                                'Seoul': seoul_ls_70,
                                                'Shanghai': shanghai_ls_70,
                                                'Tokyo': tokyo_ls_70,
                                                'Lahore': lahore_ls_70},
                                           80: {
                                                'Berlin' : berlin_ls_80,
                                                'London': london_ls_80,
                                                'Munich': munich_ls_80,
                                                'New York': newyork_ls_80,
                                                'San Francisco': sf_ls_80,
                                                'Santiago': santiago_ls_80,
                                                'Seoul': seoul_ls_80,
                                                'Shanghai': shanghai_ls_80,
                                                'Tokyo': tokyo_ls_80,
                                                'Lahore': lahore_ls_80
                                               },
                                           90: {
                                                'Berlin': berlin_ls_90,
                                                'London': london_ls_90,
                                                'Munich': munich_ls_90,
                                                'New York': newyork_ls_90,
                                                'San Francisco': sf_ls_90,
                                                'Santiago': santiago_ls_90,
                                                'Seoul': seoul_ls_90,
                                                'Shanghai': shanghai_ls_90,
                                                'Tokyo': tokyo_ls_90,
                                                'Lahore': lahore_ls_90
                                                },
                                           100: {
                                                'Berlin': berlin_ls_100,
                                                'London': london_ls_100,
                                                'Munich': munich_ls_100,
                                                'New York': newyork_ls_100,
                                                'San Francisco': sf_ls_100,
                                                'Santiago': santiago_ls_100,
                                                'Seoul': seoul_ls_100,
                                                'Shanghai': shanghai_ls_100,
                                                'Tokyo': tokyo_ls_100,
                                                'Lahore': lahore_ls_100 
                                           },
                                           110: {
                                                'Berlin': berlin_ls_110,
                                                'London': london_ls_110,                                                
                                                'Munich': munich_ls_110,
                                                'New York': newyork_ls_110,
                                                'San Francisco': sf_ls_110,
                                                'Santiago': santiago_ls_110,
                                                'Seoul': seoul_ls_110,
                                                'Shanghai': shanghai_ls_110,
                                                'Tokyo': tokyo_ls_110,
                                                'Lahore': lahore_ls_110 
                                           },
                                           120: {
                                                'Berlin': berlin_ls_120,
                                                'London': london_ls_120,
                                                'Munich': munich_ls_120,
                                                'New York': newyork_ls_120,
                                                'San Francisco': sf_ls_120,
                                                'Santiago': santiago_ls_120,
                                                'Seoul': seoul_ls_120,
                                                'Shanghai': shanghai_ls_120,
                                                'Tokyo': tokyo_ls_120,
                                                'Lahore': lahore_ls_120 
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
               'As_consulting_2022' : consulting_ass_2022,
               'n_consulting_2022': n_consulting_2022,
               'As_consulting_2023' : consulting_ass_2023,
               'n_consulting_2023': n_consulting_2023,
               'As_LS_2022' : ls_ass_2022,
               'n_LS_2022': n_ls_2022,
               'As_LS_2023' : ls_ass_2023,
               'n_LS_2023': n_ls_2023,
               'As_total_2022': total_ass_2022,
               'n_total_2022': n_total_2022,
               'As_total_2023': total_ass_2023,
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

as_consulting_2022_avg = df['As_consulting_2022'].mean()
as_consulting_2023_avg = df['As_consulting_2023'].mean()
as_ls_2022_avg = df['As_LS_2022'].mean()
as_ls_2023_avg = df['As_LS_2023'].mean()
as_total_2022_avg = df['As_total_2022'].mean()
as_total_2023_avg = df['As_total_2023'].mean()

average_costs = {
     'As_consulting_2022': as_consulting_2022_avg,
     'As_consulting_2023': as_consulting_2023_avg,
     'As_LS_2022': as_ls_2022_avg,
     'As_LS_2023': as_ls_2023_avg,
     'As_total_2022': as_total_2022_avg,
     'As_LS_2023': as_total_2023_avg
     }

print (average_costs)

df_average_costs = pd.DataFrame([average_costs])

st.title('Bonus Average Costs Analysis', anchor=None)
st.dataframe(df_average_costs)



df['As_consulting_diff'] = df['As_consulting_2023'] - df['As_consulting_2022']
df['As_LS_diff'] = df['As_LS_2023'] - df['As_LS_2022']
df['As_total_diff'] = df['As_total_2023'] - df['As_total_2022']

st.title('Cost Difference Analysis', anchor=None)
st.dataframe (df[['reference_date', 'As_consulting_diff', 'As_LS_diff', 'As_total_diff']])



#with pd.ExcelWriter('summary_stats.xlsx') as writer:

#df.to_excel(writer, sheet_name = 'statistics') 



#df[['reference_date', 'Ass_consulting_diff', 'Ass_LS_diff', 'Ass_total_diff']].to_excel(writer, sheet_name = 'cost_differences')
#df_margin.to_excel(writer, sheet_name = 'margin_analysis')





  


     
            
          
          
        



















