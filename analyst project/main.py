import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv(r'c:\Users\barga\OneDrive\Documents\Desktop\data.csv')

# data cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.info())
df=df.drop_duplicates()

#numeric columns

df['price']=df['price'].astype(str).str.replace(",","").astype(int)

df['area']=df['area'].astype(str).str.replace(",","").astype(int)

df['rate_per_sqft'] =df['rate_per_sqft'].astype(str).str.replace(",","").astype(int)

print(df['rate_per_sqft'])

#categorical columns cleaning
df['status']= df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower().map({'approved by rera':True,'not approved by rera': False})
print(df['rera_approval'])
df=df.drop_duplicates()
#print(df.info())
# ques1. which is the costliest flat in thr dataset?

costliest_flat= df.loc[df['price'].idxmax()]

print(f"The costliest flat in the dataset is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']}, built by {costliest_flat['builder_name']}. It is priced at {costliest_flat['price']/100000} lakhs and has an area of {costliest_flat['area']} sqft with a rate of {costliest_flat['rate_per_sqft']} per sqft. The flat is currently {costliest_flat['status']} and RERA approved: {costliest_flat['rera_approval']} society: {costliest_flat['socity']}. The company name is {costliest_flat['company_name']}.")

# ques2. which locality has the highest average price?

highest_avg_price = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price}.")
print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(20))

#ques3. which locality has the highest rate per sqft?

highest_avg_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest average rate per sqft is {highest_avg_rate_per_sqft}.")
#ques4. do ready to move properties cost more than under construction properties?

ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
print(f"Average price of ready to move properties: {ready_to_move_avg_price}")
print(f"Average price of under construction properties: {under_construction_avg_price}")
#ques5. do rera approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print(f"RERA approved properties command a price premium. Average price of RERA approved properties: {rera_approved_avg_price}, Average price of non-RERA approved properties: {not_rera_approved_avg_price}")
else:
    print(f"RERA approved properties do not command a price premium. Average price of RERA approved properties: {rera_approved_avg_price}, Average price of non-RERA approved properties: {not_rera_approved_avg_price}")   

    # ques6.how does area impact the price?
sns.scatterplot(data=df, x='area', y='price')
#plt.show()

    #ques7.which bhk configuration is the most expensive?
more_expensive_bhk = df.groupby('bhk_count')['price'].mean().idxmax()
print(f"The most expensive BHK configuration is {more_expensive_bhk} BHK.")


    # ques8.which property type is the costliest?
costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest property type is {costliest_property_type}.")


    #  ques 9.Do certain builder price higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))
# print name of top 5
print("Top 5 builders with highest average rate per sqft:")
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder,end=", ")

    # ques 10.are larger home more expensive per sqft?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.xlabel('Area')
plt.ylabel('Rate per Sqft')
plt.title('Area vs Rate per Sqft')
plt.show()     
