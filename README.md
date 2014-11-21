lottery
=======

A Lottery Number Generator developed in Python.

The concept of the lottery is a fun one.  Everyone would like to win a jackpot which would potentially solve all kinds of financial problems/constraints/limitations. However the fact is, each ticket is like buying a dream, and rarely to ever plays into a significant win. Several people can get $3 to $200 back after that things start to get severely difficult.

Here is an interesting white paper on 'Lottery winning strategies': http://www.bentley.edu/centers/sites/www.bentley.edu.centers/files/csbigs/chen.pdf

And this wiki entry on Lottery mathematics is good to (there is a table with probablity stats): http://en.wikipedia.org/wiki/Lottery_mathematics

For fun here are some interesting Lottery statistics (on the bigger lottos like Powerball which is roughly a 1/195,000,000 odds (these are rough estimates):
- Dying from a bee sting (1-6,000,000)
- Getting hit by lightning (1-6000)
- Getting a hole-in-one playing golf (I actually saw this with my own eyes once) (1-12,000)
- Hitting three consecutive hole-in-one events (1-165,000,000)
- Dying from Ebola (if you get it) (25%-90%)
- Becoming president (1 in 10,000,000)
- A highschool baseball player making it to the MLB (1-200)
- Of those MBL draftees playing 1 inning of pro baseball (10%)
- Hitting a deer....in Hawaii (1-6000)
- Getting eaten by a shark (1-10,000,000)
- Dying in a plane crash (1-6000)
- Being born polydactyly (1-500)
- Odds of being born in the United States (1-20)
- Odds of being born at all (1-576,000) <<< If you are reading this...You win
- Odds of becoming a millionare in the stock market (1-750,000)

And here are some interesting statistics on Lottery winners (after they won), their behaviors and what they did with thier money: http://www.statisticbrain.com/lottery-winner-statistics/

The object is to give a good random selection of lottery numbers. 

There is no weighting towards number frequency (which could make for an interesting addition later).

Although this won't scale, it is a good start.  It needs more states/lottery options. That means there will need to be a few additional files to break out of this one page program. It will possibly need another option selector added for state, maybe a fourth, for country if it gets that big.

I should set mega-millions and powerball the first options by default since most all U.S. states participate in those.

The option menu chain should go like this: country->state->lottery
- Country Selector
- State (province) Selector
- Lottery Type Selector

