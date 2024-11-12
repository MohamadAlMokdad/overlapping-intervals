def merge_intervals(intervals):
    # If intervals is empty return an empty list
    if not intervals:
        return []
        
    intervals.sort()
    
    merged = [intervals[0]]
    
    # Iterate through each interval starting from the second
    for current in intervals[1:]:
        # Get the last interval in the merged list to compare with current
        last_merged = merged[-1]
        
        # Checking for an overlap
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            
            merged.append(current)
    
    return merged
