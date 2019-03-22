import pandas as pd

data = pd.read_csv('CRDC2013_14.csv')

data['total_enrollment'] = data.TOT_ENR_M + data.TOT_ENR_F

all_enrollment = data.total_enrollment.sum()

cols = [  'SCH_ENR_HI_M',
            'SCH_ENR_HI_F',
            'SCH_ENR_AM_M',
            'SCH_ENR_AM_F',
            'SCH_ENR_AS_M',
            'SCH_ENR_AS_F',
            'SCH_ENR_HP_M',
            'SCH_ENR_HP_F',
            'SCH_ENR_BL_M',
            'SCH_ENR_BL_F',
            'SCH_ENR_WH_M',
            'SCH_ENR_WH_F',
            'SCH_ENR_TR_M',
            'SCH_ENR_TR_F'  ]

rg = pd.concat(
    [ pd.DataFrame([[c, data[c].sum(), round(data[c].sum()*100.0/all_enrollment,1)]],
    columns=['Field','Sum','Percent']
    ) for c in cols ], ignore_index=True
)

r = pd.DataFrame(columns=['Field','Sum','Percent'])
g = pd.DataFrame(columns=['Field','Sum','Percent'])
for c in cols:
    # Race
    if len(r.loc[r['Field']==c[:-2]]):
        r.loc[r['Field']==c[:-2], 'Sum'] += data[c].sum()
        r.loc[r['Field']==c[:-2], 'Percent'] = r.loc[r['Field']==c[:-2]]['Sum']/all_enrollment
    else:
        r = r.append({'Field':c[:-2],
                'Sum':data[c].sum(),
                'Percent':data[c].sum()/all_enrollment}, ignore_index=True)
    # Gender
    if len(g.loc[g['Field']==c[-1:]]):
        g.loc[g['Field']==c[-1:], 'Sum'] += data[c].sum()
        g.loc[g['Field']==c[-1:], 'Percent'] = g.loc[g['Field']==c[-1:]]['Sum']/all_enrollment
    else:
        g = g.append({'Field':c[-1:],
                'Sum':data[c].sum(),
                'Percent':data[c].sum()/all_enrollment}, ignore_index=True)
# r['Percent'] = round(r['Percent']*100,1)

 
print(rg)
print(r)
print(g)
