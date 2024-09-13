import csv
from collections import Counter

def analyze_election(file_path):
    vote_counter = Counter()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vote_counter[row['Candidate']] += 1
    total_votes = sum(vote_counter.values())
    vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in vote_counter.items()}
    winner = max(vote_counter, key=vote_counter.get)
    winner_votes = vote_counter[winner]
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in vote_counter.items():
        print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    with open("election_results.txt", "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in vote_counter.items():
            file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")
file_path = 'election_data.csv'
analyze_election(file_path)


