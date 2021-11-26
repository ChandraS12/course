import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image
from plotly.subplots import make_subplots
st.set_page_config(layout="wide")
DATA_URL='new_data.xlsx'
#@st.cache(persist =True)
def load_data():
	data = pd.read_excel(DATA_URL)
	return data

data = load_data()

st.title('L&D Dashboard 👨‍🎓 👩‍🎓')


st.markdown('### Employee-Wise Data')
st.write("An Overview of total courses available on the LMS VS The total courses completed by the employees as well as the courses in progress.\n\n As can be seen in the chart the number of courses Not Started is the highest followed by Completed courses and The Number of courses In Progress being the least")
#st.write(data)
df=data.groupby(['Course Name','Course Status']).count()
#st.write(df)
dataframe=pd.DataFrame({'Course':df.index.get_level_values(0),'Course Status':df.index.get_level_values(1),'Number of Employes':df['Name']})

#dataframe.pivot_table('Course','Course Status',['Number of Employes'])
#st.write(dataframe)

course=dataframe['Course']
course_status=dataframe['Course Status']
number_of_employee=dataframe['Number of Employes']
df1=pd.DataFrame({'Course':course,'Course Status':course_status,'Number of Employes':number_of_employee})
#df1=df1.reset_index(drop=True, inplace=True)
df1.index=range(205)
#st.write(df1)
#df1.pivot_table('Number of Employes',['Course'],'Course Status')
#df.set_index(['Course','Number of Employes','Course Status'],drop=True).unstack('Course Status

#fig=go.Figure()
#fig=fig.add_trace(go.Bar(x=course,y=number_of_employee,color=course_status))
#fig.update_layout(height=1000,width=1000,barmode='stack')
#st.plotly_chart(fig)

fig=px.bar(df1,x="Course",y="Number of Employes",color="Course Status",height=1000,width=1300)

st.plotly_chart(fig)


st.markdown("### Individual Reports")
st.write("Please select the Name you want to see the report for")
employee_names=data['Name'].copy().drop_duplicates()
employee_names=employee_names.to_list()
options=st.multiselect('Employee Name',employee_names)

st.write("The graph below represents the total number of courses Completed, Not Started and In progress by Each Individual Employee")

if not options:
    filtered_data = data.copy()

else:
    filtered_data = data.loc[data["Name"].isin(options)]


#st.write(filtered_data)

df=filtered_data.groupby(['Name','Course Status']).count()
df1=pd.DataFrame({'Name':df.index.get_level_values(0),'Status':df.index.get_level_values(1),'count':df['User Code']})
#st.write(df)
#st.write(df1)

#name=filtered_data['Name']
#topic_name=filtered_data['Topic Name']

#course_name=filtered_data['Course Name']
#course_type=filtered_data['Course Type']  
#category_name=filtered_data['Category Name']
#course_status=filtered_data['Course Status']
#count=course_status.count()
#total_time=filtered_data['Total Access Time']
#course_mandatory=filtered_data['Course Mandatory']
name=df1['Name']
status=df1['Status']
count=df1['count']


fig2=px.bar(df1,x='Status',y='count',color=name,height=600,width=1000)

st.plotly_chart(fig2)



#fig1 = px.scatter(df,x=df.index.get_level_values(0), y='Course Name', color=df.index.get_level_values(1),
 #                title="Course Status",height=800,width=800)

#st.plotly_chart(fig1)


#fig1.add_trace(go.Bar(
#   x=clients,
#   y=offers,
#   name='Offers',
#   text=offers,
#    marker_color='lightsalmon'
#))
#fig1.add_trace(go.Bar(
#   x=clients,
#   y=joinings,
#   name='Joinings',
#   text=joinings,
#    marker_color='darkred'
#))



st.markdown("### Parameter Wise Score")

#st.write(data3)
data4='score_Data.xlsx'
def load_data():
    data5=pd.read_excel(data4)
    return data5

data5= load_data()
#st.write(data5)
name=data5['Name'].drop_duplicates()


options2=st.multiselect('Employee Name',name)

st.write("Each Course is divided in Parameters that you get scored in when you complete a course, there are essentially *24* Parameters in which you can get scored on. \n\n You can select *Desired Scores* in the drop down to view how you compare to the Desired Score")
if not options2:
    filtered_data5 = data5.copy()

else:
    filtered_data5 = data5.loc[data5["Name"].isin(options2)]

#st.write(filtered_data5)

parameters=filtered_data5['Parameter']
score=filtered_data5['Score']
names=filtered_data5['Name']


fig5=px.line(x=parameters,y=score,color=names)
fig5.update_layout(width=1500,height=500)

st.plotly_chart(fig5)


st.write("### Domain Wise Score")
st.write("Furthermore the Parameters are Divided into *4* Domains Namely: \n\n 1. Soft Skills \n 2. Functional \n 3. Technical \n 4. Motivational")
st.write("Hover Over the graph to see your individual Domain and Parameter Score.")
fig7=px.treemap(filtered_data5,path=[px.Constant('Name'),'Domain','Parameter'],values='Score')
fig7.update_layout(width=1000,height=800)
st.plotly_chart(fig7)

#st.write(data5)
grouped_data=data5.groupby('Name').sum()
#st.write(grouped_data)
df=grouped_data.sort_values('Score')
#max_score=score.max()
#st.write(df)
st.markdown("### Final Score")
st.write('This Graph Shows the total score of each Individual ranging from Minimum attained score to Maximum attained score.')
fig6=px.area(df, x=df.index,y='Score')
fig6.update_layout(width=1000,height=500)

st.plotly_chart(fig6)

















 
