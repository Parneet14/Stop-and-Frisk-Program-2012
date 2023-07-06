# Stop-and-Frisk-Program-2012Report 1: Data and Visualization Business Understanding:
What is the purpose of the SQF program?
SQF program is designed to reduce shooting and saving lives.

How would you define and measure the effectiveness of such a program? 
Stops and frisks are two separate acts that involve two different levels of required legal justification. To stop a person, a police officer must have reasonable suspicion the person has committed, is committing, or is about to commit an unlawful act. To frisk a person, however, the officer must have reason to believe the person stopped has a weapon that poses a threat to the officer’s safety, a higher and more specific standard. Data from 2012 stops indicate that NYPD officers are routinely frisking people without suspicion that the person has a weapon

What data would you need be able to judge its effectiveness?
NYPD Stop Question Frisk Database 2012
NYPD Stop Question Frisk Codebook 2012


Data Understanding:
Describe the meaning and type of data (e.g., scale, values) for each attribute in the data file.
Table 1 shows the different attributes collected, meaning and value range of those attributes throughout the SQF program of 2012
Variable	Label	Scale
year	YEAR OF STOP (CCYY)	2Th
pct	PRECINCT OF STOP (district of city as defined for police purpose)	1-123
ser_num	UF250 SERIAL NUMBER	1-11969
datestop	DATE OF STOP (MM-DD-YYYY)	Jan1-Dec31
timestop	TIME OF STOP (HH:MM)	00:00-23:59
recstat	RECORD STATUS	1-A
inout	WAS STOP INSIDE OR OUTSIDE ?	IN-OUT
trhsloc	WAS LOCATION HOUSING OR TRANSIT AUTHORITY ?	P(Niether),H(Housing),
T (Transit)
perobs	PERIOD OF OBSERVATION (MMM)	0-955
crimsusp	CRIME SUSPECTED	values like robbery,
felony,CRIM TRESP,
and so on,blank 
perstop	PERIOD OF STOP (MMM)	0-99, **
typeofid	STOPPED PERSON'S IDENTIFICATION TYPE	O(OTHER),P(PHOTO),
R(REFUSED),V(VERBAL)
explnstp	DID OFFICER EXPLAIN REASON FOR STOP ?	yes,no
othpers	WERE OTHER PERSONS STOPPED, QUESTIONED OR FRISKED ?	yes,no
arstmade	WAS AN ARREST MADE ?	yes,no
arstoffn	OFFENSE SUSPECT ARRESTED FOR	
sumissue	WAS A SUMMONS ISSUED ?	yes,no
sumoffen	OFFENSE SUSPECT WAS SUMMONSED FOR	0 to 99-999,AC160118(1)
To AC24-236,admin code to 
Y-010118A,blanks
compyear	COMPLAINT YEAR (IF COMPLAINT REPORT PREPARED)	0
comppct	COMPLAINT PRECINCT (IF COMPLAINT REPORT PREPARED)	0
offunif	WAS OFFICER IN UNIFORM ?	yes,no
officrid	ID CARD PROVIDED BY OFFICER (IF NOT IN UNIFORM)	Not listed,No,ID
frisked	WAS SUSPECT FRISKED ?	yes,no
searched	WAS SUSPECT SEARCHED ?	yes,no
contrabn	WAS CONTRABAND FOUND ON SUSPECT ?	yes,no
adtlrept	WERE ADDITIONAL REPORTS PREPARED ?	no
pistol	WAS A PISTOL FOUND ON SUSPECT ?	yes,no
riflshot	WAS A RIFLE FOUND ON SUSPECT ?	yes,no
asltweap	WAS AN ASSAULT WEAPON FOUND ON SUSPECT ?	yes,no
knifcuti	WAS A KNIFE OR CUTTING INSTRUMENT FOUND ON SUSPECT ?	YES,NO
machgun	WAS A MACHINE GUN FOUND ON SUSPECT ?	YES,NO
othrweap	WAS ANOTHER TYPE OF WEAPON FOUND ON SUSPECT	YES,NO
pf_hands	PHYSICAL FORCE USED BY OFFICER - HANDS	YES,NO
pf_wall	PHYSICAL FORCE USED BY OFFICER - SUSPECT AGAINST WALL	YES,NO
pf_grnd	PHYSICAL FORCE USED BY OFFICER - SUSPECT ON GROUND	YES,NO
pf_drwep	PHYSICAL FORCE USED BY OFFICER - WEAPON DRAWN	YES,NO
pf_ptwep	PHYSICAL FORCE USED BY OFFICER - WEAPON POINTED	YES,NO
pf_baton	PHYSICAL FORCE USED BY OFFICER - BATON	YES,NO
pf_hcuff	PHYSICAL FORCE USED BY OFFICER - HANDCUFFS	YES,NO
pf_pepsp	PHYSICAL FORCE USED BY OFFICER - PEPPER SPRAY	YES,NO
pf_other	PHYSICAL FORCE USED BY OFFICER - OTHER	YES,NO
radio	RADIO RUN	YES,NO
ac_rept	ADDITIONAL CIRCUMSTANCES - REPORT BY VICTIM/WITNESS/OFFICER	YES,NO
ac_inves	ADDITIONAL CIRCUMSTANCES - ONGOING INVESTIGATION	YES,NO
rf_vcrim	REASON FOR FRISK - VIOLENT CRIME SUSPECTED	YES,NO
rf_othsw	REASON FOR FRISK - OTHER SUSPICION OF WEAPONS	YES,NO
ac_proxm	ADDITIONAL CIRCUMSTANCES - PROXIMITY TO SCENE OF OFFENSE	YES,NO
rf_attir	REASON FOR FRISK - INAPPROPRIATE ATTIRE FOR SEASON	YES,NO
cs_objcs	REASON FOR STOP - CARRYING SUSPICIOUS OBJECT	YES,NO
cs_descr	REASON FOR STOP - FITS A RELEVANT DESCRIPTION	YES,NO
cs_casng	REASON FOR STOP - CASING A VICTIM OR LOCATION	YES,NO
cs_lkout	REASON FOR STOP - SUSPECT ACTING AS A LOOKOUT	YES,NO
rf_vcact	REASON FOR FRISK-  ACTIONS OF ENGAGING IN A VIOLENT CRIME	YES,NO
cs_cloth	REASON FOR STOP - WEARING CLOTHES COMMONLY USED IN A CRIME	YES,NO
cs_drgtr	REASON FOR STOP - ACTIONS INDICATIVE OF A DRUG TRANSACTION	YES,NO
ac_evasv	ADDITIONAL CIRCUMSTANCES - EVASIVE RESPONSE TO QUESTIONING	YES,NO
ac_assoc	ADDITIONAL CIRCUMSTANCES - ASSOCIATING WITH KNOWN CRIMINALS	YES,NO
cs_furtv	REASON FOR STOP - FURTIVE MOVEMENTS	YES,NO
rf_rfcmp	REASON FOR FRISK - REFUSE TO COMPLY W OFFICER'S DIRECTIONS	YES,NO
ac_cgdir	ADDITIONAL CIRCUMSTANCES - CHANGE DIRECTION AT SIGHT OF OFFICER	YES,NO
rf_verbl	REASON FOR FRISK - VERBAL THREATS BY SUSPECT	YES,NO
cs_vcrim	REASON FOR STOP - ACTIONS OF ENGAGING IN A VIOLENT CRIME	YES,NO
cs_bulge	REASON FOR STOP - SUSPICIOUS BULGE	YES,NO
cs_other	REASON FOR STOP – OTHER	YES,NO
ac_incid	ADDITIONAL CIRCUMSTANCES - AREA HAS HIGH CRIME INCIDENCE	YES,NO
ac_time	ADDITIONAL CIRCUMSTANCES - TIME OF DAY FITS CRIME INCIDENCE	YES,NO
rf_knowl	REASON FOR FRISK - KNOWLEDGE OF SUSPECT'S PRIOR CRIM BEHAV	YES,NO
ac_stsnd	ADDITIONAL CIRCUMSTANCES - SIGHTS OR SOUNDS OF CRIMINAL ACTIVITY	YES,NO
ac_other	ADDITIONAL CIRCUMSTANCES – OTHER	YES,NO
sb_hdobj	BASIS OF SEARCH - HARD OBJECT	YES,NO
sb_outln	BASIS OF SEARCH - OUTLINE OF WEAPON	YES,NO
sb_admis	BASIS OF SEARCH - ADMISSION BY SUSPECT	YES,NO
sb_other	BASIS OF SEARCH – OTHER	YES,NO
repcmd	REPORTING OFFICER'S COMMAND (1 TO 999)	1-985,blank
revcmd	REVIEWING OFFICER'S COMMAND (1 TO 999)	1-879
rf_furt	REASON FOR FRISK - FURTIVE MOVEMENTS	yes,no
rf_bulg	REASON FOR FRISK - SUSPICIOUS BULGE	yes,no
offverb	VERBAL STATEMENT PROVIDED BY OFFICER (IF NOT IN UNIFORM)	V,blank
offshld	SHIELD PROVIDED BY OFFICER (IF NOT IN UNIFORM)	S,blank
forceuse	REASON FORCE USED	DO(Defense of other)
,OT(other),
DS(defence of shelf),
OR(Overcome resistance),
SF(Suspected Flight),
SW(suspected weapon),blanks
sex	SUSPECT'S SEX	Male,Female,Unknown
race	SUSPECT'S RACE	blank,asian/Pacific islander,
american indian/alaskan 
native,Black-hispanic,
white-hispanic,white,
unknown,other
dob	SUSPECT'S DATE OF BIRTH (CCYY-MM-DD)	10/01/1953-31/12/1996
age	SUSPECT'S AGE	0-999
ht_feet	SUSPECT'S HEIGHT (FEET)	3 to7
ht_inch	SUSPECT'S HEIGHT (INCHES)	0-11
weight	SUSPECT'S WEIGHT	0-99
haircolr	SUSPECT'S HAIRCOLOR	blank,bald,blond,black,
brown,dyed,frosted,gray,red,
sandy,salt&pepper,white,
unknow,other
eyecolor	SUSPECT'S EYE COLOR	blank,black,blue,brown,
twodifferent,green,gray,
hazel,maroon,pink,violet,
unknown,other
build	SUSPECT'S BUILD	blankl.heavy,medium,
thin,muscular,unknown
othfeatr	SUSPECT'S OTHER FEATURES (SCARS, TATOOS ETC.)	0-8,blank
addrtyp	LOCATION OF STOP ADDRESS TYPE	R 
rescode	LOCATION OF STOP RESIDENT CODE	blank
premtype	LOCATION OF STOP PREMISE TYPE	blank
premname	LOCATION OF STOP PREMISE NAME	values from1-9634,addresses 
of different location such as
streets and ymca food court
addrnum	LOCATION OF STOP ADDRESS NUMBER	values from 0 to 99-999,
F/O1-F/O31,one,,OP19,blanks
stname	LOCATION OF STOP STREET NAME	contains name of different
streets such as 1Avenue,
blanks
stinter	LOCATION OF STOP INTERSECTION	contains name of different
intersection points,blanks
crossst	LOCATION OF STOP CROSS STREET	contains name of different
cross streets and blanks
aptnum	LOCATION OF STOP APT NUMBER	blank
city	LOCATION OF STOP CITY	Bronx,brooklyn,Staten In,
Queens,Mahattan
state	LOCATION OF STOP STATE	blank
zip	LOCATION OF STOP ZIP CODE	blank
addrpct	LOCATION OF STOP ADDRESS PRECINCT	1-123,blank
sector	LOCATION OF STOP SECTOR	5,A-U,blank
beat	LOCATION OF STOP BEAT	1-9,*,blank
post	LOCATION OF STOP POST	1-99,blank
xcoord	LOCATION OF STOP X COORD	916682-1064490,blank
ycoord	LOCATION OF STOP Y COORD	122441-269551,blank
dettypCM	DETAILS TYPES CODE	C      M-Blank
lineCM	COUNT >1 ADDITIONAL DETAILS	0-1,blank
detailCM	CRIME CODE DESCRIPTION	1-113,blank

Verify data quality. Are there missing values? Duplicate data? Outliers? Are those mistakes? How do you deal with these problems? 
1.	There are number of missing values and even empty columns present in the data some of the columns are present that we don’t even need in the analysis.
2.	Verify that all the number columns (perobs, perstop, age, weight, ht_feet, ht_inch, datestop, timestop, xcoord, ycoord) have numeric values and if a numeric value can’t be converted into number make it NaN
3.	Drop off all the invalid value in the dataframe.
4.	Converting datestop into format of 8 digits (DDMMYYYY) and timestop into 4 digits (HHMM) then creating datetime column in the dataframe
5.	By combining ht_feet and ht_inch into one column called height(inch)
6.	By using xcoord and Y coord created columns of longitude and latitude
7.	Read the 2012 spec file and Replace values in the dataframe with the matching values for better understanding
8.	Removing invalid values from age i.e., greater than 100 and less than 10 and weight i.e., greater than 350 and less than 50
9.	Dropping of columns that are not used for analysis like datestop, timestop, ht_feet, ht_inch, xcoord, ycoord, year, recstat, crimusp, dob, ser_num, dob, ser_num, arstoffn, sumoffen, comyear, compct, othfeatr, adtlrept, dettypcm, linecm, repcmd, addrtype, rescode, premtype, premname, addrnum, stname, strinter, crosstr, aptnum, state, zip, addrpct, sector, beat, post.

Give simple, appropriate statistics (e.g., range, mode, mean, median, variance, counts) for the most important attributes in these files, and then describe what they mean or whether you found something interesting. 
1.	Average age of people who are stopped during SQF is 28year 
2.	423168 more males were stopped
3.	Average height of people being stopped is 174.25
4.	51% of stopping is based on furtive movement.
5.	Only 633 pistols are recovered during the SQF
6.	Average time for inquiry is 5mins
Explore relationships between attributes. Look at the attributes and then scatter plots, correlation, cross-tabulation, group-wise averages, etc., as appropriate. 
Police officers in Brooklyn are more active to stop people and inquiry. This city seems more residents of the Black community because more than 50% people of black race are inquired and Brooklyn police paid more attention on males than females. Queens police officers inquired more of white Hispanic as of quarter of people in total are stopped. From all of three the graphs below it seems like in all the city Black male and female are stopped more than any other race. American Indian and Asian female are not stopped at all.

Compare the reasons for an SQF and what type of force was used by the officer. 
On being searched and frisked in most of the cases hands are used as a physical force by officers to control the person followed by handcuffs of person is not cooperating at all then the hard forces like pushing towards the ground or against the wall is used.
Report 2: Association Rule Mining
Data Preparation 
Construct the required transaction data set for frequent itemset and association rule mining. 
1.	Data that is cleaned in Report 1 is saved to pickle file and is used for association analysis
2.	Further following changes are made 
3.	Manual one hot encoding is done for three of the columns i.e., race, city, detailcm to get the unique values in them.
4.	Sex column is converted to Boolean and only Male will be used for association Rule 
5.	Created a reason column from all the cs_ columns to see the reason of stop.
6.	For association rules Mining only unique values from detailcm, race and city, Male and Reason column is used.

Modelling 
Create frequent itemsets and association rules. 
Use tables and visualizations to help explain your results.
Frequent itemsets are created using the minimum support value of 10% is used to analysis, it shows that only two races (54% Black,25% of White-Hispanic) fall in this category, for Cities (Bronx, Manthan, Queens, Brooklyn) with Brooklyn has highest percentage of 34. The detail crimes is Robbery, CPW and burglary.92 percent of males are stopped and searched for a reason.
Table 2 shows the Feature itemsets and the support value associated with male of race Black, White Hispanic associated with crimes of Robbery, CPW, Burglary in different cities as Bronx, Manhattan, Brooklyn Queens and stopped for a reason by police offciers.


Serial NO	support	Itemsets
0	0.53587	frozenset({'race_BLACK'})
1	0.246366	frozenset({'race_WHITE-HISPANIC'})
2	0.192846	frozenset({'city_BRONX'})
3	0.21967	frozenset({'detailcm_ROBBERY'})
4	0.244367	frozenset({'detailcm_CPW'})
5	0.113689	frozenset({'detailcm_BURGLARY'})
6	0.208693	frozenset({'city_MANHATTAN'})
7	0.349685	frozenset({'city_BROOKLYN'})
8	0.209752	frozenset({'city_QUEENS'})
9	0.91614	frozenset({'Male'})
10	0.923424	frozenset({'Reason'})
11	0.121899	frozenset({'race_BLACK', 'detailcm_ROBBERY'})
12	0.151522	frozenset({'detailcm_CPW', 'race_BLACK'})
13	0.109531	frozenset({'city_MANHATTAN', 'race_BLACK'})
14	0.225829	frozenset({'city_BROOKLYN', 'race_BLACK'})
15	0.496336	frozenset({'race_BLACK', 'Male'})
16	0.495796	frozenset({'Reason', 'race_BLACK'})
17	0.22799	frozenset({'Male', 'race_WHITE-HISPANIC'})
18	0.22832	frozenset({'Reason', 'race_WHITE-HISPANIC'})
19	0.175693	frozenset({'city_BRONX', 'Male'})
20	0.176843	frozenset({'city_BRONX', 'Reason'})
21	0.207029	frozenset({'Male', 'detailcm_ROBBERY'})
22	0.202599	frozenset({'Reason', 'detailcm_ROBBERY'})
23	0.232466	frozenset({'detailcm_CPW', 'Male'})
24	0.229473	frozenset({'detailcm_CPW', 'Reason'})
25	0.104477	frozenset({'detailcm_BURGLARY', 'Male'})
26	0.106918	frozenset({'Reason', 'detailcm_BURGLARY'})
27	0.188106	frozenset({'city_MANHATTAN', 'Male'})
28	0.190363	frozenset({'city_MANHATTAN', 'Reason'})
29	0.320139	frozenset({'city_BROOKLYN', 'Male'})
30	0.325696	frozenset({'city_BROOKLYN', 'Reason'})
31	0.19742	frozenset({'Male', 'city_QUEENS'})
32	0.194689	frozenset({'Reason', 'city_QUEENS'})
33	0.848168	frozenset({'Reason', 'Male'})
34	0.115842	frozenset({'race_BLACK', 'Male', 'detailcm_ROBBERY'})
35	0.111734	frozenset({'Reason', 'race_BLACK', 'detailcm_ROBBERY'})
36	0.145867	frozenset({'detailcm_CPW', 'race_BLACK', 'Male'})
37	0.142698	frozenset({'detailcm_CPW', 'Reason', 'race_BLACK'})
38	0.100335	frozenset({'city_MANHATTAN', 'race_BLACK', 'Male'})
39	0.100309	frozenset({'city_MANHATTAN', 'Reason', 'race_BLACK'})
40	0.208744	frozenset({'city_BROOKLYN', 'race_BLACK', 'Male'})
41	0.210796	frozenset({'city_BROOKLYN', 'Reason', 'race_BLACK'})
42	0.460366	frozenset({'Reason', 'race_BLACK', 'Male'})
43	0.211731	frozenset({'Male', 'Reason', 'race_WHITE-HISPANIC'})
44	0.16141	frozenset({'city_BRONX', 'Reason', 'Male'})
45	0.191192	frozenset({'Reason', 'Male', 'detailcm_ROBBERY'})
46	0.218632	frozenset({'detailcm_CPW', 'Reason', 'Male'})
47	0.171963	frozenset({'city_MANHATTAN', 'Reason', 'Male'})
48	0.298858	frozenset({'city_BROOKLYN', 'Reason', 'Male'})
49	0.183892	frozenset({'Male', 'Reason', 'city_QUEENS'})
50	0.106334	frozenset({'Reason', 'race_BLACK', 'Male', 'detailcm_ROBBERY'})
51	0.137524	frozenset({'detailcm_CPW', 'Reason', 'race_BLACK', 'Male'})
52	0.195269	frozenset({'city_BROOKLYN', 'Reason', 'race_BLACK', 'Male'})


The following association rules are created based on the minimum threshold of 0.8. The result of association Rule shows that if race is black and is male chances of stopping that person and inquiring is 92%.

Table 3 explains association of race male reason city with the support value, confidence, lift.
antecedents	consequents	antecedent support	consequent support	support	confidence	lift	leverage	conviction
frozenset({'race_BLACK'})	frozenset({'Male'})	0.536	0.916	0.496	0.926	1.011	0.005	1.137
frozenset({'race_BLACK'})	frozenset({'Reason'})	0.536	0.923	0.496	0.925	1.002	0.001	1.024
frozenset({'race_WHITE-HISPANIC'})	frozenset({'Male'})	0.246	0.916	0.228	0.925	1.010	0.002	1.124
frozenset({'race_WHITE-HISPANIC'})	frozenset({'Reason'})	0.246	0.923	0.228	0.927	1.004	0.001	1.045
frozenset({'city_BRONX'})	frozenset({'Male'})	0.193	0.916	0.176	0.911	0.994	-0.001	0.943
frozenset({'city_BRONX'})	frozenset({'Reason'})	0.193	0.923	0.177	0.917	0.993	-0.001	0.923
frozenset({'detailcm_ROBBERY'})	frozenset({'Male'})	0.220	0.916	0.207	0.942	1.029	0.006	1.457
frozenset({'detailcm_ROBBERY'})	frozenset({'Reason'})	0.220	0.923	0.203	0.922	0.999	0.000	0.985
frozenset({'detailcm_CPW'})	frozenset({'Male'})	0.244	0.916	0.232	0.951	1.038	0.009	1.722
frozenset({'detailcm_CPW'})	frozenset({'Reason'})	0.244	0.923	0.229	0.939	1.017	0.004	1.256
frozenset({'detailcm_BURGLARY'})	frozenset({'Male'})	0.114	0.916	0.104	0.919	1.003	0.000	1.035
frozenset({'detailcm_BURGLARY'})	frozenset({'Reason'})	0.114	0.923	0.107	0.940	1.018	0.002	1.286
frozenset({'city_MANHATTAN'})	frozenset({'Male'})	0.209	0.916	0.188	0.901	0.984	-0.003	0.850
frozenset({'city_MANHATTAN'})	frozenset({'Reason'})	0.209	0.923	0.190	0.912	0.988	-0.002	0.872
frozenset({'city_BROOKLYN'})	frozenset({'Male'})	0.350	0.916	0.320	0.916	0.999	0.000	0.992
frozenset({'city_BROOKLYN'})	frozenset({'Reason'})	0.350	0.923	0.326	0.931	1.009	0.003	1.116
frozenset({'city_QUEENS'})	frozenset({'Male'})	0.210	0.916	0.197	0.941	1.027	0.005	1.426
frozenset({'city_QUEENS'})	frozenset({'Reason'})	0.210	0.923	0.195	0.928	1.005	0.001	1.066
frozenset({'Reason'})	frozenset({'Male'})	0.923	0.916	0.848	0.919	1.003	0.002	1.029
frozenset({'Male'})	frozenset({'Reason'})	0.916	0.923	0.848	0.926	1.003	0.002	1.032
frozenset({'race_BLACK', 'detailcm_ROBBERY'})	frozenset({'Male'})	0.122	0.916	0.116	0.950	1.037	0.004	1.688
frozenset({'race_BLACK', 'detailcm_ROBBERY'})	frozenset({'Reason'})	0.122	0.923	0.112	0.917	0.993	-0.001	0.918
frozenset({'detailcm_CPW', 'race_BLACK'})	frozenset({'Male'})	0.152	0.916	0.146	0.963	1.051	0.007	2.247
frozenset({'detailcm_CPW', 'race_BLACK'})	frozenset({'Reason'})	0.152	0.923	0.143	0.942	1.020	0.003	1.315
frozenset({'city_MANHATTAN', 'race_BLACK'})	frozenset({'Male'})	0.110	0.916	0.100	0.916	1.000	0.000	0.999
frozenset({'city_MANHATTAN', 'race_BLACK'})	frozenset({'Reason'})	0.110	0.923	0.100	0.916	0.992	-0.001	0.910
frozenset({'city_BROOKLYN', 'race_BLACK'})	frozenset({'Male'})	0.226	0.916	0.209	0.924	1.009	0.002	1.109
frozenset({'city_BROOKLYN', 'race_BLACK'})	frozenset({'Reason'})	0.226	0.923	0.211	0.933	1.011	0.002	1.150
frozenset({'Reason', 'race_BLACK'})	frozenset({'Male'})	0.496	0.916	0.460	0.929	1.014	0.006	1.174
frozenset({'race_BLACK', 'Male'})	frozenset({'Reason'})	0.496	0.923	0.460	0.928	1.004	0.002	1.057
frozenset({'race_BLACK'})	frozenset({'Reason', 'Male'})	0.536	0.848	0.460	0.859	1.013	0.006	1.078
frozenset({'race_WHITE-HISPANIC', 'Male'})	frozenset({'Reason'})	0.228	0.923	0.212	0.929	1.006	0.001	1.074
frozenset({'Reason', 'race_WHITE-HISPANIC'})	frozenset({'Male'})	0.228	0.916	0.212	0.927	1.012	0.003	1.154
frozenset({'race_WHITE-HISPANIC'})	frozenset({'Reason', 'Male'})	0.246	0.848	0.212	0.859	1.013	0.003	1.080
frozenset({'city_BRONX', 'Reason'})	frozenset({'Male'})	0.177	0.916	0.161	0.913	0.996	-0.001	0.961
frozenset({'city_BRONX', 'Male'})	frozenset({'Reason'})	0.176	0.923	0.161	0.919	0.995	-0.001	0.942
frozenset({'city_BRONX'})	frozenset({'Reason', 'Male'})	0.193	0.848	0.161	0.837	0.987	-0.002	0.931
frozenset({'Reason', 'detailcm_ROBBERY'})	frozenset({'Male'})	0.203	0.916	0.191	0.944	1.030	0.006	1.489
frozenset({'Male', 'detailcm_ROBBERY'})	frozenset({'Reason'})	0.207	0.923	0.191	0.924	1.000	0.000	1.001
frozenset({'detailcm_ROBBERY'})	frozenset({'Reason', 'Male'})	0.220	0.848	0.191	0.870	1.026	0.005	1.171
frozenset({'detailcm_CPW', 'Reason'})	frozenset({'Male'})	0.229	0.916	0.219	0.953	1.040	0.008	1.775
frozenset({'detailcm_CPW', 'Male'})	frozenset({'Reason'})	0.232	0.923	0.219	0.940	1.018	0.004	1.287
frozenset({'detailcm_CPW'})	frozenset({'Reason', 'Male'})	0.244	0.848	0.219	0.895	1.055	0.011	1.442
frozenset({'city_MANHATTAN', 'Reason'})	frozenset({'Male'})	0.190	0.916	0.172	0.903	0.986	-0.002	0.868
frozenset({'city_MANHATTAN', 'Male'})	frozenset({'Reason'})	0.188	0.923	0.172	0.914	0.990	-0.002	0.892
frozenset({'city_MANHATTAN'})	frozenset({'Reason', 'Male'})	0.209	0.848	0.172	0.824	0.972	-0.005	0.863
frozenset({'city_BROOKLYN', 'Reason'})	frozenset({'Male'})	0.326	0.916	0.299	0.918	1.002	0.000	1.018
frozenset({'city_BROOKLYN', 'Male'})	frozenset({'Reason'})	0.320	0.923	0.299	0.934	1.011	0.003	1.152
frozenset({'city_BROOKLYN'})	frozenset({'Reason', 'Male'})	0.350	0.848	0.299	0.855	1.008	0.002	1.045
frozenset({'city_QUEENS', 'Male'})	frozenset({'Reason'})	0.197	0.923	0.184	0.931	1.009	0.002	1.118
frozenset({'Reason', 'city_QUEENS'})	frozenset({'Male'})	0.195	0.916	0.184	0.945	1.031	0.006	1.512
frozenset({'city_QUEENS'})	frozenset({'Reason', 'Male'})	0.210	0.848	0.184	0.877	1.034	0.006	1.231
frozenset({'Reason', 'race_BLACK', 'detailcm_ROBBERY'})	frozenset({'Male'})	0.112	0.916	0.106	0.952	1.039	0.004	1.735
frozenset({'race_BLACK', 'Male', 'detailcm_ROBBERY'})	frozenset({'Reason'})	0.116	0.923	0.106	0.918	0.994	-0.001	0.933
frozenset({'race_BLACK', 'detailcm_ROBBERY'})	frozenset({'Reason', 'Male'})	0.122	0.848	0.106	0.872	1.028	0.003	1.189
frozenset({'detailcm_CPW', 'Reason', 'race_BLACK'})	frozenset({'Male'})	0.143	0.916	0.138	0.964	1.052	0.007	2.313
frozenset({'detailcm_CPW', 'race_BLACK', 'Male'})	frozenset({'Reason'})	0.146	0.923	0.138	0.943	1.021	0.003	1.339
frozenset({'detailcm_CPW', 'race_BLACK'})	frozenset({'Reason', 'Male'})	0.152	0.848	0.138	0.908	1.070	0.009	1.644
frozenset({'city_BROOKLYN', 'Reason', 'race_BLACK'})	frozenset({'Male'})	0.211	0.916	0.195	0.926	1.011	0.002	1.138
frozenset({'city_BROOKLYN', 'race_BLACK', 'Male'})	frozenset({'Reason'})	0.209	0.923	0.195	0.935	1.013	0.003	1.186
frozenset({'city_BROOKLYN', 'race_BLACK'})	frozenset({'Reason', 'Male'})	0.226	0.848	0.195	0.865	1.019	0.004	1.122
The confidence value related with Black race is always high even if it is related with the reason of what they are wearing or actions indicative of drug transaction, casing a victim or location, suspect as a lookout or others. Top detailed crimes are robbery and Criminal Possession of a Weapon.
The black race male of wearing cloths involved in crimes or casing a victim or location or suspect to lookout found in Brooklyn city is high.
Report 3: Cluster Analysis 
Define and prepare your class variables. 
To analysis the crime of Assault based on the different five cities of New York and 76 police stations, all the columns of people stopped by reason like(cs_cloth, cs_objcs, cs_descr, cs_casang, cs_lkout, cs_drgtr, cs_vcrim, cs_bulge, cs_other).

Remove variables that are not needed/useful for the analysis.
To do analysis only City, longitude, latitude, police stations, cs_cloth, cs_objcs, cs_descr, cs_casang, cs_lkout, cs_drgtr, cs_vcrim, cs_bulge, cs_other, from detailcm only Assault is used, tried to use Robbery and CPW but there was memory problem with the system so Assault is used

Describe the final dataset that is used for classification and include the scale/range for the new combined variables. 
Table 4 below shows the final dataset used for classification

Columns	Data type	Range
City	String	Brooklyn, Bronx, Queens, Manhattan, Staten is
PCT	Number	1-123
Detailcm	String	ASSAULT
cs_cloth	String	Yes/No
cs_objcs	string	Yes/No
cs_descr	string	Yes/No
cs_casang	string	Yes/No
cs_lkout	string	Yes/No
cs_drgtr	string	Yes/No
cs_vcrim	string	Yes/No
cs_bulge	string	Yes/No
cs_other	string	Yes/No
lon	Float64	-73.914098 to -74.174762
lat	Float64	40.806274 to 40.526736

Modelling 
Perform cluster analysis. 
The crime used to cluster according to location is Assault, then apply hierarchical clustering on a range of arbitrary values of number of city (5) to number of police stations (76) and recording the silhouette_score and find the best number of clusters. Due to memory issue offset value of 20. The number of clusters formed are 4.The best value of the cluster is 25.
How did you determine a suitable number of clusters for each method? 
To find the suitable clusters for each method hierarchical clustering on a range of arbitrary values and recording the silhouette_score and find the best number of clusters. In range of number of city and number of police stations.
Evaluation 
Describe your results. What findings are the most interesting? How can these findings be used? 
The result defines that maximum number of assault cases are in Brooklyn so police officers need to pay more attention in that city to control the crime and staten is has the least cases so police can be provide to Brooklyn in order to control cases there and Detailed investigation needs to be done in order to find the reason of the cases.

Report 4: Predictive Modelling

Data Preparation 
Define and prepare your class variables. 
Note: You may have to combine different columns. 
Columns used for this analysis are cs_cloth, cs_objcs, cs_descr, cs_casang, cs_lkout,cs_drgtr, cs_vcrim, cs_bulge,cs_other, rf_rfcmp, rf_verbl, rf_vcrim,rf_othsw,rf_attir, rf_vcact, rf_knowl, rf_furt, rf_bulg, to create a column named forces by combining  columns pf_hands, pf_wall,  pf_grnd, pf_drwep,  pf_ptwep, pf_baton, pf_hcuff, pf_pepsp, pf_other.Combining all the above columns to create a Boolean data frame.

Remove variables that are not needed/useful for the analysis. 
Create Labels for dataset and then dropping forces column.

Describe the final dataset that is used for classification and include the scale/range for the new combined variables.
Table 5 below describes the final dataset used to analysis 
Columns	Data type	Range
age	float	15-78
weight	float	45-90
height	float	160-190
cs_cloth	Boolean	True/False
cs_objcs	Boolean	True/False
cs_descr	Boolean	True/False
cs_casang	Boolean	True/False
cs_lkout	Boolean	True/False
cs_drgtr	Boolean	True/False
cs_vcrim	Boolean	True/False
cs_bulge	Boolean	True/False
cs_other	Boolean	True/False
Pf_hands	Boolean	True/False
Pf_wall	Boolean	True/False
Pf_others	Boolean	True/False
Pf_grnd	Boolean	True/False
Pf_drwep	Boolean	True/False
Pf_ptwep	Boolean	True/False
Pf_baton	Boolean	True/False
Pf_hdcuff	Boolean	True/False
Pf_pepsp	Boolean	True/False
City 	string	Brooklyn, Bronx, Queens, Manhattan, Staten is
race	string	blank,asian/Pacific islander,american indian/alaskan 
native,Black-hispanic,white-hispanic,white, unknown,other
Build	string	blank.heavy,medium,
thin,muscular,unknown



Modelling 
Create at least three different classification models (different techniques) for each of the classification tasks. 
Decision Tree, Logistic Regression and Multinomial Regression is used to analysis the physical forces used by forces police officers using different variables such as Reason for Frisk, reason for stop, city, build, race, height weight of the person. By trying all these models it is found that Decision is giving the best F1 score from all .


Discuss the advantages of each model for this classification task.
Decision Tree gives the best F1 score value of testing result for this classification. Decision tree forces managers to consider a range of options rather than relying on hunch.

Logistic Regression makes no assumptions about distributions of classes in feature space.

Multinomial Regression has ability to determine the relative influence of one or more predictor variables to the criterion value


What are the most important variables found by each model? 
For Decision Trees: REASON FOR FRISK - FURTIVE MOVEMENTS, REASON FOR FRISK - VIOLENT CRIME SUSPECTED, BROOKLYN
For Logistic Regression: REASON FOR FRISK - OTHER SUSPICION OF WEAPONS, REASON FOR FRISK - VIOLENT CRIME SUSPECTED, REASON FOR FRISK - SUSPICIOUS BULGE
Assess how well each model performs (use training/test data, cross validation, etc., as appropriate). 
Decision Tree Classifier is used that gives following results for training and testing
Training Result:                                                                             Testing Result
Accuarcy:0.9915104699761174                                                    0.759827572364381
Precision:0.99679273443206				       0.31880773923653477
Recall:0.9546401471952314				       0.33684792117500806
F1 score:09752611751912696                                                      0.3275796449280229

Logistic Classifier is used that gives following results for training and testing
Training Result							Testing Result
Accuracy:0.8203977951211191					0.821975754861822
Precision:0.4368363522798251					0.4366852886405959
Recall:0.08507823548195793					0.08507823548195793


Multinomial Regression is used that gives following results:
Training Result 							Testing Result
Accuracy:0.8070864252814739					0.8090375511770727
Precision:0.3831802120143427					0.386362684055532
Recall:0.1648951538098931					 0.16911460011971086
F1 score:0.23056887405249676					 0.2352451404233516
F1Score:0.14241895864886533					 0.1442244858735345


Evaluation
How useful is your model for the police? How would you measure the model’s value if it were used? 
This model needs more improvement to finally put in effective. With this model police officers can eliminate the variables that are not affecting the results, can reduce the collection of variables that are not affecting the results.

How would your implement your model to improve policing? What other data should be collected? How often would your model need to be updated? 
To improve the model’s performance, we can eliminate the variables are affecting the result more towards the negative result such as height, weight, age in multinomial Regression Model. Model needs to be updated as soon as new data is collected.


Conclusion

During SQF 2012 more young male black and white Hispanic people are stopped and frisked, the rate of finding weapons is low. From the results it is observed that police officers biased more Many people opposed the SQF due to which government restrict SQF.
More data is required to predictive anything from such models as the testing value of all the models is really low.

