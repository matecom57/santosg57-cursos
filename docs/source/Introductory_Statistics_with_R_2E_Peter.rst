Introductory Statistics with R, 2E, Peter
=========================================

1 Basics
--------

1.1 First steps .
1.1.1 An overgrown calculator .
1.1.2 Assignments .
1.1.3 Vectorized arithmetic .
1.1.4 Standard procedures .
1.1.5 Graphics .

1.2 R language essentials .
1.2.1 Expressions and objects .
1.2.2 Functions and arguments .
1.2.3 Vectors .
1.2.4 Quoting and escape sequences .
1.2.5 Missing values .
1.2.6 Functions that create vectors .
1.2.7 Matrices and arrays .
1.2.8 Factors .
1.2.9 Lists .
1.2.10 Data frames .
1.2.11 Indexing .
1.2.12 Conditional selection .
1.2.13 Indexing of data frames .
1.2.14 Grouped data and data frames .xii
1.2.15 Implicit loops .
1.2.16 Sorting .
1.3 Exercises .26

2 The R environment
--------------------

2.1 Session management .
2.1.1 The workspace .
2.1.2 Textual output .
2.1.3 Scripting .
2.1.4 Getting help .
2.1.5 Packages .
2.1.6 Built-in data .
2.1.7 attach and detach .
2.1.8 subset, transform, and within .

2.2 The graphics subsystem .
2.2.1 Plot layout .
2.2.2 Building a plot from pieces .
2.2.3 Using par .
2.2.4 Combining plots .

2.3 R programming .
2.3.1 Flow control .
2.3.2 Classes and generic functions .

2.4 Data entry .
2.4.1 Reading from a text file .
2.4.2 Further details on read.table .
2.4.3 The data editor .
2.4.4 Interfacing to other programs .

2.5 Exercises .31

3 Probability and distributions
-------------------------------

3.1 Random sampling .
3.2 Probability calculations and combinatorics .
3.3 Discrete distributions .
3.4 Continuous distributions .

3.5 The built-in distributions in R .
3.5.1 Densities .
3.5.2 Cumulative distribution functions .
3.5.3 Quantiles .
3.5.4 Random numbers .

3.6 Exercises .55

4 Descriptive statistics and graphics
-------------------------------------

4.1 Summary statistics for a single group .

4.2 Graphical display of distributions .
4.2.1 Histograms .67
4.2.2 Empirical cumulative distribution .
4.2.3 Q–Q plots .
4.2.4 Boxplots .

4.3 Summary statistics by groups .
4.4 Graphics for grouped data .
4.4.1 Histograms .
4.4.2 Parallel boxplots .
4.4.3 Stripcharts .

4.5 Tables .
4.5.1 Generating tables .
4.5.2 Marginal tables and relative frequency .

4.6 Graphical display of tables .
4.6.1 Barplots .
4.6.2 Dotcharts .
4.6.3 Piecharts .
Exercises .73

5 One- and two-sample tests
5.1 One-sample t test .
5.2 Wilcoxon signed-rank test .
5.3 Two-sample t test .
5.4 Comparison of variances .
5.5 Two-sample Wilcoxon test .
5.6 The paired t test .
5.7 The matched-pairs Wilcoxon test .
5.8 Exercises .95

6 Regression and correlation
6.1 Simple linear regression .
6.2 Residuals and fitted values .
6.3 Prediction and confidence bands .

6.4 Correlation .
6.4.1 Pearson correlation .
6.4.2 Spearman’s ρ .
6.4.3 Kendall’s τ .
6.5 Exercises .109

7 Analysis of variance and the Kruskal–Wallis test
7.1 One-way analysis of variance .
7.1.1 Pairwise comparisons and multiple testing .
7.1.2 Relaxing the variance assumption .
7.1.3 Graphical presentation .
7.1.4 Bartlett’s test .

7.2 Kruskal–Wallis test .

7.3 Two-way analysis of variance .127
7.3.1 Graphics for repeated measurements .
7.4 The Friedman test .
7.5 The ANOVA table in regression analysis .
7.6 Exercises .140

8 Tabular data
8.1 Single proportions .
8.2 Two independent proportions .
8.3 k proportions, test for trend .
8.4 r × c tables .
8.5 Exercises .145

9 Power and the computation of sample size
9.1 The principles of power calculations .
9.1.1 Power of one-sample and paired t tests .
9.1.2 Power of two-sample t test .
9.1.3 Approximate methods .
9.1.4 Power of comparisons of proportions .

9.2 Two-sample problems .
9.3 One-sample problems and paired tests .
9.4 Comparison of proportions .
9.5 Exercises .155

10 Advanced data handling
-------------------------

10.1 Recoding variables .
10.1.1 The cut function .
10.1.2 Manipulating factor levels .
10.1.3 Working with dates .
10.1.4 Recoding multiple variables .

10.2 Conditional calculations .

10.3 Combining and restructuring data frames .
10.3.1 Appending frames .
10.3.2 Merging data frames .
10.3.3 Reshaping data frames .

10.4 Per-group and per-case procedures .
10.5 Time splitting .
10.6 Exercises .163

11 Multiple regression
----------------------

11.1 Plotting multivariate data .
11.2 Model specification and output .
11.3 Model search .
11.4 Exercises .185

12 Linear models
----------------

12.1 Polynomial regression .
12.2 Regression through the origin .
12.3 Design matrices and dummy variables .
12.4 Linearity over groups .
12.5 Interactions .
12.6 Two-way ANOVA with replication .

12.7 Analysis of covariance .
12.7.1 Graphical description .
12.7.2 Comparison of regression lines .
12.8 Diagnostics .
12.9 Exercises .195

13 Logistic regression
13.1 Generalized linear models .

13.2 Logistic regression on tabular data .
13.2.1 The analysis of deviance table .
13.2.2 Connection to test for trend .

13.3 Likelihood profiling .
13.4 Presentation as odds-ratio estimates .
13.5 Logistic regression using raw data .
13.6 Prediction .
13.7 Model checking .
13.8 Exercises .227

14 Survival analysis
--------------------

14.1 Essential concepts .
14.2 Survival objects .
14.3 Kaplan–Meier estimates .
14.4 The log-rank test .
14.5 The Cox proportional hazards model .
14.6 Exercises .249

15 Rates and Poisson regression
-------------------------------

15.1 Basic ideas .
15.1.1 The Poisson distribution .
15.1.2 Survival analysis with constant hazard .
15.2 Fitting Poisson models .
15.3 Computing rates .
15.4 Models with piecewise constant intensities .
15.5 Exercises .259

16 Nonlinear curve fitting
--------------------------

16.1 Basic usage .
16.2 Finding starting values .275
16.3 Self-starting models .
16.4 Profiling .
16.5 Finer control of the fitting algorithm .
16.6 Exercises .

A Obtaining and installing R and the ISwR package289
B Data sets in the ISwR package293
C Compendium325
D Answers to exercises337
Bibliography355
Index3571

