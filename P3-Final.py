from bs4 import BeautifulSoup
import random
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline  
from scipy.stats import poisson

soup = BeautifulSoup(open('Games/2000.htm'), 'lxml')
table = soup.find_all('table')
rows = table[0].find_all('tr')

#Storing values for graphing
tol = [] #Turnovers for losing team
tow = [] #Turnovers for winning team
wts = [] #Winning team scores
lts = [] #Losing team scores
h_s = [] #Home score
a_s = [] #Away Score
total_s = [] #Total Score
for year in range (2000, 2023, 1):
    filein = 'Games/' + str(year) + '.htm'
    soup = BeautifulSoup(open(filein), 'lxml')

    
    entries = soup.find_all('tr', attrs={'class' : ''})
    for entry in entries:
    #print entry
        columns = entry.find_all('td')
        if len (columns)>12 :
        
            day = columns[0].get_text()
            
            date = columns[1].get_text()

            time = columns[2].get_text()

            winning_team = columns[3].get_text()

            losing_team = columns[5].get_text()

            #checking if values are blank (if so, set them to 0)
            winning_team_score = columns[7].get_text()
            if(winning_team_score != ''):
                winning_team_score = int(winning_team_score)
            else:
                winning_team_score = 0
            wts.append(winning_team_score)

            losing_team_score = columns[8].get_text()
            if(losing_team_score != ''):
                losing_team_score = int(losing_team_score)
            else:
                losing_team_score = 0
            lts.append(losing_team_score)
            
            #totalling score
            if(columns[4].get_text()== '@'):
                home_score = losing_team_score
                away_score = winning_team_score
                total = home_score + away_score
                total_s.append(total)
                total = 0
                h_s.append(home_score)
                a_s.append(away_score)
            else:
                home_score = winning_team_score
                away_score = losing_team_score
                total = home_score + away_score
                total_s.append(total)
                total = 0
                h_s.append(home_score)
                a_s.append(away_score)

            yards_winning_team = columns[9].get_text()

            turnovers_winning_team = columns[10].get_text()
            if(turnovers_winning_team != ''):
                turnovers_winning_team = int(turnovers_winning_team)
            else:
                turnovers_winning_team = 0
            tow.append(turnovers_winning_team)
            
            yards_losing_team = columns[11].get_text()

            turnovers_losing_team = columns[12].get_text()
            if(turnovers_losing_team != ''):
                turnovers_losing_team = int(turnovers_losing_team)
            else:
                turnovers_losing_team = 0
            tol.append(turnovers_losing_team)
            #print("TOL:" + turnovers_losing_team)

#Implementation:Empirical Probability Distribution of winning and losing teams turnovers per game
#Find values for emprical probability distribution histogram
def measure_probability_distribution (outcomes):
    
    average_value = 0.0
    variance = 0.0
    
    pdf = {}
    norm = 0.0
    
    ##count number of observations
    for x in outcomes:
        if x not in pdf:
            pdf[x] = 0.0
        pdf[x] += 1.0
        norm += 1.0
        
        average_value += x
        variance += x*x
        
        
    average_value /= norm
    variance /= norm
    variance = variance - average_value * average_value
        
        
    ##normalize pdf
    for x in pdf:
        pdf[x] /= norm
    
    
    return pdf, average_value, variance
pdf, av, var = measure_probability_distribution(tol)
#Winning vs Losing probability distribution measuring
pdf_w, av_w, var_w = measure_probability_distribution (tow)
pdf_l, av_l, var_l = measure_probability_distribution (tol)
print("Average winning:" + str(av_w) + " Average losing:" + str(av_l))
print("Winning Variance:" + str(var_w) + " Losing Variance:" + str(var_l))

#Visualizing the histograms
plt.figure(figsize=(10,10))
plt.rc('text', usetex=True)
plt.rc('font', size=24, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8

plt.xlabel('total number of turnovers in a game')
plt.ylabel('probability distribution')

#Construct two lists for winning visualization
x = []
Px = []
for q in pdf_w:
    x.append(q)
    Px.append(pdf_w[q])
    
#Plot Winning Histogram 
plt.bar(x, Px, color = 'red', align='center', alpha=0.5, label = 'winning')
plt.plot(sorted(x), poisson.pmf(sorted(x), av_w), linestyle='-', linewidth=2.0, color='red', label = '$\lambda_w = '+'%.2f' % av_w+'$')


#Construct two lists for losing visualization
x = []
Px = []
for q in pdf_l:
    x.append(q)
    Px.append(pdf_l[q])
    
#Plot Losing Histogram 
plt.bar(x, Px, color = 'blue', align='center', alpha=0.5, label = 'losing')
plt.plot(sorted(x), poisson.pmf(sorted(x), av_l), linestyle='-', linewidth=2.0, color='blue', label = '$\lambda_l = '+'%.2f' % av_l+'$')

#Plot legend
plt.legend(loc='upper right', numpoints=1, prop={'size':30})

plt.show()
print("Implementation: Calculated probability distribution of both winning and losing teams turnovers per game then plotted them over each other. Each step commented in code.")
print("Description:The probability of a team's chance of causing a turnover is much higher in losing teams over winning teams. A team that wins on average has less of a chance of turning over the ball. On average, a winning team only turns over the ball 1.04 times and a losing team turns over the ball 2.1 times. The variance of losing team's turnovers probability distribution is almost a full unit higher than a winning team. A losing team's probability distribution of turning over the ball is much more spread out than a winning team's.")

#Implementation: Scatterplot and line regression of home vs. away scores
from scipy import stats

#Display/Calculate Slope, Intercept, Correlation Coefficient, and Standard Deviation for line regression of scores
slope, intercept, r_value, p_value, std_err = stats.linregress(h_s,a_s)
print ('alpha : ', intercept)
print ('beta : ', slope)
print ('correlation coefficient : ', r_value)

#Create Plot
plt.figure(figsize=(10,10))
plt.rc('text', usetex=True)
plt.rc('font', size=22, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8

#Labels
plt.xlabel('total number of points, home')
plt.ylabel('total number of points, visitors')

#Plot Points
plt.plot(h_s,a_s,marker='o', color ='red', markersize=5, alpha=0.15, linewidth=0)

#Find lines of best fit
best_fit_x = np.arange(min(h_s), max(h_s), (max(h_s) - min(h_s)) / 1000.0)
best_fit_y = intercept + slope * best_fit_x
#Plot lines
plt.plot(best_fit_x, best_fit_y, color ='black', markersize=0, linewidth=3, linestyle='-', alpha = 1.0, label = 'Best linear fit')
plt.plot(best_fit_x, best_fit_x, color ='blue', markersize=0, linewidth=3, linestyle='--', alpha = 1.0, label = 'Equal number of points')

#Legend
plt.legend(loc = 'upper left', fontsize = 18)

plt.show()

print("Implementation: Created a scatterplot of scores of home vs. away teams. Calculated line regression of both teams to see correlation. Each step commented in code.")
print("Description: The correlation of home vs. away team scores is very low, almost 0 even. This shows both teams have equal likeliness to score no matter the location. The intercept shows that teams will score around 21 total points and the slope for that line is almost 0. Over the past 22 years, it seems that there is no advantage over the long-term of home-field advantage for a given team. ")

