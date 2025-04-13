def max_non_overlapping_meetings(meetings):
    if not meetings:
        return 0
    
    meetings.sort(key=lambda x: x[1])  # Sort by end time
    count = 1
    last_end = meetings[0][1]

    for start, end in meetings[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count

meeting_times = [(1, 3), (2, 4), (3, 5), (7, 8)]
print(max_non_overlapping_meetings(meeting_times))
