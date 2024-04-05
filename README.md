# I369-Spring-2023
## Performance Analytics Project

Our goal was to analyze NFL Statistics from 2000-2023 in search of find the correlation between numbers of turnovers and wins along with if there was any home field advantage in the NFL.

## Turnover Effect

<img width="658" alt="Screenshot 2024-04-05 at 6 22 45 PM" src="https://github.com/mjleitgeb/i369/assets/166170067/0d3e7db1-6ba4-408e-81cc-3f7741c80fa6">

- Average winning:1.044624090541633
- Average losing:2.1023443815683103
- Winning Variance:1.0489383590962824 
- Losing Variance:1.9699621675775685

Implementation: Calculated probability distribution of both winning and losing teams turnovers per game then plotted them over each other. Each step commented in code.
Description:The probability of a team's chance of causing a turnover is much higher in losing teams over winning teams. A team that wins on average has less of a chance of turning over the ball. On average, a winning team only turns over the ball 1.04 times and a losing team turns over the ball 2.1 times. The variance of losing team's turnovers probability distribution is almost a full unit higher than a winning team. A losing team's probability distribution of turning over the ball is much more spread out than a winning team's.


## Home vs. Away

<img width="641" alt="Screenshot 2024-04-05 at 6 23 53 PM" src="https://github.com/mjleitgeb/i369/assets/166170067/d4a4fecc-bd88-4c6b-906c-fcc13213ccb3">

- alpha :  21.12183611703535
- beta :  -0.011155646515864327
- correlation coefficient :  -0.01143842242470336

Implementation: Created a scatterplot of scores of home vs. away teams. Calculated line regression of both teams to see correlation. Each step commented in code.
Description: The correlation of home vs. away team scores is very low, almost 0 even. This shows both teams have equal likeliness to score no matter the location. The intercept shows that teams will score around 21 total points and the slope for that line is almost 0. Over the past 22 years, it seems that there is no advantage over the long-term of home-field advantage for a given team. 
