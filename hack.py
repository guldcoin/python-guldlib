from guldlib import *

individuals = [
    "cz",
    "mozilla1",
    "eylon",
    "fdreyfus",
    "cynopterus",
    "ying",
    "iramiller",
    "juankong",
    "ingridjased",
    "veronica",
    "rukie",
    "cmejia",
    "imiller",
    "ira",
    "mizim",
    "isysd",
    "et4te",
    "goldchamp",
    "rsfogel",
    "srcreativo",
    "jamesbong",
    "monta",
    "waynesthompson",
    "okojumo",
    "cryptobit",
    "lewi",
    "jvkatzman",
    "vonsteuben",
    "garrett-keirns",
    "raadyx",
    "derekshalom"
]

groups = {
    "drprx": 10,
    "zimmi": 20,
    "hodlmybeer": 250,
    "spartan": 10000,
    "300e": 20,
    "mizim": 500,
    "betatown": 10000,
    "panafintech": 100,
    "tigoctm": 20
}

for ind in individuals:
    dt, tstamp = get_time_date_stamp()
    fname = '%s.dat' % tstamp
    tx = gen_redeem_registration_fee(ind, 'individual', 1, dt, tstamp)
    with open(os.path.join(GULD_HOME, 'ledger', 'GULD', ind, fname), 'w') as f:
        f.write(tx)

for grp in groups:
    dt, tstamp = get_time_date_stamp()
    fname = '%s.dat' % tstamp
    tx = gen_redeem_registration_fee(grp, 'group', groups[grp], dt, tstamp)
    with open(os.path.join(GULD_HOME, 'ledger', 'GULD', grp, fname), 'w') as f:
        f.write(tx)
