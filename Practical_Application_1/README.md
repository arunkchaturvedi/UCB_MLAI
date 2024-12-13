## University of California Berkeley - MLAI Professional Certification Practical Application 1 --> Will the Customer Accept the Coupon

Goal of this assignment is to analyze coupon data provieded in .csv file 'data/coupon.csv' and identify patterns related to customers accepting driving coupons. 
I will be using data cleaning/preperation, visualization and other steps to arrive at observation and hypothesis

This assignment submission has following artifacts
1. Link to [Jupyter Notebook](practical_application_1.ipynb)
2. Link to [Data Folder](data/)
3. Link to [Images Folder](images/)
4. Link to [License File](LICENSE.md)


Following libraries were used for the project: matplotlib.pyplot, seaborn, pandas, and numpy.


**Steps:**
1. **Data Cleanup:** 
Entire Dataset was reviewed to isolate columns with mising or not-applicable values. Column [Car] was removed as it had more than 99% missing values. 5 columns ['CoffeeHouse'], ['Restaurant20To50'], ['CarryAway'], ['RestaurantLessThan20'],and ['Bar'] were missing around 1% of values so records with missing values were removevd using .dropna()
2. **Check New Data** 
New dataframe was compared with old datafrme for proportion of coupon accpetance. Proportion in old and cleaned up dataframes were almost identical **'56.9 : 43:1'** as compared to **'56.8 : 43.2'** so at this point data cleanup was deemed to be complete without impacing sanctity of the original dataset in any meaningful way. 
3. **Analysis and Visulaization** 
Based on prompts provided visualization of [coupon] column was done an Histogram for [temperature] column were created. 
* Bar Coupon Analysis: After that anlysis for Bar coupons was done that resulted in following observation and hypothesis
- More than half the drivers (almost 59%) declined Bar coupons, when oerall coupon decline rats is lower at around 43%. 
- Drivers had higher chances of accepting coupons when they were not accompanied by Kid(s) as passengers
- Drivers that went to bars more than 4 times had about 2 times higher changes of accepting coupons as compared to drivers who went to bars 3 times or less
- **Hypothesis:** Drivers are more likely to decline Bar coupons. But when they are 1/travelling without kids; and 2/go to bars regularly, their chances of accpeting Bar coupons are higher. 

* Coffee House Coupon Analysis: Coffee house coupon anlysis was done which resulted in following observation and hypothesis
- Drivers are more likely to avail Coffee House coupons during snow or rainy weather as compared to when it is sunny outside
- Drivers that are dirving with Kid(s), partners are more likely to accept coupon as comapred to drivers who are alone or with Friend(s)
- Drivers that go to coffee house 4 or more times are 25% more likely, in comparison, to accpet coffee house coupons as compared to drivers that go to coffee houses 3 times or less 
- Female drivers are more likely to order cofee s compared to male drivers
- **'Hypothesis:'** Female drivers when travelling with Kids in Snow or Rain will 100% avail the coupons for Coffee House.

**Overall Hypothesis** Drivers that frequent bars or coffee houses are more likely to avail coupons for bars and coffee houses respedctively.
