def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.
    Each activity is (start_time, finish_time).
    Activities that finish at time t may be followed by one starting at t.
    """
    # Sort by finish time: earliest finishing activity is chosen first.
    sorted_activities = sorted(activities, key=lambda activity: activity[1])

    selected = []
    last_finish = float("-inf")

    for start, finish in sorted_activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


if __name__ == "__main__":
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
    chosen = activity_selection(activities)
    print("Selected activities:", chosen)
    print("Maximum count:", len(chosen))
