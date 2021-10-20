#imports
import pandas as pd
import plotly.figure_factory as ff
import statistics as stats

#dataframes
data_df = pd.read_csv('data.csv')
#print(data_df)
height_df = data_df['Height(Inches)']

#lists
height_ls = height_df.tolist()

#height statistics
height_mn = stats.mean(height_ls)
height_mo = stats.mode(height_ls)
height_me = stats.median(height_ls)
height_sd = stats.stdev(height_ls)

#printing stats
print(f'standard deviattion of height {height_sd}, mean of height {height_mn}, mode of height {height_mo}, median of height {height_me}')

#first standard deviation
std_1_start, std_1_end = height_mn - height_sd, height_mn + height_sd
h_data_std1 = [result for result in height_ls if result>std_1_start and result<std_1_end]
print(f'percentage of data of height that lies within first standard deviation is {len(h_data_std1)*100.0/len(height_ls)}')

#second standard deviation
std_2_start, std_2_end = height_mn - 2*height_sd, height_mn + 2*height_sd
h_data_std2 = [result for result in height_ls if result>std_2_start and result<std_2_end]
print(f'percentage of data of height that lies within second standard deviation is {len(h_data_std2)*100.0/len(height_ls)}')

#third standard deviation
std_3_start, std_3_end = height_mn - 3*height_sd, height_mn + 3*height_sd
h_data_std3 = [result for result in height_ls if result>std_3_start and result<std_3_end]
print(f'percentage of data of height that lies within third standard deviation is {len(h_data_std3)*100.0/len(height_ls)}')

#graphs
graph1 = ff.create_distplot([height_df.tolist()],['distribution plot for 18 years olds height'],show_hist=False,)
graph1.show()