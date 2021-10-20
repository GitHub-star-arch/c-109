#imports
import pandas as pd
import plotly.figure_factory as ff
import statistics as stats

#dataframes
data_df = pd.read_csv('data.csv')
#print(data_df)
weight_df = data_df['Weight(Pounds)']

#lists
weight_ls = weight_df.tolist()

#weight statistics
weight_mn = weight_df.mean()
weight_mo = weight_df.mode()
weight_me = weight_df.median()
weight_sd = stats.stdev(weight_ls)

#printing stats
print(f'standard deviattion of weight {weight_sd}, mean of weight {weight_mn}, mode of weight {weight_mo}, median of weight {weight_me}')

#first standard deviation
std_1_start, std_1_end = weight_mn - weight_sd, weight_mn + weight_sd
w_data_std1 = [result for result in weight_ls if result>std_1_start and result<std_1_end]
print(f'percentage of data of weight that lies within first standard deviation is {len(w_data_std1)*100.0/len(weight_ls)}')

#second standard deviation
std_2_start, std_2_end = weight_mn - 2*weight_sd, weight_mn + 2*weight_sd
w_data_std2 = [result for result in weight_ls if result>std_2_start and result<std_2_end]
print(f'percentage of data of weight that lies within second standard deviation is {len(w_data_std2)*100.0/len(weight_ls)}')

#third standard deviation
std_3_start, std_3_end = weight_mn - 3*weight_sd, weight_mn + 3*weight_sd
w_data_std3 = [result for result in weight_ls if result>std_3_start and result<std_3_end]
print(f'percentage of data of weight that lies within third standard deviation is {len(w_data_std3)*100.0/len(weight_ls)}')

#graphs
graph2 = ff.create_distplot([weight_df.tolist()],['distribution plot for 18 years olds weight'],show_hist=False)
graph2.show()