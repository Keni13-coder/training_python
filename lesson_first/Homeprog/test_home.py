import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# print(data.head())
# print(pd.get_dummies(data['whoAmI']))

# {x:True if x =='robot' else x:False for x in data['whoAmI']}
# robot_data = pd.DataFrame({x:1 if x == 'robot' else 0 for x in data['whoAmI']})
# print(robot_data.head())
robot = [1  if x == 'robot' else 0 for x in data['whoAmI']]
human = [1  if x == 'human' else 0 for x in data['whoAmI']]
new_data = pd.DataFrame({'robot': robot,
                         'human':human})
print(new_data)
print(pd.get_dummies(data['whoAmI']))