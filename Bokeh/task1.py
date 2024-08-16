from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
import webbrowser

# Завантаження даних
df = pd.read_csv("/Users/admin/Desktop/DataSoftwareEngineeringCourse/Bokeh/Titanic-Dataset.csv")

# Обробка пропущених значень
df['Age'].fillna(df['Age'].median(), inplace=True)  
df['Cabin'].fillna('Unknown', inplace=True)        
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Створення вікових груп
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 24, 59, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'], right=False)

# Графік 1: Кількість виживших по вікових групах
survivors_count = df[df['Survived'] == 1].groupby('AgeGroup').size().reset_index(name='Count')
source1 = ColumnDataSource(survivors_count)
age_groups = survivors_count['AgeGroup'].astype(str).tolist()

p1 = figure(x_range=age_groups, title="Number of Survivors by Age Group",
            x_axis_label='Age Group', y_axis_label='Number of Survivors',
            height=400, width=600)

p1.vbar(x='AgeGroup', top='Count', source=source1, width=0.5, color="magenta", alpha=0.8)

# Додавання Hover Tool для першого графіка
hover1 = HoverTool()
hover1.tooltips = [("Age Group", "@AgeGroup"), ("Count", "@Count")]
p1.add_tools(hover1)

# Збереження першого графіка
output_file("survival_count_by_age_group.html")
show(p1)

# Графік 2: Рівень виживання по вікових групах
survival_rate = df.groupby('AgeGroup')['Survived'].mean() * 100
survival_rate = survival_rate.reset_index()
source2 = ColumnDataSource(survival_rate)
age_groups = survival_rate['AgeGroup'].astype(str).tolist()
output_file("survival_rate_by_age_group.html")
p2 = figure(x_range=age_groups, title="Survival Rate by Age Group",
            x_axis_label='Age Group', y_axis_label='Survival Rate (%)',
            height=400, width=600)

p2.vbar(x='AgeGroup', top='Survived', source=source2, width=0.4, color="navy", alpha=0.7)

# Додавання Hover Tool для другого графіка
hover2 = HoverTool()
hover2.tooltips = [("Age Group", "@AgeGroup"), ("Survival Rate (%)", "@Survived{0.0}%")]
p2.add_tools(hover2)

# Збереження другого графіка

show(p2)

# Графік 3: Рівень виживання по класам та статі
survival_class_gender = df.groupby(['Pclass', 'Sex'])['Survived'].mean().reset_index()
survival_class_gender['Survived'] *= 100  # Перетворюємо в відсотки
source3 = ColumnDataSource(survival_class_gender)

p3 = figure(x_range=[f'{cls}-{gen}' for cls in ['1', '2', '3'] for gen in ['male', 'female']],
            title="Survival Rate by Class and Gender",
            x_axis_label='Class-Gender', y_axis_label='Survival Rate (%)',
            height=400, width=600, toolbar_location=None)

p3.vbar(x='Pclass', top='Survived', source=source3, width=0.2, color="navy", alpha=0.7, legend_field="Sex")

# Додавання Hover Tool для третього графіка
hover3 = HoverTool()
hover3.tooltips = [("Class", "@Pclass"), ("Gender", "@Sex"), ("Survival Rate (%)", "@Survived{0.0}%")]
p3.add_tools(hover3)

# Збереження третього графіка
output_file("survival_class_gender.html")
show(p3)

# Графік 4: Fare vs Survival
df['color'] = df['Pclass'].map({1: 'blue', 2: 'green', 3: 'red'})
source4 = ColumnDataSource(df)

p4 = figure(title="Fare vs Survival",
            x_axis_label='Fare', y_axis_label='Survived',
            height=400, width=600)

p4.scatter(x='Fare', y='Survived', source=source4, color='color', legend_field='Pclass',
           fill_alpha=0.6, size=8)

# Додавання Hover Tool для четвертого графіка
hover4 = HoverTool()
hover4.tooltips = [("Fare", "@Fare"), ("Survived", "@Survived"), ("Class", "@Pclass")]
p4.add_tools(hover4)

# Збереження четвертого графіка
output_file("fare_vs_survival.html")
show(p4)

# Автоматичне відкриття HTML-файлів
webbrowser.open("survival_count_by_age_group.html")
webbrowser.open("survival_rate_by_age_group.html")
webbrowser.open("survival_class_gender.html")
webbrowser.open("fare_vs_survival.html")
