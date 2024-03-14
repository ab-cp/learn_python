import matplotlib.pyplot as plt
import pandas as pd

# Sample data
'''data = """707496805,553,22.4,WindowServer
1707496805,993,5.2,Terminal
1707496805,28854,2.7,(Renderer)
1707496807,553,11.3,WindowServer
1707496807,1389,5.8,mdworker_shared
1707496807,513,4.3,mds
1707496808,553,14.3,WindowServer
1707496808,28854,5.2,(Renderer)
1707496808,994,2.8,Hub
1707496809,553,14.6,WindowServer
1707496809,546,2.9,bluetoothd
1707496809,28854,2.8,(Renderer)
1707496810,553,14.5,WindowServer
1707496810,49833,3.4,(Renderer)
1707496810,672,3.2,nxtsvc
1707496811,14069,28.1,Helper
1707496811,553,13.6,WindowServer
1707496811,56107,5.7,studio
1707496812,553,13.9,WindowServer
1707496812,1491,7.5,(Renderer)
1707496812,994,2.8,Hub
1707496813,553,14.9,WindowServer
1707496813,28854,2.9,(Renderer)
1707496813,49833,2.6,(Renderer)"""

# Convert data to dataframe
data = [line.split(',') for line in data.split('\n')]
df = pd.DataFrame(data, columns=['TimeStamp', 'Pid', 'CPUUsage', 'ProcessName'])
'''


df = pd.read_csv('your_file.csv', names=['TimeStamp', 'Pid', 'CPUUsage', 'ProcessName'])

# Convert columns to appropriate data types
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], unit='s')
df['Pid'] = df['Pid'].astype(int)
df['CPUUsage'] = df['CPUUsage'].astype(float)

# Get unique processes
processes = df['ProcessName'].unique()

# Plotting
plt.figure(figsize=(10, 6))

for process in processes:
    pid = df[df['ProcessName'] == process]['Pid'].iloc[0]
    cpu_usage = df[df['ProcessName'] == process]['CPUUsage']
    timestamp = df[df['ProcessName'] == process]['TimeStamp']
    plt.plot(timestamp, cpu_usage, label=f'{process} (PID: {pid})')

plt.xlabel('Timestamp')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage Over Time for Different Processes')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
