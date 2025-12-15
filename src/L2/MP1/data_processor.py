# Filename: src/L2/MP1/data_processor.py
# Mini Project 1: Data Processor

def get_scores():
    """Get scores from user with error handling."""
    try:
        scores_input = input("Enter scores separated by commas: ")
        if not scores_input.strip():
            print("No input provided. Using sample data.")
            return [85, 90, 85, 92, 90, 88, 85, 75, 95, 88]
        
        scores = [int(score.strip()) for score in scores_input.split(",")]
        return scores
    except ValueError:
        print("Error: Please enter valid numbers separated by commas!")
        print("Using sample data instead.")
        return [85, 90, 85, 92, 90, 88, 85, 75, 95, 88]
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def process_scores(scores):
    """Process scores using sets, tuples, and comprehensions."""
    if not scores:
        return None, None, None, None
    
    # Remove duplicates using set
    unique_scores = set(scores)
    
    # Create tuples of (score, frequency) using list comprehension
    score_tuples = [(score, scores.count(score)) for score in unique_scores]
    
    # Transform: get only scores above 70 using comprehension
    passing_scores = [score for score in unique_scores if score >= 70]
    
    # Calculate average using comprehension and built-in functions
    average = sum(unique_scores) / len(unique_scores) if unique_scores else 0
    
    return unique_scores, score_tuples, passing_scores, average


def display_results(original, unique, tuples, passing, average):
    """Display all results in a formatted way."""
    print("=" * 50)
    print("DATA PROCESSING RESULTS")
    print("=" * 50)
    
    print(f"\nOriginal Scores: {original}")
    print(f"Total scores: {len(original)}")
    
    print(f"\nUnique Scores (Set): {sorted(unique)}")
    print(f"Total unique scores: {len(unique)}")
    
    print(f"\nScore Tuples (Score, Frequency):")
    for score, count in sorted(tuples):
        print(f"  {score}: appears {count} time(s)")
    
    print(f"\nPassing Scores (>=70): {sorted(passing)}")
    print(f"Passing count: {len(passing)}")
    
    if unique:
        print(f"\nStatistics:")
        print(f"  Minimum score: {min(unique)}")
        print(f"  Maximum score: {max(unique)}")
        print(f"  Average score: {average:.2f}")


def main():
    """Main program function."""
    print("=" * 50)
    print("STUDENT SCORE DATA PROCESSOR")
    print("=" * 50)
    print()
    
    scores = get_scores()
    
    if not scores:
        print("No valid scores to process. Exiting.")
        return
    
    unique, tuples, passing, average = process_scores(scores)
    
    if unique is None:
        print("Error processing scores.")
        return
    
    display_results(scores, unique, tuples, passing, average)
    
    print("\n" + "=" * 50)
    print("Processing complete!")
    print("=" * 50)


# Run the program
if __name__ == "__main__":
    main()

