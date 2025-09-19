Linear Mixed-Effects Models Using R, Andrzej
===============================================

Part I
Introduction
1Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
1.1 The Aim of the Book .. . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
1.2 Implementation of Linear Mixed-Effects Models in R . . . . . . . . . . . . .
1.3 The Structure of the Book . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
1.4 Technical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .3
3
3
5
8
2Case Studies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.2 Age-Related Macular Degeneration Trial . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.2.1 Raw Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.2.2 Data for Analysis . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.3 Progressive Resistance Training Study . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.3.1 Raw Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.3.2 Data for Analysis . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.4 The Study of Instructional Improvement Project . . . . . . . . . . . . . . . . . .
2.4.1 Raw Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.4.2 Data for Analysis . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.4.3 Data Hierarchy . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.5 The Flemish Community Attainment-Targets Study . . . . . . . . . . . . . . .
2.5.1 Raw Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.5.2 Data for Analysis . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
2.6 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .11
11
12
13
14
20
20
22
24
24
26
28
31
32
34
34
3Data Exploration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.2 ARMD Trial: Visual Acuity . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.2.1 Patterns of Missing Data . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.2.2 Mean-Value Profiles . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.2.3 Sample Variances and Correlations of Visual
Acuity Measurements . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .39
39
39
41
42
45
xixii
Contents
3.3
3.4
3.5
3.6
Part II
PRT Study: Muscle Fiber Specific Force . . . . . . .. . . . . . . . . . . . . . . . . . . .
SII Project: Gain in the Math Achievement Score . . . . . . . . . . . . . . . . .
3.4.1 School-Level Data . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.4.2 Class-Level Data . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
3.4.3 Pupil-Level Data . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
FCAT Study: Target Score . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
48
53
55
58
60
63
64
Linear Models for Independent Observations
4Linear Models with Homogeneous Variance . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.2 Model Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.2.1 Model Equation at the Level of the Observation . . . . . . . . . .
4.2.2 Model Equation for All Data . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.3 Offset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.4 Estimation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.4.1 Ordinary Least Squares . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.4.2 Maximum-Likelihood Estimation . . . . .. . . . . . . . . . . . . . . . . . . .
4.4.3 Restricted Maximum-Likelihood Estimation .. . . . . . . . . . . .
4.4.4 Uncertainty in Parameter Estimates . . .. . . . . . . . . . . . . . . . . . . .
4.5 Model Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.5.1 Residuals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.5.2 Residual Diagnostics . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.5.3 Influence Diagnostics . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.6 Inference .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.6.1 The Wald, Likelihood Ratio, and Score Tests . . . . . . . . . . . .
4.6.2 Confidence Intervals for Parameters . .. . . . . . . . . . . . . . . . . . . .
4.7 Model Reduction and Selection . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.7.1 Model Reduction . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.7.2 Model Selection Criteria . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
4.8 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
69
69
70
70
71
71
72
72
73
74
75
75
76
78
80
81
81
84
84
85
86
88
5Fitting Linear Models with Homogeneous Variance:
The lm() and gls() Functions . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 89
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 89
5.2 Specifying the Mean Structure Using a Model Formula . . . . . . . . . . . 89
5.2.1 The Formula Syntax . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 90
5.2.2 Representation of R Formula: The terms Class . . . . . . . . . . 94
5.3 From a Formula to the Design Matrix .. . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 96
5.3.1 Creating a Model Frame.. . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 96
5.3.2 Creating a Design Matrix . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 102
5.4 Using the lm() and gls() Functions to Fit a Linear Model.. . . . . . 107
5.5 Extracting Information from a Model-Fit Object .. . . . . . . . . . . . . . . . . . 108Contentsxiii
5.6
5.7Tests of Linear Hypotheses for Fixed Effects . .. . . . . . . . . . . . . . . . . . . . 109
Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 110
6
7
8
ARMD Trial: Linear Model with Homogeneous Variance .. . . . . . . . . . .
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
6.2 A Linear Model with Independent Residual Errors
with Homogeneous Variance . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
6.3 Fitting a Linear Model Using the lm() Function . . . . . . . . . . . . . . . . . .
6.4 Fitting a Linear Model Using the gls() Function .. . . . . . . . . . . . . . . .
6.5 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .113
113
Linear Models with Heterogeneous Variance . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.2 Model Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.2.1 Known Variance Weights . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.2.2 Variance Function . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.3 Details of the Model Specification . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.3.1 Groups of Variance Functions . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.3.2 Aliasing in Variance Parameters . . . . . .. . . . . . . . . . . . . . . . . . . .
7.4 Estimation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.4.1 Weighted Least Squares . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.4.2 Likelihood Optimization . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.4.3 Constrained Versus Unconstrained
Parameterization of the Variance Parameters . . . . . . . . . . . . .
7.4.4 Uncertainty in Parameter Estimation .. . . . . . . . . . . . . . . . . . . .
7.5 Model Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.5.1 Pearson Residuals . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.5.2 Influence Diagnostics . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.6 Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.6.1 Tests of Statistical Significance . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.6.2 Confidence Intervals for Parameters . .. . . . . . . . . . . . . . . . . . . .
7.7 Model Reduction and Selection . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.8 Mean-Variance Models . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.8.1 Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
7.8.2 Model Diagnostics and Inference . . . . .. . . . . . . . . . . . . . . . . . . .
7.9 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .123
123
124
124
125
127
127
129
130
130
131
Fitting Linear Models with Heterogeneous Variance:
The gls() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
8.2 Variance-Function Representation: The varFunc Class . . . . . . . . . . .
8.2.1 Variance-Function Constructors . . . . . . .. . . . . . . . . . . . . . . . . . . .
8.2.2 Initialization of Objects of Class varFunc .. . . . . . . . . . . . . . .
8.3 Inspecting and Modifying Objects of Class varFunc . . . . . . . . . . . . . .
8.4 Using the gls() Function to Fit Linear Models
with Heterogeneous Variance . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
113
114
119
120
135
135
136
136
137
138
138
140
140
141
141
145
146
149
149
149
150
151
152
154xiv
Contents
8.5
8.6
9
Extracting Information From a Model-fit Object
of Class gls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 156
Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 158
ARMD Trial: Linear Model with Heterogeneous Variance . . . . . . . . . . .
9.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
9.2 A Linear Model with Independent Residual Errors
and Heterogeneous Variance . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
9.2.1 Fitting the Model Using the gls() Function . . . . . . . . . . . . .
9.3 Linear Models with the varPower(·) Variance-Function . . . . . . . . . . .
9.3.1 Fitting the Models Using the gls() Function .. . . . . . . . . . .
9.3.2 Model-Fit Evaluation . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
9.4 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
Part III
159
159
159
160
162
163
168
171
Linear Fixed-Effects Models for Correlated Data
10 Linear Model with Fixed Effects and Correlated Errors . . . . . . . . . . . . . .
10.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.2 Model Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.3 Details of Model Specification . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.3.1 Variance Structure . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.3.2 Correlation Structure . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.3.3 Serial Correlation Structures . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.3.4 Spatial Correlation Structures . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.4 Estimation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.4.1 Weighted Least Squares . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.4.2 Likelihood-Based Estimation . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.4.3 Constrained Versus Unconstrained
Parameterization of the Variance-Covariance
Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.4.4 Uncertainty in Parameter Estimation .. . . . . . . . . . . . . . . . . . . .
10.5 Model Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.5.1 Residual Diagnostics . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.5.2 Influence Diagnostics . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.6 Inference and Model Selection . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.7 Mean-Variance Models . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
10.8 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11 Fitting Linear Models with Fixed Effects and Correlated Errors:
The gls() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.2 Correlation-Structure Representation: The corStruct Class . . . . . . . .
11.2.1 Correlation-Structure Constructor Functions .. . . . . . . . . . . .
11.3 Inspecting and Modifying Objects of Class corStruct . . . . . . . . . . . . .
11.3.1 Coefficients of Correlation Structures .. . . . . . . . . . . . . . . . . . . .
11.3.2 Semivariogram .. . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.3.3 The corMatrix() Function . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
177
177
178
179
180
181
182
183
185
185
186
188
190
190
191
192
192
194
196
197
197
197
198
199
199
200
202Contents
xv
11.4 Illustration of Correlation Structures . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.4.1 Compound Symmetry: The corCompSymm
Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.4.2 Autoregressive Structure of Order 1:
The corAR1 Class. . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.4.3 Exponential Structure: The corExp Class . . . . . . . . . . . . . . . . .
11.5 Using the gls() Function . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.6 Extracting Information from a Model-Fit Object
of Class gls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
11.7 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12 ARMD Trial: Modeling Correlated Errors for Visual Acuity . . . . . . . .
12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.2 The Model with Heteroscedastic, Independent
Residual Errors Revisited .. . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.2.1 Empirical Semivariogram . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.3 A Linear Model with a Compound-Symmetry
Correlation Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.3.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.3.2 Syntax and Results . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.4 Heteroscedastic Autoregressive Residual Errors .. . . . . . . . . . . . . . . . . .
12.4.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.4.2 Syntax and Results . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.5 General Correlation Matrix for Residual Errors . . . . . . . . . . . . . . . . . . .
12.5.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.5.2 Syntax and Results . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.6 Model-Fit Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.6.1 Scatterplots of Raw Residuals . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.6.2 Scatterplots of Pearson Residuals . . . . .. . . . . . . . . . . . . . . . . . . .
12.6.3 Normalized Residuals . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.7 Inference About the Mean Structure . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.7.1 Models with the General Correlation Structure
and Power Variance Function . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.7.2 Syntax and Results . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
12.8 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
Part IV
202
203
204
206
209
210
211
213
213
213
214
216
216
217
220
220
221
223
223
224
227
227
229
232
234
236
236
238
Linear Mixed-Effects Models
13 Linear Mixed-Effects Model . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.2 The Classical Linear Mixed-Effects Model . . . .. . . . . . . . . . . . . . . . . . . .
13.2.1 Specification at a Level of a Grouping Factor .. . . . . . . . . . . .
13.2.2 Specification for All Data . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.3 The Extended Linear Mixed-Effects Model . . . .. . . . . . . . . . . . . . . . . . . .
245
245
246
246
248
249xvi
Contents
13.4 Distributions Defined by the y and b Random Variables . . . . . . . . . .
13.4.1 Unconditional Distribution of Random Effects .. . . . . . . . . .
13.4.2 Conditional Distribution of y Given the
Random Effects . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.4.3 Additional Distributions Defined by y and b . . . . . . . . . . . . .
13.5 Estimation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.5.1 The Marginal Model Implied by the Classical
Linear Mixed-Effects Model .. . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.5.2 Maximum-Likelihood Estimation . . . . .. . . . . . . . . . . . . . . . . . . .
13.5.3 Penalized Least Squares . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.5.4 Constrained Versus Unconstrained
Parameterization of the Variance-Covariance
Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.5.5 Uncertainty in Parameter Estimation .. . . . . . . . . . . . . . . . . . . .
13.5.6 Alternative Estimation Approaches .. . .. . . . . . . . . . . . . . . . . . . .
13.6 Model Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.6.1 Normality of Random Effects . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.6.2 Residual Diagnostics . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.6.3 Influence Diagnostics . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.7 Inference and Model Selection . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.7.1 Testing Hypotheses About the Fixed Effects .. . . . . . . . . . . . .
13.7.2 Testing Hypotheses About the Variance-
Covariance Parameters . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.7.3 Confidence Intervals for Parameters . .. . . . . . . . . . . . . . . . . . . .
13.8 Mean-Variance Models . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.8.1 Single-Level Mean-Variance Linear
Mixed-Effects Models .. . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.8.2 Multilevel Hierarchies . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.8.3 Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
13.9 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .250
250
14 Fitting Linear Mixed-Effects Models: The lme() Function . . . . . . . . . .
14.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
14.2 Representation of a Positive-Definite Matrix: The pdMat Class . . .
14.2.1 Constructor Functions for the pdMat Class . . . . . . . . . . . . . . .
14.2.2 Inspecting and Modifying Objects of Class pdMat . . . . . . .
14.3 Random-Effects Structure Representation:
The reStruct class . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
14.3.1 Constructor Function for the reStruct Class . . . . . . . . . . . . . . .
14.3.2 Inspecting and Modifying Objects of Class reStruct . . . . .
14.4 The Random Part of the Model Representation:
The lmeStruct Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
14.5 Using the Function lme() to Specify and Fit Linear
Mixed-Effects Models . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .275
275
276
276
279
250
252
254
254
256
257
261
263
264
264
264
265
267
267
267
268
269
270
270
272
272
273
283
284
286
290
292Contents
xvii
14.6 Extracting Information from a Model-Fit Object
of Class lme .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 293
14.7 Tests of Hypotheses About the Model Parameters .. . . . . . . . . . . . . . . . 297
14.8 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 300
15 Fitting Linear Mixed-Effects Models: The lmer() Function . . . . . . . . .
15.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.2 Specification of Models with Crossed and Nested
Random Effects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.2.1 A Hypothetical Experiment with the Effects
of Plates Nested Within Machines .. . . .. . . . . . . . . . . . . . . . . . . .
15.2.2 A Hypothetical Experiment with the Effects
of Plates Crossed with the Effects of Machines .. . . . . . . . . .
15.2.3 General Case . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.3 Using the Function lmer() to Specify and Fit Linear
Mixed-Effects Models . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.3.1 The lmer() Formula . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.4 Extracting Information from a Model-Fit Object
of Class mer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.5 Tests of Hypotheses About the Model Parameters .. . . . . . . . . . . . . . . .
15.6 Illustration of Computations . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
15.7 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .303
303
16 ARMD Trial: Modeling Visual Acuity . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.2 A Model with Random Intercepts and Homogeneous
Residual Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.2.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.2.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.3 A Model with Random Intercepts and the varPower(·)
Residual Variance Function .. . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.3.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.3.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.3.3 Diagnostic Plots . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.4 Models with Random Intercepts and Slopes and the
varPower(·) Residual Variance-Function . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.4.1 Model with a General Matrix D . . . . . .. . . . . . . . . . . . . . . . . . . .
16.4.2 Model with a Diagonal Matrix D . . . . . .. . . . . . . . . . . . . . . . . . . .
16.4.3 Model with a Diagonal Matrix D
and a Constant Treatment Effect . . . . . .. . . . . . . . . . . . . . . . . . . .
16.5 An Alternative Residual Variance Function: varIdent(·) . . . . . . . . . .
16.6 Testing Hypotheses About Random Effects . . . .. . . . . . . . . . . . . . . . . . . .
16.6.1 Test for Random Intercepts . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.6.2 Test for Random Slopes . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .327
327
304
304
305
306
308
308
312
314
315
325
327
328
330
334
334
336
339
346
346
348
353
356
361
362
364xviii
Contents
16.7 Analysis Using the Function lmer() . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.7.1 Basic Results . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.7.2 Simulation-Based p-Values:
The simulate.mer() Method . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.7.3 Test for Random Intercepts . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.7.4 Test for Random Slopes . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
16.8 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17 PRT Trial: Modeling Muscle Fiber Specific-Force .. . . . . . . . . . . . . . . . . . . .
17.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.2 A Model with Occasion-Specific Random Intercepts
for Type-1 Fibers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.2.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.2.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.3 A Mean-Variance Model with Occasion-Specific
Random Intercepts for Type-1 Fibers . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.3.1 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.4 A Model with Heteroscedastic Fiber-Type×Occasion-
Specific Random Intercepts .. . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.4.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.4.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.5 A Model with Heteroscedastic Fiber-Type×Occasion-
Specific Random Intercepts (Alternative Specification) .. . . . . . . . . . .
17.5.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.5.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.6 A Model with Heteroscedastic Fiber-Type×Occasion-
Specific Random Intercepts and a Structured
Matrix D .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.6.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.6.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.7 A Model with Homoscedastic Fiber-Type×Occasion-
Specific Random Intercepts and a Structured
Matrix D .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.7.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.7.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.8 A Joint Model for Two Dependent Variables . . .. . . . . . . . . . . . . . . . . . . .
17.8.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.8.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
17.9 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18 SII Project: Modeling Gains in Mathematics Achievement-Scores . .
18.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.2 A Model with Fixed Effects for School-
and Pupil-Specific Covariates and Random Intercepts
for Schools and Classes . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.2.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.2.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
367
367
372
376
379
380
385
385
385
386
388
397
397
400
400
402
411
411
412
415
415
416
419
419
420
422
422
423
429
431
431
431
432
433Contents
18.3 A Model with an Interaction Between School-
and Pupil-Level Covariates . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.3.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.3.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.4 A Model with Fixed Effects of Pupil-Level
Covariates Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.4.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.4.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.5 A Model with a Third-Degree Polynomial
of a Pupil-Level Covariate in the Mean Structure . . . . . . . . . . . . . . . . . .
18.5.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.5.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.6 A Model with a Spline of a Pupil-Level Covariate
in the Mean Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.6.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.6.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.7 The Final Model with Only Pupil-Level Variables
in the Mean Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.7.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.7.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.8 Analysis Using the Function lmer() . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
18.9 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
xix
438
438
439
442
442
442
444
444
444
448
448
449
450
450
450
457
462
19 FCAT Study: Modeling Attainment-Target Scores . . . . . . . . . . . . . . . . . . . .
19.1 Introduction .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.2 A Fixed-Effects Linear Model Fitted Using
the Function lm() . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.2.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.2.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.3 A Linear Mixed-Effects Model with Crossed Random
Effects Fitted Using the Function lmer() . . . . . .. . . . . . . . . . . . . . . . . . . .
19.3.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.3.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.4 A Linear Mixed-Effects Model with Crossed Random
Effects Fitted Using the Function lme().. . . . . . .. . . . . . . . . . . . . . . . . . . .
19.5 A Linear Mixed-Effects Model with Crossed Random
Effects and Heteroscedastic Residual Errors Fitted
Using lme() .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.5.1 Model Specification . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.5.2 R Syntax and Results . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
19.6 Chapter Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .465
465
20 Extensions of the R Tools for Linear Mixed-Effects Models . . . . . . . . . .
20.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.2 The New pdMatClass: pdKronecker . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.2.1 Creating Objects of Class pdKronecker . . . . . . . . . . . . . . . . . . .491
491
491
493
465
466
466
468
469
469
478
485
485
486
489xx
Contents
20.2.2 Extracting Information from Objects of Class
pdKronecker . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.3 Influence Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.3.1 Preparatory Steps . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.3.2 Influence Diagnostics . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.4 Simulation of the Dependent Variable . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.5 Power Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.5.1 Post Hoc Power Calculations . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.5.2 A Priori Power Calculations
for a Hypothetical Study . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
20.5.3 Power Evaluation Using Simulations .. . . . . . . . . . . . . . . . . . . .
494
497
497
501
509
511
512
515
521
Acronyms . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 525
References .. .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 527
Function Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 531
Subject Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 537List of Tables
Table 1.1Classes of linear models presented in the book . . . . . . . . . . . . . . . . . . .7
Table 2.1
Table 2.2FCAT: Attainment targets for reading comprehension . . . . . . . . . . .
Data frames in the nlmeU package .. . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .32
36
Table 4.1
Table 4.2
Table 4.3Scaled residuals .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
Scaled residuals that involve the hat-matrix elements . . . . . . . . . . . .
Sequential (Type I) and marginal (Type III) testing approaches .77
79
85
Table 5.1
Table 5.2
Table 5.3
Table 5.4
Table 5.5Operators used in an R formula.. . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 90
Expanding elementary formulae .. . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 92
Interpretation of nonessential formula-operators . . . . . . . . . . . . . . . . . 92
Selected arguments of the lm() and gls() functions .. . . . . . . . . . . 107
Extracting results from objects of class lm and gls . . . . . . . . . . . . . . . 109
Table 6.1ARMD: The lm() and gls() estimates for model M6.1 .. . . . . . . . 116
Table 7.1
Table 7.2
Table 7.3
Table 7.4
Table 7.5Groups of variance functions . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .
Variance functions from the <δ>-group . . . . . . .. . . . . . . . . . . . . . . . . . . .
Variance functions from the <δ, μ>-group . . . .. . . . . . . . . . . . . . . . . . . .
Variance functions from the <μ>-group .. . . . . .. . . . . . . . . . . . . . . . . . . .
Pearson residuals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . .Table 8.1
Table 8.2Variance functions in the package nlme . . . . . . .. . . . . . . . . . . . . . . . . . . . 151
Variance structure contained in an object of class gls . . . . . . . . . . . . 157
Table 9.1ARMD: REML estimates for models with variance
functions from the <δ>-group.. . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 167
REML estimates for models with variance functions
from the <δ, μ>- and <μ>-groups .. . . .


