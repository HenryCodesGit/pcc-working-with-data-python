import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(x,y, linewidth=3)

plt.style.use('grayscale')
fig, ax = plt.subplots()
ax.plot(x,y, linewidth=3)

# Setting chart details for the subplot named 'ax'
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value',fontsize=14)
ax.tick_params(labelsize=14) # tick marks

plt.show()