**key findings:**
73% of anomalies earn their alpha primarily overnight. Only 9% are intraday-dominant. The remaining 19% are mixed.
The scatter plot in the output folder shows overnight annual alphah vs intraday annual alpha for 162 anomalies. |

momentum is overwhelmingly overnight. all 21 momentum variants earn the majority of their alpha between market close and next open. 

Volatility anomalies are also overnight dominant, but with negative signals. High volatility stocks lose money in both sessions, but lose even more overnight. IdioVol3F: -152% overnight vs -53% intraday. 

Profitability signals skew overnight. This differs from Lou et al's finding that profitability accrues intraday. 

This shows that if we were to run any factor strategy (momentum, value, quality, low-vol) nearly all our alpha accrues between 4pm and 930am. The trading day contributes little to cross sectional return predictability. This has practical implications for execution timing, hedging and portfolio construction. 

The finding also constraints which theories can explain anomaly returns. Any explanation must account for why the effect operates predominantly when markets are closed. Retail trading at open, institutional rebalancing during the day and dealer inventory management are the leading candidates. 

**full results**
Total anomalies decomposed: 162
  OVERNIGHT-dominant: 118 (73%)
  INTRADAY-dominant:  14 (9%)
  MIXED:              30 (19%)

  Overnight alpha > intraday alpha: 107/162 (66%)
  Mean session ratio: 0.70 (1.0 means pure overnight)

  Significant overnight alpha (|t|>1.96): 151/162
  Significant intraday alpha (|t|>1.96):  140/162

t = mean / (standard deviation / sqrt(number of months))
|t| > 1.96 shows statistical significance at 95% level 
* not just 20%  one day and +1000% the next, but less volatile consistent results

top 10 overnight anomalies : 

Anomaly                    Overnight  t     Intraday    t  Ratio
Mom12m                       241.4%  24.1     64.1%  17.2  0.79
Mom6m                        214.7%  22.7     59.8%  16.7  0.78
MomVol                       204.7%  19.0     46.7%  11.4  0.81
Mom12mOffSeason              198.9%  21.2     51.6%  15.1  0.79
IO_ShortInterest             183.7%   9.7     88.8%  10.9  0.67
IntanSP                      181.5%  29.4     41.6%  16.3  0.81
roaq                         175.4%  24.6     52.2%  17.6  0.77
Mom6mJunk                    165.8%  18.5     51.5%  12.9  0.76
FirmAgeMom                   156.3%  19.6     22.0%   6.9  0.88
OperProfRD                   152.4%  23.6     56.1%  19.4  0.73


top 10 intraday anomalies :
Anomaly                    Overnight   t   Intraday    t  Ratio
IO_ShortInterest             183.7%   9.7     88.8%  10.9  0.67
ProbInformedTrading           84.6%   7.2     71.0%   9.8  0.54
Mom12m                       241.4%  24.1     64.1%  17.2  0.79
FEPS                         128.5%  16.7     63.7%  16.2  0.67
Mom6m                        214.7%  22.7     59.8%  16.7  0.78
CBOperProf                   137.4%  25.0     58.4%  23.6  0.70
sfe                           91.8%  12.3     57.4%  17.2  0.62
AnnouncementReturn           130.5%  48.4     56.5%  34.8  0.70
OperProfRD                   152.4%  23.6     56.1%  19.4  0.73
GP                            74.5%  20.7     53.3%  26.4  0.58


opposite signs across sessions (33 anomalies) <-- tug of war (Lou et al., 2018)
Anomaly                    Overnight   Intraday   Spread
zerotrade1M                  -32.1%     48.2%    -80.3%
SP                           -67.9%      4.7%    -72.6%
zerotrade6M                  -11.9%     50.5%    -62.4%
VolumeTrend                   16.7%    -36.9%     53.7%
DelDRC                        50.3%     -2.2%     52.5%
ShortInterest                 25.4%    -26.8%     52.2%
TrendFactor                    7.1%    -41.1%     48.2%
NetDebtPrice                  45.8%     -0.9%     46.7%
CoskewACX                    -43.3%      0.4%    -43.8%
OrderBacklog                  38.7%     -0.2%     39.0%


intraday dominant anomalies (intraday higher t )

Anomaly                    Overnight   t   Intraday    t
zerotrade6M                  -11.9%  -2.1     50.5%  17.4
zerotrade12M                   1.5%   0.3     48.3%  16.6
BMdec                          7.6%   2.5     23.7%  12.1
SmileSlope                    -2.2%  -0.9     23.5%  14.6
dCPVolSpread                   9.4%   4.6     21.5%  18.1
BM                            -2.2%  -0.6     20.2%   8.2
AbnormalAccruals               2.8%   1.8      8.8%  10.5
Activism1                     -1.5%  -0.3     -4.1%  -2.0
BetaLiquidityPS               -2.6%  -0.8     -4.2%  -2.2
InvGrowth                      6.8%   2.9    -11.0%  -9.5
CPVolSpread                    8.1%   3.3    -12.3%  -9.5
BetaTailRisk                 -11.2%  -2.1    -18.2%  -6.9
VolumeTrend                   16.7%   4.8    -36.9% -23.4
TrendFactor                    7.1%   1.1    -41.1% -10.2


momentum cluster (21 anomalies)
  Mom12m                    over= 241.4%  intra=  64.1%  class=OVERNIGHT
  Mom6m                     over= 214.7%  intra=  59.8%  class=OVERNIGHT
  MomVol                    over= 204.7%  intra=  46.7%  class=OVERNIGHT
  Mom12mOffSeason           over= 198.9%  intra=  51.6%  class=OVERNIGHT
  Mom6mJunk                 over= 165.8%  intra=  51.5%  class=OVERNIGHT
  FirmAgeMom                over= 156.3%  intra=  22.0%  class=OVERNIGHT
  IntMom                    over= 151.8%  intra=  36.0%  class=OVERNIGHT
  ResidualMomentum          over= 122.8%  intra=  20.2%  class=OVERNIGHT
  MomSeasonShort            over=  49.3%  intra=  15.8%  class=OVERNIGHT
  MomOffSeason              over=  47.9%  intra=   8.7%  class=OVERNIGHT
  IndMom                    over=  41.4%  intra=   4.6%  class=OVERNIGHT
  CustomerMomentum          over=  35.0%  intra=  28.9%  class=MIXED
  MomOffSeason06YrPlus      over=  22.2%  intra=   2.8%  class=OVERNIGHT
  iomom_supp                over=  22.0%  intra=  11.4%  class=OVERNIGHT
  MomOffSeason11YrPlus      over=  21.5%  intra=   2.1%  class=OVERNIGHT
  iomom_cust                over=  20.1%  intra=  15.0%  class=MIXED
  MomSeason                 over=  19.6%  intra=   9.2%  class=OVERNIGHT
  MomOffSeason16YrPlus      over=  14.8%  intra=   3.3%  class=OVERNIGHT
  MomSeason06YrPlus         over=  13.0%  intra=   7.0%  class=OVERNIGHT
  MomSeason11YrPlus         over=  10.6%  intra=   3.4%  class=OVERNIGHT
  MomSeason16YrPlus         over=   9.0%  intra=   1.8%  class=OVERNIGHT


volatility clustr ( 14 anomalies)
  MomVol                    over= 204.7%  intra=  46.7%  class=OVERNIGHT
  OptionVolume2             over=  68.1%  intra=  22.4%  class=OVERNIGHT
  OptionVolume1             over=  56.3%  intra=   3.9%  class=OVERNIGHT
  RIVolSpread               over=  29.8%  intra=  11.6%  class=OVERNIGHT
  VolumeTrend               over=  16.7%  intra= -36.9%  class=INTRADAY
  dCPVolSpread              over=   9.4%  intra=  21.5%  class=INTRADAY
  CPVolSpread               over=   8.1%  intra= -12.3%  class=INTRADAY
  VolSD                     over= -30.0%  intra= -43.8%  class=MIXED
  dVolPut                   over= -30.4%  intra= -38.5%  class=MIXED
  dVolCall                  over= -39.8%  intra= -59.1%  class=MIXED
  VolMkt                    over= -92.8%  intra= -82.9%  class=MIXED
  VarCF                     over=-133.2%  intra= -42.3%  class=OVERNIGHT
  RealizedVol               over=-147.4%  intra= -55.5%  class=OVERNIGHT
  IdioVol3F                 over=-152.2%  intra= -53.3%  class=OVERNIGHT


value cluster (19 anomalies)
  IntanBM                   over= 146.7%  intra=  30.6%  class=OVERNIGHT
  FEPS                      over= 128.5%  intra=  63.7%  class=OVERNIGHT
  cfp                       over=  99.1%  intra=  44.6%  class=OVERNIGHT
  EarningsStreak            over=  99.1%  intra=  19.0%  class=OVERNIGHT
  CF                        over=  91.7%  intra=  43.5%  class=OVERNIGHT
  EarningsSurprise          over=  58.6%  intra=   6.7%  class=OVERNIGHT
  IntanCFP                  over=  55.4%  intra=   8.9%  class=OVERNIGHT
  EarningsConsistency       over=  54.2%  intra=  12.4%  class=OVERNIGHT
  IntanEP                   over=  52.3%  intra=   6.1%  class=OVERNIGHT
  BookLeverage              over=  37.5%  intra=  18.8%  class=OVERNIGHT
  EarnSupBig                over=  30.5%  intra=   6.6%  class=OVERNIGHT
  AnalystValue              over=  15.3%  intra=  20.9%  class=MIXED
  BMdec                     over=   7.6%  intra=  23.7%  class=INTRADAY
  BM                        over=  -2.2%  intra=  20.2%  class=INTRADAY
  BPEBM                     over= -12.5%  intra=  -5.6%  class=OVERNIGHT
  EP                        over= -26.1%  intra=   3.0%  class=OVERNIGHT
  EarningsForecastDisparity over= -85.3%  intra= -11.3%  class=OVERNIGHT
  EBM                       over= -97.6%  intra= -17.0%  class=OVERNIGHT
  VarCF                     over=-133.2%  intra= -42.3%  class=OVERNIGHT


profitability cluster 
  roaq                      over= 175.4%  intra=  52.2%  class=OVERNIGHT
  OperProfRD                over= 152.4%  intra=  56.1%  class=OVERNIGHT
  CBOperProf                over= 137.4%  intra=  58.4%  class=OVERNIGHT
  RoE                       over= 109.1%  intra=  37.5%  class=OVERNIGHT
  GP                        over=  74.5%  intra=  53.3%  class=MIXED
  GP                        over=  74.5%  intra=  53.3%  class=MIXED
  OperProf                  over=  27.8%  intra=  14.5%  class=OVERNIGHT

**pipeline explanation**
The pipeline loads CRSP data, which is US stock's daily prices dating back to 1920s. one row per stock per day. Each row has the stocks PERMNO number, date, PRC, OPENPRC, RET and SHROUT. This data were taken from WRDS. overnight and intraday numbers are then computed from these data. This returns 58 million valid observations. 

overnight = ln(today's open / yesterday's close)
intraday = ln(today's close / today's open)
for additive purposes

we then load all 209 anomaly signals from Chen-Zimmermann dataset collection. we match the PERMNO number and date for and merge the anomaly signals with the CRSP data. 

we then quintile sort for each anomaly. Quintile 1 being the bottom 20% this follows the Fama-French portfolio sort methodology. 

For each day, we compute the average overnight return for quintile 5 and quintile 1 stocks. We then calculate the Long-Short spread by session. Long quintile 5 and short quintile 1. This will be dollar neutral. However, this is results in large numbers such as 241%, without meaning we would actually earn 241%. This shows the return on a zero capital long short portfolio, which is not a realistic P%L. 

The results are aggregated into monthly spreads. 

For each anomaly, we now have a time series of monthly overnight and intraday spreads. 

From these, we compute 
overnight_ann : mean monthly overnight spread * 12
overnight_t : t-statistic
_ann and _t for intraday as well
session)ratio : what fraction of the total absolute alpha comes from overnight. 0.8 meaning 80% overnight. 

these values are then classified to overnight, intraday and mixed
overnight meaning overnight alpha is at least 1.5x larger than intraday AND |t| > 1.65
vice versa
mixed : everything else

**review**
The raw numbers are however not directily tradable due to transactional costs. Quintile rebalancing requires touching hundres of stocks montly. This eliminates large portion of gross alpha. Market impacts of these capital allocations also cause significant market impact to smaller stocks. 

A realistic version restricted to liquid large cap stocks, value weighted with conservative cost estimates might yield 5-15% annual overnight momentum alpha. 

The objective of this research is not as a standalone trading strategy, but as a framework to understand when and why these anomalies return accrue, which informs execution timing, factor timing and portfolio construction at institutional scale. 

**next steps can involve :**
explaining the theory behind this phenomenon, and its implications
Subperiod stability (pre-2010 vs post-2010) to check if any anomalies have switched sessions. 
VIX conditioning to see if overnight and intraday split change in high volatility regimes. 
Value-weighted portfolios: do the results hold when we downweight micro-caps
TugOfWar meta-signal: EWMA(overnight) − EWMA(intraday) as a factor timing indicator
Hypothesis testing: retail clientele, information timing, dealer hedging, ETF rebalancing

