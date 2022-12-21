import json
import sqlalchemy
from sqlalchemy import create_engine

def return_query():
 query = """
drop table if exists public.bonus_tracker;
create table public.bonus_tracker as 
select
    dtsd.team_structure_date ref_date,
    dtsd.employee_id,
    dtsd.bamboo_id,
    dtsd.bamboo_employee_number,
    dtsd.employee_name,
    dtsd.employee_position_id,
    dtsd.employee_position,
    dtsd.is_new_hire,
    dtsd.hire_date,
    dtsd.months_employed,
    dwdd.working_days,
    dtsd.cost_center,
    dtsd.employee_atheneum_office_id,
    dtsd.employee_atheneum_office,
    dtsd.employee_atheneum_office_code,
    dtsd.team_id,
    dtsd.team_name,
    tv.vertical Team_Vertical,
    dtsd.job_title,
    dtsd.team_leader_id,
    dtsd.team_leader_name,
    dtsd.account_manager_id,
    dtsd.account_manager_name,    
    dtsd.principal_id,
    dtsd.principal_name,
    coalesce(fe.Deliveries, 0) Deliveries,
    coalesce(fe.CR_Deliveries, 0) CR_Deliveries,
    coalesce(fe.Interviews, 0) Interviews,
    coalesce(fe.CR_Interviews, 0) CR_Interviews,
    coalesce(fr.Revenue, 0) Revenue,
    coalesce(fr.deductible_costs, 0) deductible_costs,
    coalesce(fr.Margin, 0) margin,
    dtsd.target_margin,
    dtsd.senior_account_manager_id,
    dtsd.senior_account_manager_name,
    dtsd.senior_principal_id,
    dtsd.senior_principal_name,
    dtsd.monthly_revenue_target,
    dtsd.quarterly_revenue_target,
    current_date last_uploaded_at  
from
(select id, team_structure_date, employee_id, bamboo_id, job_title, bamboo_employee_number, employee_name, employee_position_id, employee_position, cost_center, employee_atheneum_office_id, employee_atheneum_office, employee_atheneum_office_code,
team_id, team_name, target_margin, team_leader_id, team_leader_name, account_manager_id, account_manager_name, senior_account_manager_id, senior_account_manager_name, principal_id, principal_name, 
senior_principal_id, senior_principal_name, is_new_hire, hire_date, months_employed, monthly_revenue_target, quarterly_revenue_target
from public.dim_team_structures_monthly dtsd
where team_structure_date>='2022-01-01' and employee_position_id in (1, 2, 5, 15)) dtsd
left join (
select date_trunc('month', event_occurred_date) event_occurred_date, employee_id, sum(case when epl_status_id=5 then 1 else 0 end) Deliveries, sum(case when epl_status_id=5 then is_cr else 0 end) CR_Deliveries,
sum(case when epl_status_id=10 then 1 else 0 end) Interviews, sum(case when epl_status_id=10 then is_cr else 0 end) CR_Interviews
from public.fact_events fe where event_occurred_date>='2022-01-01' group by 1, 2) fe
on dtsd.team_structure_date=fe.event_occurred_date and dtsd.employee_id=fe.employee_id 
left join(select date_trunc('month', delivery_date) delivery_date, employee_id, 
sum(eur_rev) Revenue, sum(case when (cost_type_id in (1, 9, 10, 11, 3, 2, 22, 21, 13, 20, 23)) then eur_cost else 0 end) deductible_costs, sum(eur_cost) total_costs, (revenue - deductible_costs) as margin
from public.fact_revenues where delivery_date>='2022-01-01' group by 1, 2) fr 
on dtsd.team_structure_date=fr.delivery_date and dtsd.employee_id=fr.employee_id
left join offline_data.team_verticals tv on dtsd.team_id=tv.team_id
left join (select date_trunc('month', date) date, atheneum_office_id, sum(working_days) working_days from dim_working_days_daily dwdd where date >='2022-01-01' and date <= current_date group by 1, 2) dwdd
on dtsd.team_structure_date = dwdd.date and dtsd.employee_atheneum_office_id = dwdd.atheneum_office_id
order by 4, 1 asc
"""
 return query