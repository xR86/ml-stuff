print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
fd = open("./visualizer/matplot-text.txt","r")
fd2 = open("./visualizer/matplot-output.txt","w")

pullData = fd.read()
fd.close()

dataList = pullData.split('\n')
xList = []
yList = []
x2List = []
y2List = []
data_typeList = []
for eachLine in dataList:
    if len(eachLine) > 1:
        x, y, data_type = eachLine.split(' ')
        xList.append([float(x)])
        yList.append([float(y)])
        data_typeList.append(int(data_type))

print yList

index_change = data_typeList.index(2) #find training data index
#train: xList[:index_change], yList[:index_change]
diabetes_X_train = np.array( xList[:index_change] )
diabetes_y_train = np.array( yList[:index_change] )
#test: xList[index_change:], yList[index_change:]
diabetes_X_test = np.array( xList[index_change:] )
diabetes_y_test = np.array( yList[index_change:] )

print diabetes_y_train

"""
diabetes = datasets.load_diabetes()
print type(diabetes), diabetes.data
# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

#print type(diabetes_X_train), 'diabetes_X_train: ', diabetes_X_train

exit()
"""

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
#print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

prediction = regr.predict(diabetes_X_test)
#prediction = prediction[:]
print 'Haoleo, prediction #### ia sa-ti citeasca baba in regresia liniara !!!', prediction
print "Length !", len(diabetes_X_test)
for i in range(len(diabetes_X_test)):
	#print diabetes_X_test[i][0]
	fd2.write(str(diabetes_X_test[i][0]) + ' ' + str(prediction[i][0]) + '\n')

fd2.close()

plt.xticks(())
plt.yticks(())

plt.show()