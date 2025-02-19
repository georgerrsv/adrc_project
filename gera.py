import matplotlib.pyplot as plt
import pandas as pd

def plot_comparison(ping_file_10, ping_file_15, ping_file_20):
    ping_data_10 = pd.read_csv(ping_file_10, header=None)
    ping_data_15 = pd.read_csv(ping_file_15, header=None)
    ping_data_20 = pd.read_csv(ping_file_20, header=None)

    plt.figure(figsize=(10, 6))

    plt.plot(ping_data_10.index, ping_data_10[0], label='Ping Jitter 10', color='blue')
    plt.plot(ping_data_15.index, ping_data_15[0], label='Ping Jitter 15', color='green')
    plt.plot(ping_data_20.index, ping_data_20[0], label='Ping Jitter 20', color='red')

    plt.xticks(range(0, len(ping_data_20), 5))

    plt.title('Comparação de Jitter (Ping) - Níveis 10, 15, 20')
    plt.xlabel('Índice')
    plt.ylabel('Jitter (ms)')
    plt.legend()

    plt.show()

ping_file_10 = 'dados/ping_jitter/ping_jitter_10.csv'
ping_file_15 = 'dados/ping_jitter/ping_jitter_15.csv'
ping_file_20 = 'dados/ping_jitter/ping_jitter_20.csv'

plot_comparison(ping_file_10, ping_file_15, ping_file_20)

def plot_comparison_iperf_jitter(iperf_jitter_file_10, iperf_jitter_file_15, iperf_jitter_file_20):
    iperf_jitter_data_10 = pd.read_csv(iperf_jitter_file_10, header=None)
    iperf_jitter_data_15 = pd.read_csv(iperf_jitter_file_15, header=None)
    iperf_jitter_data_20 = pd.read_csv(iperf_jitter_file_20, header=None)

    plt.figure(figsize=(10, 6))
    plt.plot(iperf_jitter_data_10.index, iperf_jitter_data_10[0], label='Iperf Jitter 10', color='blue')
    plt.plot(iperf_jitter_data_15.index, iperf_jitter_data_15[0], label='Iperf Jitter 15', color='green')
    plt.plot(iperf_jitter_data_20.index, iperf_jitter_data_20[0], label='Iperf Jitter 20', color='red')

    plt.xticks(range(0, len(iperf_jitter_data_20), 5))
    plt.title('Comparação de Jitter (Iperf) - Níveis 10, 15, 20')
    plt.xlabel('Índice')
    plt.ylabel('Jitter (ms)')
    plt.legend()
    plt.show()

iperf_jitter_file_10 = 'dados/iperf_jitter/iperf_jitter_10.csv'
iperf_jitter_file_15 = 'dados/iperf_jitter/iperf_jitter_15.csv'
iperf_jitter_file_20 = 'dados/iperf_jitter/iperf_jitter_20.csv'

plot_comparison_iperf_jitter(iperf_jitter_file_10, iperf_jitter_file_15, iperf_jitter_file_20)

def plot_comparison_delay_jitter10(ping_delay_file, ping_jitter_file, level):
    ping_delay_data = pd.read_csv(ping_delay_file, header=None)
    ping_jitter_data = pd.read_csv(ping_jitter_file, header=None)

    plt.figure(figsize=(10, 6))
    plt.plot(ping_delay_data.index, ping_delay_data[0], label=f'Ping Delay {level}', color='red')
    plt.plot(ping_jitter_data.index, ping_jitter_data[0], label=f'Ping Jitter {level}', color='blue')
    plt.xticks(range(0, len(ping_delay_data), 5))
    plt.title(f'Comparação de Delay e Jitter (Ping) - Nível {level}')
    plt.xlabel('Índice')
    plt.ylabel('Tempo (ms)')
    plt.legend()
    plt.show()

nivel = 10
ping_delay_file = f'dados/ping_delay/ping_delay_{nivel}.csv'
ping_jitter_file = f'dados/ping_jitter/ping_jitter_{nivel}.csv'

plot_comparison_delay_jitter10(ping_delay_file, ping_jitter_file, nivel)

def plot_comparison_delay_jitter15(ping_delay_file, ping_jitter_file, level):
    ping_delay_data = pd.read_csv(ping_delay_file, header=None)
    ping_jitter_data = pd.read_csv(ping_jitter_file, header=None)

    plt.figure(figsize=(10, 6))
    plt.plot(ping_delay_data.index, ping_delay_data[0], label=f'Ping Delay {level}', color='red')
    plt.plot(ping_jitter_data.index, ping_jitter_data[0], label=f'Ping Jitter {level}', color='blue')
    plt.xticks(range(0, len(ping_delay_data), 5))
    plt.title(f'Comparação de Delay e Jitter (Ping) - Nível {level}')
    plt.xlabel('Índice')
    plt.ylabel('Tempo (ms)')
    plt.legend()
    plt.show()

nivel = 15
ping_delay_file = f'dados/ping_delay/ping_delay_{nivel}.csv'
ping_jitter_file = f'dados/ping_jitter/ping_jitter_{nivel}.csv'

plot_comparison_delay_jitter15(ping_delay_file, ping_jitter_file, nivel)

def plot_comparison_delay_jitter20(ping_delay_file, ping_jitter_file, level):
    ping_delay_data = pd.read_csv(ping_delay_file, header=None)
    ping_jitter_data = pd.read_csv(ping_jitter_file, header=None)

    plt.figure(figsize=(10, 6))
    plt.plot(ping_delay_data.index, ping_delay_data[0], label=f'Ping Delay {level}', color='red')
    plt.plot(ping_jitter_data.index, ping_jitter_data[0], label=f'Ping Jitter {level}', color='blue')
    plt.xticks(range(0, len(ping_delay_data), 5))
    plt.title(f'Comparação de Delay e Jitter (Ping) - Nível {level}')
    plt.xlabel('Índice')
    plt.ylabel('Tempo (ms)')
    plt.legend()
    plt.show()

nivel = 20
ping_delay_file = f'dados/ping_delay/ping_delay_{nivel}.csv'
ping_jitter_file = f'dados/ping_jitter/ping_jitter_{nivel}.csv'

plot_comparison_delay_jitter20(ping_delay_file, ping_jitter_file, nivel)

import matplotlib.pyplot as plt
import pandas as pd

def plot_comparison2(ping_file_10, ping_file_15, ping_file_20):
    ping_data_10 = pd.read_csv(ping_file_10, header=None)
    ping_data_15 = pd.read_csv(ping_file_15, header=None)
    ping_data_20 = pd.read_csv(ping_file_20, header=None)

    plt.figure(figsize=(10, 6))

    plt.plot(ping_data_10.index, ping_data_10[0], label='Ping Jitter 10', color='blue')
    plt.plot(ping_data_15.index, ping_data_15[0], label='Ping Jitter 15', color='green')
    plt.plot(ping_data_20.index, ping_data_20[0], label='Ping Jitter 20', color='red')

    plt.xticks(range(0, len(ping_data_20), 5))

    plt.title('Comparação de Jitter (Ping) - Níveis 10, 15, 20')
    plt.xlabel('Índice')
    plt.ylabel('Jitter (ms)')
    plt.legend()

    plt.show()

ping_file_10 = 'dados/ping_jitter/ping_jitter_10.csv'
ping_file_15 = 'dados/ping_jitter/ping_jitter_15.csv'
ping_file_20 = 'dados/ping_jitter/ping_jitter_20.csv'

plot_comparison2(ping_file_10, ping_file_15, ping_file_20)

def plot_comparison3(ping_file_10, ping_file_15, ping_file_20):
    ping_data_10 = pd.read_csv(ping_file_10, header=None)
    ping_data_15 = pd.read_csv(ping_file_15, header=None)
    ping_data_20 = pd.read_csv(ping_file_20, header=None)

    filtered_data_10 = ping_data_10.iloc[31:41]
    filtered_data_15 = ping_data_15.iloc[46:61]
    filtered_data_20 = ping_data_20.iloc[61:81]

    plt.figure(figsize=(10, 6))

    plt.plot(filtered_data_10.index, filtered_data_10[0], label='Ping Jitter 10', color='blue')
    plt.plot(filtered_data_15.index, filtered_data_15[0], label='Ping Jitter 15', color='green')
    plt.plot(filtered_data_20.index, filtered_data_20[0], label='Ping Jitter 20', color='red')

    plt.xticks(range(31, 81, 5))

    plt.title('Comparação de Jitter (Ping) - Níveis 10, 15, 20 com Padding 3500')
    plt.xlabel('Índice')
    plt.legend()

    plt.show()

ping_file_10 = 'dados/ping_jitter/ping_jitter_10.csv'
ping_file_15 = 'dados/ping_jitter/ping_jitter_15.csv'
ping_file_20 = 'dados/ping_jitter/ping_jitter_20.csv'

plot_comparison3(ping_file_10, ping_file_15, ping_file_20)