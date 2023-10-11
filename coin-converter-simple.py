# converts coin values in arden vul RAW to values better for my campaign

import random


ag_str_number_coin = 0
as_str_number_coin = 0
ac_str_number_coin = 0
pp_str_number_coin = 0
ep_str_number_coin = 0
gp_str_number_coin = 0
sp_str_number_coin = 0
cp_str_number_coin = 0

ag_conv = 0
as_conv = 0
ac_conv = 0
pp_conv = 0
ep_conv = 0
gp_conv = 0
sp_conv = 0
cp_conv = 0

ag_pct = 0
as_pct = 0
ac_pct = 0
pp_pct = 0
ep_pct = 0
gp_pct = 0
sp_pct = 0
cp_pct = 0

print('Enter coins: ag, as, ac, pp, ep, gp, sp, cp')
user_input = input()

#user_input = "10ag, 40as, 100ac, 40pp, 500gp, 1000sp, 4000cp"

user_input_list = user_input.split(',')

for coin_type in user_input_list:
    if 'ag' in coin_type:
        ag_number_coin = coin_type.replace('ag','')
        ag_str_number_coin = int(ag_number_coin)
    elif 'as' in coin_type:
        as_number_coin = coin_type.replace('as','')
        as_str_number_coin = int(as_number_coin)
    elif 'ac' in coin_type:
        ac_number_coin = coin_type.replace('ac','')
        ac_str_number_coin = int(ac_number_coin)
    elif 'pp' in coin_type:
        pp_number_coin = coin_type.replace('pp','')
        pp_str_number_coin = int(pp_number_coin)
    elif 'ep' in coin_type:
        ep_number_coin = coin_type.replace('ep','')
        ep_str_number_coin = int(ep_number_coin)
    elif 'gp' in coin_type:
        gp_number_coin = coin_type.replace('gp','')
        gp_str_number_coin = int(gp_number_coin)
    elif 'sp' in coin_type:
        sp_number_coin = coin_type.replace('sp','')
        sp_str_number_coin = int(sp_number_coin)
    elif 'cp' in coin_type:
        cp_number_coin = coin_type.replace('cp','')
        cp_str_number_coin = int(cp_number_coin)

ag_cp_value = (ag_str_number_coin*1000)
as_cp_value = (as_str_number_coin*100)
ac_cp_value = (ac_str_number_coin*10)
pp_cp_value = (pp_str_number_coin*1000)
ep_cp_value = (ep_str_number_coin*50)
gp_cp_value = (gp_str_number_coin*100)
sp_cp_value = (sp_str_number_coin*10)

total_coins = (ag_str_number_coin + as_str_number_coin + ac_str_number_coin + pp_str_number_coin + ep_str_number_coin + gp_str_number_coin + sp_str_number_coin + cp_str_number_coin)

total_val_in_cp = (ag_cp_value + as_cp_value + ac_cp_value + pp_cp_value + ep_cp_value + gp_cp_value + sp_cp_value + cp_str_number_coin)

gp_fuzz = random.randrange(20, 40) / 100
sp_fuzz = random.randrange(20, 40) / 100
cp_fuzz = 1 - gp_fuzz - sp_fuzz

gp_pct = gp_fuzz
sp_pct = sp_fuzz
cp_pct = cp_fuzz

gp_conv = total_val_in_cp * gp_fuzz / 100
sp_conv = total_val_in_cp * sp_fuzz / 10
cp_conv = total_val_in_cp * cp_fuzz

pp_conv = round(pp_conv)
gp_conv = round(gp_conv)
ep_conv = round(ep_conv)
sp_conv = round(sp_conv)
cp_conv = round(cp_conv)

pp_conv = str(pp_conv)
gp_conv = str(gp_conv)
ep_conv = str(ep_conv)
sp_conv = str(sp_conv)
cp_conv = str(cp_conv)

print(gp_conv + "gp, " + sp_conv + "sp, " + cp_conv + "cp")