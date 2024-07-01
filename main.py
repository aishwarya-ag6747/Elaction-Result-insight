import pandas as pd

# Load the election results data from the CSV file
data = pd.read_csv('results_2024_winners.csv')

# Convert 'Margin Votes' to numeric
data['Margin Votes'] = pd.to_numeric(data['Margin Votes'], errors='coerce').fillna(0).astype(int)

# Common Insights
# 1. Winning Party Distribution
winning_party_distribution = data['Winning Party'].value_counts().reset_index()
winning_party_distribution.columns = ['Winning Party', 'Seats Won']
winning_party_distribution.to_csv('winning_party_distribution.csv', index=False)

# 2. Close Contests (Assuming a close contest has a margin of less than 1000 votes)
close_contests = data[data['Margin Votes'] < 1000]
close_contests.to_csv('close_contests.csv', index=False)

# 3. State-wise Party Performance
state_party_performance = data.groupby(['State', 'Winning Party']).size().unstack(fill_value=0)
state_party_performance.to_csv('state_party_performance.csv')

# 4. Stronghold Constituencies (Winning party with large margin, assume margin > 10000)
stronghold_constituencies = data[data['Margin Votes'] > 10000]
stronghold_constituencies.to_csv('stronghold_constituencies.csv', index=False)

# 5. Runner-Up Analysis
runner_up_analysis = data['Runner-up Party'].value_counts().reset_index()
runner_up_analysis.columns = ['Runner-up Party', 'Number of Runner-ups']
runner_up_analysis.to_csv('runner_up_analysis.csv', index=False)

# Unique Insights for Script 2
# 6. Uncontested Seats (Very large winning margins, assume margin > 50000)
uncontested_seats = data[data['Margin Votes'] > 50000]
uncontested_seats.to_csv('uncontested_seats.csv', index=False)

# 7. Runner-Up Impact (Close second places)
runner_up_impact = data[data['Margin Votes'] < 2000]
runner_up_impact.to_csv('runner_up_impact.csv', index=False)

# 8. Top 5 States by Number of Seats
top_states_by_seats = data['State'].value_counts().head(5).reset_index()
top_states_by_seats.columns = ['State', 'Number of Seats']
top_states_by_seats.to_csv('top_states_by_seats.csv', index=False)

# 9. Party-wise Average Margin of Victory
party_average_margin = data.groupby('Winning Party')['Margin Votes'].mean().reset_index()
party_average_margin.columns = ['Winning Party', 'Average Margin of Victory']
party_average_margin.to_csv('party_average_margin.csv', index=False)

# 10. Number of Candidates per Party
candidates_per_party = data['Winning Party'].value_counts().reset_index()
candidates_per_party.columns = ['Party', 'Number of Candidates']
candidates_per_party.to_csv('candidates_per_party.csv', index=False)
