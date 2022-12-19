with cte1 as (
    select 
        npi,
        cpt,
        avg(paid_amount) as avg_cost 
        
)
select 
    *,
    npi,
    cte1.avg_cost
    from referral_providers

    join cte1
    on cte1.npi = referral_providers.npi
    and cte1.procedure = referral_providers.cpt 
    