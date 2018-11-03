import csv

with open('election_data.csv', newline='') as csvfile:
    csvfile.readline()
    data = list(csv.reader(csvfile))
    totVotes = len(data)
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {totVotes}")
    print(f"-------------------------")
    candidates = [line[2] for line in data]
    uCandidates = list(set(candidates))
    winVotes = 0
    results = []
    for candidate in uCandidates:
        sumVotes = 0
        i_result = []
        for voted in candidates:
            if voted == candidate:
                sumVotes += 1
        if sumVotes > winVotes:
            winner = candidate
            winVotes = sumVotes
        print(f"{candidate}: {'{:.3f}'.format(100*(sumVotes/totVotes))}% ({'{:,.0f}'.format(sumVotes)})")
        i_result.append([candidate, sumVotes/totVotes, sumVotes])
        results.append(i_result)
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    
    with open("Poll_Results.csv", "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Candidate", "Percentage", "Number of Votes"])
        writer.writerows(results)